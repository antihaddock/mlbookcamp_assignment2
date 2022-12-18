End of Term term project for 2022 ML Bookcamp course.
Written by Ryan Gallagher

Data utilised in MRI and Alzeimhers dataset from Kaggle
https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers


## How to use this Repo ##

### About the Dataset ###
This is a dataset from kaggle and can be found at: https://www.kaggle.com/datasets/prosperchuks/health-dataset. This dataset is from the US and utilises responses to health surveys and matches this to history of Stroke, Hypertension or Diabetes. It is a cleaned and encoded label encoded dataset of nearly 71 000 responses to a 2015 CDC survey. A range of data on age, BMI, gender along with medical history is supplied.

For the purpose of this assignment only the stroke data is being used for the classification problem (ie I have discarded the hypertension and Diabetes columns from the analysis). This dataset has been downloaded and saved in the `Data` directory as `health_data.csv`.


### Exploratory Data Analysis ###
Data is stored in the `Data` directory. `health_data.csv` is the data utiulised by `notebook.ipynb` for exploratory analysis and modelling. `train.py` also utilises this data to train the Decision Tree Classifier model used in project.  In `train.py` this hyperparameters utilised are from EDA and exploration in `notebook.ipyb`.

The test data created in the test/train/validation split is saved as `test_data.csv`  which can be used to test data to the  developed ML model.

### Data cleaning ###
Given this dataset is a pre cleaned dataset the only cleaning that has been done is the dropping of data columns not in use and sense checking data to check there are no missing values etc.

### Interacting with the model ###

The `flask_test.py` allows local interation with the trained  Classification Tree model. To interact with the model via `flask_test.py` follow these steps:
 1. From the command line run `python predict.py` to utise the flask to service the model. In a separate window run `python flask_test.py` to run the model via flask.
 2.  call `gunicorn --bind 0.0.0.0:5000  predict_outcome:app` from the command line to run this model via gunicorn (linux only)
 
### Using Pip Env and Pip File ###
A pipfile is provided for this repo. To install dependencies call `pipenv install`. To activate the environment call `pipenv shell`. 


 ### Interacting via docker container ###

 A dockerfile is available in this repo to allow a docker image to be created for serving this model. To run this model within docker:
 1. Call `docker build -t mlbookcamp-project .` to build the docker image locally. Once the docker image is built locally calling `docker run -it --rm -p  5000:5000  mlbookcamp-project` will allow interaction with the docker container for  `flask_test.py`. Ensure you do not have a flask or gunicorn server running locally if you wish to interact with the model via docker.

 Additionally Bento ML was used to facilitate deployment of this model and interaction with the model is possible via the Bento deployed on AWS.

 ### Deployment of Bento ML to Elastic Container Repository ###
The method of deployment of this model to AWS has been utilising AWS. The `bentofile.yaml` contains all of the necessary information to create a bentoML container for deployment to AWS.

To create a BentoML image in the root directory of this repo call `bentoml build`. upon completion of the build a tag for the build will appear in the command line. Copy this tag and run the code `bentoml containerize stroke_risk_modelling:tag_here`. This will place the BentoML model into a docker contain utilising information stored in the `bentofile.yaml`. to run this bentoML locally call `docker run -it --rm -p 3000:3000 stroke_risk_modelling:tag_here serve --production` from the command line. replace `tag_here` with the tag number from `bentoml build`.


To deploy to AWS using ECS ensure awscli is installed. A 2 step process is required to utilise your Bento on AWS
1. Deploy the container to AWS Elastic Container Repository (ECR)
2. Connect your container from ECR to Elastic Container Service(ECS)
 
 The following code will deploy you bentoML container to AWS ECR:
 `aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin xxxxx.dkr.ecr.your-region.amazonaws.com`
`your-region` and `xxxxx.dkr.ecr.your-region.amazonaws.com` must be replaced with your AWS region and the location of your ECR repo.

Once you have connected your docker to AWS you need to tage your image for aws
`docker tag mlbookcamp_prediction_stroke:latest xxxxxx.dkr.ecr.ap-southeast-2.amazonaws.com/mlbookcamp_prediction_stroke:latest` again replacing `xxxx` as above

Finally push your bento via `docker push xxxxx.dkr.ecr.your-region.amazonaws.com/mlbookcamp_prediction_stroke:latest`


 ### Deployment of Bento ML to AWS Fargate ###

 To deploy your Bento ML to AWS via Fargate this must be done via the AWS website. The steps that must be followed are:
 1. Open Elastic Container Service (ECS)
 2. Create a cluster. 
 3. Select new Task definition and select Fargate. This is the process to connect your ECR to your ECR cluster. Select the appropriate level of memory 
 and CPU for the task.
 !<img src="./Data/Bento Deployment/Task deployment.jpg" title="Bento Deployment">

 4. Once a cluster & task is created select Tasks and "Run new Task". Under security groups again expose port 3000.
 !<img src="./Data/Bento Deployment/Run Task.jpg" title="Run Tasl">
 Finally open the task you have created and copy the public IP address into your web browser. You will now be able to interact with your Bento ML model


This is what should be available upon successful deployment to AWS Fargate
 !<img src="./Data/Bento Deployment/Bento Deployment.jpg" title="Bento Deployment">
