import os
import numpy as np


root = '/home/minji/gcn/carfusion_to_coco/datasets/carfusion/test/'
seq_list = {'car_penn1', 'car_penn2'}

img_list = []
for seq_name in seq_list:
    img_list += ['/code/datasets/carfusion/test/' + seq_name + '/images_jpg/' + p for p in os.listdir(root + seq_name + '/images_jpg')
                    if os.path.splitext(p)[1] == '.jpg']

# with open("carfusion_test.txt", "w") as f:
#     for img in img_list:
#         if not os.path.exists(img):
#             print(img)
#         f.write(img+'\n')

np.savetxt("carfusion_test.txt", img_list, fmt='%s', delimiter=',')

# np.save("carfusion_test.npy", img_list)