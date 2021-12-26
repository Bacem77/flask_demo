# About 
This project is a full CI CD dockerized flask application.

This application is deployed on heroku servers here is the link : https://flask-demo-cicd.herokuapp.com/ .

The CI CD platforme used in this project is `GitHub Actions`

# The jobs of the CI CD cycle

1. Testing : Running unit tests using **Pytest**
2. Building + Dockerizing 
3. Deploying : The app is deployed on heroku using `akhileshns/heroku-deploy` action.

These jobs are executed sequentially.

# How to run this app 
You can clone the repository and install the necessary dependencies by following these steps:

1. Creating a virtual enviroment :
`python -m venv env`.
2. Activate and install the dependencies :
`pip install -r requirements.txt`.
3. Run the app app.py:
`flask run`.

As simple as that !!!