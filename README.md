# **COVID19-Analysis-with-SQL**
## Introduction 
This dataset provides information about COVID-19 cases such as deaths, hospitalizations, and vaccinations across 
different locations and continents. We aim to provide insight and answer important questions about the pandemic as well 
as provide further exploratory and/or predictive analysis.

## Aim
Use flask to provide a user the ability to interact with COVID19 data that was managed with the use of SQL queries. 
The user will be able to go to a webpage and interact with flask, giving information between the web browser and flask 
such as inputs to filter with. The user then will interact with flask by clicking the "submit" button and Flask will 
then receive that request from the user and communicate with the MySQL server for that information by providing it with 
the query. The server will then provide raw information to flask which will then filter, manipulate, and format the data 
into HTML. Once completed the information is then sent back to the user.

<img src="https://img.shields.io/badge/language-Python-blue.svg" style="zoom:100%;" /> <img src="https://img.shields.io/badge/language-HTML-green.svg" style="zoom:100%;" /> <img src="https://img.shields.io/badge/language-CSS-orange.svg" style="zoom:100%;" /> <img src="https://img.shields.io/badge/language-FLASK-lightblue.svg" style="zoom:100%;" /> <img src="https://img.shields.io/badge/language-SQL-lightgrey.svg" style="zoom:100%;" />

## Workflow
This project uses [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow as 
the Git branching model.

![img_1.png](img_1.png)

**Develop and main branches**

This workflow uses two branches to record the history of the project. 
The main branch stores the official release history, and the develop branch serves as an integration branch for features. 

The first step is to complement the default main with a develop branch.
A simple way to do this is to create an empty develop branch locally and push it to the server:
> git branch develop\
> git push -u origin develop

This branch will contain the complete history of the project, whereas main will contain an abridged version. 
Other developers should now clone the central repository and create a tracking branch for develop. When the develop branch
is done it is merged into main.
[www.atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## Getting Started
### Clone COVID19-Analysis-with-SQL project
>cd destination\
>git clone https://github.com/albertjseo/COVID19-Analysis-with-SQL.git

### Check branch
You will want to be sure that you are in your 'dev' branch before proceeding. *If a 'dev' branch does not exist, 
you will need to create one.*
> git status (if status reads 'On branch dev' proceed to next)

If status reads On branch 'main' and a 'dev' branch does not exist, you will need to create it before switching.
> git switch -c dev

### Good coding practice
>* remember to create a new virtual environment (/venv)

### Required packages
You will need to use requirements.txt to install the required packages onto your local machine.
>pip install -r requirements.txt

### Updating required packages
>pip freeze > requirements.txt

## Flask App
Flask is a web framework that provides you with tools, libraries and technologies that allow you to build a 
web application. This web application can be some web pages, a blog, a wiki or go as big as a web-based calendar 
application 
or a commercial website.

Flask is part of the micro-framework category. Micro-frameworks are normally frameworks with little to no
dependencies of external libraries. This has pros and cons. Pros would be that the framework is light, there are little 
dependencies to update and watch for security bugs. Cons are that sometimes you will have to do more work by yourself or 
increase the list of dependencies by adding plugins yourself.

[Flask documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)

## HTML Templates
The template system, in combintation with "jinja2" provides the ability to integrate html and css with python.
