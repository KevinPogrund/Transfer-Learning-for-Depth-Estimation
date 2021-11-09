# Code added to the train.py file in BTS
# Code was added just before the model was trained

unfreeze_layers = ['denseblock4.denselayer24']

    for param in model.parameters():
        param.requires_grad = False  # freeze everything

    for name, child in model.named_children():
        if 'encoder' not in name:
            continue
        for name2, parameters in child.named_parameters():
            # print(name, name2)  this prints out the name of the layers
            # then the layers that I want unfrozen I add to the list unfreeze_layers
            if any(x in name2 for x in unfreeze_layers):
                parameters.requires_grad = True

    for name, param in model.named_parameters():
        if param.requires_grad:
            print(name)  # print the layers which have been unfrozen (for checking)
