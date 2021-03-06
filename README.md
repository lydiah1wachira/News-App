# News-App


## By Lydiah Wachira

## Description

News App is a web appliction that displays a list of news sources from around the world. A user is able to click on a news source and view an abreviated version of the particular news article. Clicking on the news article will then redirect you to the news article's web page.

With the application, a user will be able to:

* See various news sources and select the ones they prefer.
* See all news sources from the source they selected.
* See Image description and time the news article was created.
* Click on an article and read it fully from the news source


### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.6
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual machine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3<your python version> manage.py server
```
* Run ```chmod +x start.sh``` followed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.


## Technologies Used

* Python v3.8
* Bootstrap
* Flask
