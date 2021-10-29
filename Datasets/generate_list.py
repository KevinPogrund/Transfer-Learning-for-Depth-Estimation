import os

# Variables
dataset = "not_kitti"  # name of the text file
raw_dir = "../../Unstructured/eval/rgb"  # folder of the raw images
gt_dir = "../../Unstructured/eval/gt"

raw_pics = sorted(os.listdir(raw_dir))
gt_pics = sorted(os.listdir(gt_dir))
if dataset == "kitti":
    with open("{}.txt".format(dataset), 'w') as f:
        for i in range(len(raw_pics)):
            f.write("{}/{} {}/{} 721.533\n".format(raw_dir, raw_pics[i], gt_dir, gt_pics[i]))
            # use a "/" for linux and a "\" for windows
        print("Done KITTI")
else:
    # with open("train_unstructured.txt", 'w') as f:
    #     for i in range(len(raw_pics)):
    #         f.write("{}/{} {}/{} 526.526\n".format(raw_dir, raw_pics[i], gt_dir, gt_pics[i]))
    #     print("Done unstructured")
    with open("../eval_uns.txt", 'w') as f:
        for i in range(len(raw_pics)):
            f.write("rgb/{} gt/{} 526.526\n".format(raw_pics[i], gt_pics[i]))
        print("Done unstructured")


