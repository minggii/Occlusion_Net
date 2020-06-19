BASE=$3
docker run -v $PWD:/code \
        -v $BASE/annotations:/code/datasets/carfusion/annotations \
        -v $BASE/test:/code/datasets/carfusion/test \
        --shm-size=32GB --runtime=nvidia $1 python infer.py \
        -ut $2 \
        -v True \
        -cfg data/occlusion_net_test.yaml