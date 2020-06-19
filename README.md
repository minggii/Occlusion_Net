Occlusion-Net: 2D/3D Occluded Keypoint Localization Using Graph Networks 
======================

## GCN final project

[N Dinesh Reddy](http://cs.cmu.edu/~dnarapur), [Minh Vo](http://cs.cmu.edu/~mvo), [Srinivasa G. Narasimhan](http://www.cs.cmu.edu/~srinivas/)

IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019. 

[[Project](http://www.cs.cmu.edu/~ILIM/projects/IM/CarFusion/cvpr2019/index.html)] [[Paper](http://openaccess.thecvf.com/content_CVPR_2019/papers/Reddy_Occlusion-Net_2D3D_Occluded_Keypoint_Localization_Using_Graph_Networks_CVPR_2019_paper.pdf)] [[Supp](http://openaccess.thecvf.com/content_CVPR_2019/supplemental/Reddy_Occlusion-Net_2D3D_Occluded_CVPR_2019_supplemental.pdf)] [[Bibtex](http://www.cs.cmu.edu/~ILIM/projects/IM/CarFusion/cvpr2019/occlusion_net.bib) ]


## Installation

### Setting up with docker

All the stable releases of docker-ce installed from https://docs.docker.com/install/

Install *nvidia-docker2* from https://github.com/NVIDIA/nvidia-docker

Setting up the docker

```bash
nvidia-docker build -t occlusion_net .
```

### Setting up data
You need to fill the [Access Form](https://forms.gle/FCUcbt3jD1hB6ja57) to get a email regarding the dataset and setup at using the following commands: 
```
git clone https://github.com/dineshreddy91/carfusion_to_coco
cd carfusion_to_coco
virtualenv carfusion2coco -p python3.6
source carfusion2coco/bin/activate
pip install cython numpy
pip install -r requirements.txt
python download_carfusion.py (This file need to be downloaded by requesting, please fill to get access to the data)
sh carfusion_coco_setup.sh
deactivate
```

The final folder format to train on carfusion data needs to look :

 ```text
Occlusion-Net
    └─datasets
        └─carfusion
            └─train
                └─car_craig1
                    └───images
                        01_0000.jpg
                        01_0001.jpg
                        ...   
                    └───bb
                       01_0000.txt
                       01_0001.txt
                       ...
                    └───gt
                       01_0000.txt   
                       01_0001.txt
                       ...
            └─test
                └─car_penn1
                    └───images
                        01_0000.jpg
                        01_0001.jpg
                        ...   
                    └───bb
                       01_0000.txt
                       01_0001.txt
                       ...
                    └───gt
                       01_0000.txt   
                       01_0001.txt
                       ...
            └─annotations
                car_keypoints_train.json
                car_keypoints_test.json
                
```


### Train

Training the model on the carfusion dataset 

```
sh train.sh occlusion_net <Local_Path_to_Carfusion_dataset>
ex) sh train.sh occlusion_net home/minji/gcn/carfusion_to_coco/datasets/carfusion
``` 


### Test
Download a pretrained model from  [[Google Drive](https://drive.google.com/open?id=1EUmhzeuMUnv5whv0ZmmOHTbtUiWdeDly)]

Run parser.py to generate image url list
```
python parser.py
```

Test the model on the carfusion dataset

```
sh test.sh occlusion_net carfusion_test.txt <Local_Path_to_Carfusion_dataset>
```

### Citation
```
@inproceedings{onet_cvpr19,
author = {Reddy, N. Dinesh and Vo, Minh and Narasimhan, Srinivasa G.},
title = {Occlusion-Net: 2D/3D Occluded Keypoint Localization Using Graph Networks},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
pages = {7326--7335},
year = {2019}
}
```




