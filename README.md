# Mice Protein Expression: Mice Down Syndrome through Protein Expression Analysis.

## Problem Statement:
Protein Expression classification models are frequently viewed not only as a difficult task, but also as a classification problem that, in some cases, requires a trade-off between accuracy and efficiency in analysis validation due to the large amount of data available.  

Expression levels of 77 proteins measured in the cerebral cortex of 8 classes of control and Down syndrome mice exposed to context fear conditioning, a task used to assess associative learning.  

The aim is to identify subsets of proteins that are discriminant between the classes. Basically, this is multi-class classification problem.

## Data Set Information:

[Dataset](https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression)

[xlsx file](https://archive.ics.uci.edu/ml/machine-learning-databases/00342/Data_Cortex_Nuclear.xls)

The data set consists of the expression levels of 77 proteins/protein modifications that produced detectable signals in the nuclear fraction of cortex. There are 38 control mice and 34 trisomy mice (Down syndrome), for a total of 72 mice. In the experiments, 15 measurements were registered of each protein per sample/mouse. Therefore, for control mice, there are 38x15, or 570 measurements, and for trisomy mice, there are 34x15, or 510 measurements. The dataset contains a total of 1080 measurements per protein. Each measurement can be considered as an independent sample/mouse.

The eight classes of mice are described based on features such as genotype, behaviour and treatment. According to genotype, mice can be control or trisomy. According to behaviour, some mice have been stimulated to learn (context-shock) and others have not (shock-context) and in order to assess the effect of the drug memantine in recovering the ability to learn in trisomy mice, some mice have been injected with the drug and others have not.

### Classes:
* c-CS-s: control mice, stimulated to learn, injected with saline (9 mice)
* c-CS-m: control mice, stimulated to learn, injected with memantine (10 mice)
* c-SC-s: control mice, not stimulated to learn, injected with saline (9 mice)
* c-SC-m: control mice, not stimulated to learn, injected with memantine (10 mice)
* t-CS-s: trisomy mice, stimulated to learn, injected with saline (7 mice)
* t-CS-m: trisomy mice, stimulated to learn, injected with memantine (9 mice)
* t-SC-s: trisomy mice, not stimulated to learn, injected with saline (9 mice)
* t-SC-m: trisomy mice, not stimulated to learn, injected with memantine (9 mice)

The aim is to identify subsets of proteins that are discriminant between the classes.


## Attribute Information:

1 Mouse ID
2..78 Values of expression levels of 77 proteins; the names of proteins are followed by â€œ_nâ€ indicating that they were measured in the nuclear fraction. For example: DYRK1A_n
79 Genotype: control (c) or trisomy (t)
80 Treatment type: memantine (m) or saline (s)
81 Behavior: context-shock (CS) or shock-context (SC)
82 Class: c-CS-s, c-CS-m, c-SC-s, c-SC-m, t-CS-s, t-CS-m, t-SC-s, t-SC-m

# Commands to run the model on local machine
## Creating a virtual environment for the model
```bash
conda create --prefix ./env python=3.7 -y
```
## Activating the virtual environment
```bash
conda activate ./env
```
## Installing the Required Libraries
```bash
pip install -r requirements.txt
```
## Testing the model on localhost
```bash
python predict.py
```

# Commands to build and run the model using Docker container
## Building the Docker image of the Model
```bash
docker image build -t mice .
```
## Running the docker container
```bash
docker run -p 5000:5000 -d mice
```
## Pushing the Docker container to DockerHub
```bash
docker tag mice rohandhanraj/mice

docker push rohandhanraj/mice
```
## [Docker Image](https://hub.docker.com/r/rohandhanraj/mice-protein-expression-prediction)

# Deployment
**Platform: [Heroku](https://mice-protein-expression.herokuapp.com/)**  
**Code Repo: [GitHub](https://github.com/rohandhanraj/mice-protein-expression)**
## Pushing Code to GitHub
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <repo URL>
git push -u origin main
```
## Deploying on Heroku
```bash
heroku login

heroku git:remote -a admn-predixn

git push heroku main
```

# Public Endpoint:
Check the application at: https://mice-protein-expression.herokuapp.com/
