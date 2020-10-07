# Data Engineering 
> A S1.1 course at JADS  
> This is the repository for Assignment 1 of Group 11

## Built With
pandas 1.1.1  
numpy 1.19.1  
flask 1.1.2  
requests  
os  

Google Cloud platform virtual machines  
Google Kubernetes Engine  
Docker  
Insomnia
    
    
## Installing / Getting started

The minimal commands to get the system up and running.

Run the following commands in your Google cloud VM (region: euwest4-a):

```shell
gcloud auth activate-service-account [GOOGLE-SERVICE-ACCOUNT] --key-file=[KEY-FILE]
gcloud auth configure-docker
gcloud auth print-access-token | sudo docker login -u oauth2accesstoken --password-stdin https://eu.gcr.io
```

The Google service account is authorized to publish docker images.

```shell
git clone https://github.com/pjjongenelen/DE_course
or
git pull
```
```shell
cd DE_course/eigen_project/training-db
sudo docker build -t databaseapi:0.0.1 .
sudo docker tag databaseapi:0.0.1 eu.gcr.io/dataengineering-course/databaseapi:0.0.1
sudo docker push eu.gcr.io/dataengineering-course/databaseapi:0.0.1

cd ..
cd training-cp
sudo docker build -t trainingcpapi:0.0.1 .
sudo docker tag trainingcpapi:0.0.1 eu.gcr.io/dataengineering-course/trainingcpapi:0.0.1
sudo docker push eu.gcr.io/dataengineering-course/trainingcpapi:0.0.1

cd ..
cd prediction-cp
sudo docker build -t predictionapi:0.0.1 .
sudo docker tag predictionapi:0.0.1 eu.gcr.io/dataengineering-course/predictionapi:0.0.1
sudo docker push eu.gcr.io/dataengineering-course/predictionapi:0.0.1
```

All necessary images are pushed to the Google cloud image repository.

Before executing the next steps, make sure to:
Create a GKE cluster, and connect to it using the Google Cloud Shell

```shell
kubectl create -f namespace.yaml

helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update
helm install nfs-server stable/nfs-server-provisioner --set persistence.enabled=true,persistence.size=100Gi --namespace=fifaxgb
```

Everything is ready to start creating the persitent volumes and pods.

```shell 
git clone https://github.com/pjjongenelen/DE_course
or
git pull
```

```shell
cd DE_2020/eigen_project/kubernetes-manifests
kubectl create -f nfs-pvc-traindb.yaml
kubectl get pvc --namespace=fifaxgb
kubectl create -f training-db.deployment.yaml
kubectl create -f training-db.service.yaml
kubectl create -f nfs-pvc-modelrepo.yaml
kubectl create -f training-cp.deployment.yaml
kubectl create -f training-cp.service.yaml
kubectl create -f prediction-cp.deployment.yaml
kubectl create -f prediction-cp.service.yaml

kubectl get pods --namespace=fifaxgb
kubectl get services --namespace=fifaxgb
```

The final command should return the external IPs of the components. With these
you can access the system with software such as Insomnia.

## Database

A processed version of the FIFA 19 complete player dataset, found here: https://www.kaggle.com/karangadiya/fifa19
The JSON files data_for_model_creation and data_for_new_prediction are preprocessed to work with the components of this application.  

## Api Reference

In order to access the components, use the following URLs (we use Insomnia):

```shell
http://[TRAIN-DB-EXTERNAL-IP]:5000/training-db/fifaxgb

POST; payload = columns.json
PUT; payload = data_for_model_creation.json
GET; {to check if the data has been put}
```
Now the training dataset is ready.
 
```shell
http://[TRAIN-CP-EXTERNAL-IP]:5002/training-cp/fifa

POST;
```
Model has been trained

```shell
http://[PREDICT-CP-EXTERNAL-IP]:5003/predict-cp/[MODEL-NAME]

POST; 
```
-----
Updated to this point

-----

## Tests

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Locust code
```


