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

## Workflow
This project uses [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow as 
the Git branching model.

![img_2.png](img_2.png)

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

**Creating a feature branch**\

Without the git-flow extensions:
>git checkout develop\
>git checkout -b feature_branch

Continue your work and use Git like you normally would.

Finishing a feature branch
When you’re done with the development work on the feature, the next step is to merge the feature_branch into develop.

Without the git-flow extensions:
>git checkout develop\
>git merge feature_branch

**Release branches**\
Once develop has acquired enough features for a release (or a predetermined release date is approaching), you fork a release branch off of develop. Creating this branch starts the next release cycle, so no new features can be added after this point—only bug fixes, documentation generation, and other release-oriented tasks should go in this branch. Once it's ready to ship, the release branch gets merged into main and tagged with a version number. In addition, it should be merged back into develop, which may have progressed since the release was initiated.

Using a dedicated branch to prepare releases makes it possible for one team to polish the current release while another team continues working on features for the next release. It also creates well-defined phases of development (e.g., it's easy to say, “This week we're preparing for version 4.0,” and to actually see it in the structure of the repository).

Making release branches is another straightforward branching operation. Like feature branches, release branches are based on the develop branch.

Without the git-flow extensions:
>git checkout develop\
>git checkout -b release/0.1.0

Once the release is ready to ship, it will get merged it into main and develop, then the release branch will be deleted. It’s important to merge back into develop because critical updates may have been added to the release branch and they need to be accessible to new features. If your organization stresses code review, this would be an ideal place for a pull request.

To finish a release branch, use the following methods:
Without the git-flow extensions:
>git checkout main\
>git merge release/0.1.0

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