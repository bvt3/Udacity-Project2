[![Github Actions](https://github.com/bvt3/Udacity-Project2/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/bvt3/Udacity-Project2/actions/workflows/pythonapp.yml)
[![Build Status](https://dev.azure.com/udacitytest/Flask-ML-Deploy/_apis/build/status%2Fbvt3.Udacity-Project2?branchName=main)](https://dev.azure.com/udacitytest/Flask-ML-Deploy/_build/latest?definitionId=5&branchName=main)

# Overview

The project is all about deploying and running a machine learning app that predicts the housing price in Boston.
It is kept under a public GitHub repository that can be cloned and inspected from the portal itself or by cloning it from a local development machine.
The app is running on Python version 3.9.

## Project Plan

* [Trello board](https://trello.com/b/vmQ218hf/udacity-project2) for the project
* [Project plan spreadsheet](https://docs.google.com/spreadsheets/d/1apMKKebAqOvSA9z8hcqIV6f1Bb2gQdo4qqU8FKp7uVo/edit?usp=sharing)

## Instructions

Architectural Diagram

![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/Architectural_Diagram.jpg?raw=true)

1. User initiate the change either from GitHub portal or via local repository.
2. Once the change has been pushed, GitHub workflow will run and at the same time Azure Build Pipeline will run.
3. Azure Pipeline will run necessary step to deploy it to Azure App Service.
4. The app is up and running and we can use the service it provides.

The main GitHub project is https://github.com/bvt3/Udacity-Project2

Steps to run the prediction app

1. Open portal.azure.com from your web browser and login

2. Click Cloud Shell icon from the menu (BASH)
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-01.jpg?raw=true)
3. Create a virtual environment using the command:
```bash
python3 -m venv ~/.myrepo
```
4. Activate the virtual environment:
```bash
source ~/.myrepo/bin/activate
```
5. Clone the repository using https, example:
```bash
git clone https://github.com/bvt3/Udacity-Project2.git
```
* You can get the https link from the GitHub project:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-02.jpg?raw=true)
* Sample cloned repository:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-03.jpg?raw=true)

6. Go to the root directory of the repository:
```bash
cd Udacity-Project2/
```
7. Run the makefile command:
```bash
make all
```
* Sample output of a make file command:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-04.jpg?raw=true)
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-05.jpg?raw=true)

8. Make the prediction by running the make_predict_azure_app.sh file
* Unblock the file first:
```bash
chmod u+x make_predict_azure_app.sh
```
* Then, run it:
```bash
./make_predict_azure_app.sh
```
* Output of a prediction:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-06.jpg?raw=true)

Steps to run a load testing for the application using Locust

1. Install Locust
```bash
pip3 install locust
```
2. Run a locust test; The command below runs the test with 10 users with a spawn-rate of 1 user per second
```bash
locust -f locustfile.py --headless -u 10 -r 1 --run-time 10
```
* Sample output:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-07.jpg?raw=true)
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-08.jpg?raw=true)


Sample Images:
* The resource group UdacityProject2 where the resources have been created:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-09.jpg?raw=true)

* The benprj2 app service:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-10.jpg?raw=true)

* The landing page of the service:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-11.jpg?raw=true)

* The GitHub action:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-12.jpg?raw=true)

* The Azure build pipeline inside DevOps:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-13.jpg?raw=true)

* The Log Stream for monitoring:
![alt text](https://github.com/bvt3/Udacity-Project2/blob/main/Files/CICD-14.jpg?raw=true)

## Enhancements

- Add an alert after the deployment
- UI enhancement to have a user-friendly experience
- Make the training model user configurable in the future so it is not hard-coded
- Leverage containerization or micro-services

## Demo 

[Demo Video](https://youtu.be/IyuV5pDDIiI)