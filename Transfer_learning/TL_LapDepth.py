# Code added to the train.py file in LapDepth_Release
# Code was added just before the model was trained

unfreeze_layers = ['layer3.22', 'layer3.21', 'layer3.20', 'layer3.19', 'layer3.18',
                      'layer3.17', 'layer3.16', 'layer3.15', 'layer3.14', 'layer3.13',
                      'layer3.12', 'layer3.11', 'layer3.10', 'layer3.9', 'layer3.8']
    # a list of the layers that I want to unfreeze
    for param in Model.module.parameters():
        param.requires_grad = False  # freeze everything

    for name, child in Model.module.named_children():
        if 'encoder' not in name:
            continue
        for name2, parameters in child.named_parameters():
            # print(name, name2)  # this prints out the name of the layers
            # then the layers that I want unfrozen I add to the list unfreeze_layers
            if any(x in name2 for x in unfreeze_layers):
                parameters.requires_grad = True  # unfreeze the chosen layers

    for name, param in Model.module.named_parameters():
        if param.requires_grad:
            print(name)  # print the layers which have been unfrozen (for checking)