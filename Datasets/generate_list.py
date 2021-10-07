import os

# Variables
dateset = "kitti"  # name of the text file
raw_dir = "/home/kevin/Project_Local/KITTI_validation_tests/depth_selection/test_depth_completion_anonymous/image"  # folder of the raw images
gt_dir = "/home/kevin/Project_Local/KITTI_validation_tests/depth_selection/test_depth_completion_anonymous/velodyne_raw"
seperator = "/"  # path seperator ('/' for linux, '\' for Windows)

raw_pics = os.listdir(raw_dir)
gt_pics = os.listdir(gt_dir)
with open("{}.txt".format(dateset), 'w') as f:
    if dateset == "kitti":
        # f = open("{}.txt".format(dateset), 'w')
        for i in range(len(raw_pics)):
            f.write("{}/{} {}/{} 721.533\n".format(raw_dir, raw_pics[i], gt_dir, gt_pics[i]))
    else:
        print("not kitti")
