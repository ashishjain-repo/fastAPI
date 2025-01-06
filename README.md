# fastAPI

## Your First FastAPI App
To start writing FastAPI first we have to install FastAPI in our environment, and it can be done using this command `pip install fastapi`. Then we can create an app since our tutorial is focuisng on creating a storeapi we are going to create a folder and add two files init, first `__init__.py` and `main.py` main file will allow us to write the entry point of the application and init file will treat the folder as a package so we can import and call things from the folder.
Here is the code:
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello, world!"}
```
In this we are importing the package and then creating an instance of that package. After creating an instance we are create a decorator, and the decorator is to extend the functionallity of the function. And this decorator tell the fastAPI that when this request is made show the request on the given endpoint and the result will be based on the function init.

## Initial App Setup
Now we are going to setup the project to run the fastAPI application. First we are going to create a virtual environment for our application. To create the environment we are going to use this command: `python -m venv .venv` in this we are using .venv as the name of the virtual environemnt because usually directories startuing with a dot are associated with config files and are hidden. And to activate that virtual environemnt we can use this path and run the venv file in the main directory `.\venv\Scripts\activate` and for linux environemnt we can use this `source .venv/bin/activate`. Now since our virtual environment is setup now we are going to install dependencies. First we are going to create a requirement.txt file where we can mention all the dependencies and packages that our application will require. We are going to add two main packages for now which are `fastapi` and `uvicorn[standard]`. To install the packages in the ebnvironment we have to sinmle use this command: `pip install -r requirments.txt`. Now we are also going to create a new file whihc is going to be .gitignore file which we want git to ignore when we push the code through version control. Now we are going to put the following file extensions or path that git should ignore in that file:
```
.DS_Store
*.pyc
__pycache__
.env
*.db
.venv
.vscode/
*.png
```
Now to run the application we will be using this command: `uvicorn storeapi.main:app --reload` this command first is tageting the directory, then the file, and then the variable where we set the instance. We have also added the flag for reloading so whenever some new changes are added it will reload the server and show those changes, instead of manually restarting the server for new changes.

## Linting, Formatting, and Sorting imports