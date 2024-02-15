# **COVID19-Analysis-with-SQL**
## Introduction
This project focuses on analyzing data related to the COVID-19 pandemic using SQL queries. This dataset provides information about COVID-19 cases such as deaths, hospitalizations, and vaccinations across different locations and continents. We aim to provide insight and answer important questions about the pandemic as well as provide further exploratory and/or predictive analysis.

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

Flask documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application.

## HTML Templates
The template system provides some HTML syntax which are placeholders for variables and expressions that are replaced by 
their actual values when the template is rendered. 