# ML_Deploy_Monitor

Model : simple regression model
deployment : docker
provisioning : flask

Dataset : https://www.kaggle.com/tmcketterick/heights-and-weights

## Deployment
1. build docker image
docker image build --rm -t height_weight .
2. run docker container
docker run --rm -p 8000:8000 height_weight
3. predict using 
http://127.0.0.1:8000/predict?1.7

## jenkins
1. install and setup jenkins
2. configure job to build. (webhook requires your jenkins to be exposed to internet)

## nginx and Gunicorn
1.

