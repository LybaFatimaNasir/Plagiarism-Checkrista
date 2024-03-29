# 🔎🧾 PLAGIARISM CHECKERSITA

##                                                      Django:

![alt text](https://static.djangoproject.com/img/logos/django-logo-negative.png) 

Our Project named as "Plagiarism Checkrista" is a plagiarism checking tool. It is built in Django. It takes input in the form of text and checks it with other documents available in database resulting in providing the plagiarised content.

## 🛠 TOOLS

For this project to run you need to have 
- 📋 An editor **Vs Code** or it can be any Python IDE like **PyCharm** or **Atom**.
- 🐍Python installed. 
- 🚀Django installed in virtual environment.
- 💻And a command line for windows Command Prompt and for MacOs linux, built in terminal.

  👇 Don't worry if you don't have any of these installed let's see the installation section first to install these.
  
##  🎩 INSTALLATION

1. For Installing Python [Phyton installation](https://www.python.org/downloads/) it will download latest version of python on your OS.
2. For Django first we need to create virtual environment but before this we need to clone this repo to your local computer.

##  🏗 SETUP

1. Clone the code 
2. Open Command Prompt and move to folder where Project is being cloned.
3. Now creating virtual environment close to the project folder for this case **CS311S20PID02 >> Checkrista** *if your local computer does not contain .env first perform **step4** to check whether virtual environment already exists or not because it is dependent on the machine otherwise start with this step by first creating virtual environment.* 

![Github image](/images/.env.PNG)
 
 This ``py -m venv .env`` create virtual environment .env is the folder containing virtual environment you can name it as you want Here the Project folder is used to just demonstrate how to install django Use  your own folder location .
 
 4. Activating virtual environment where our **Django** will be installed.
 
 ![Github image](/images/activating.env.PNG)
 
 The ``\.env>Scripts\activate.bat`` will activate the virtual environment ``(.env) `` this before whole path shows we are in the virtual environment.
 
 5. Now installing Django 
 
 ![Github image](/images/djangoInstallation.PNG)
 
 The ``py -m pip install django`` has installed the django in the virtual environment.
 
 If needeed pip to be upgraded so that the latest version be used we need to
 
 ![Github image](/images/pipUpgradation.PNG)
 
 The ``python -m pip install --upgrade pip`` will upgrade version in your virtual environment.
 
 6. Now we are focused on running the server so that we can use the application
  - First exit command line and reopen it then move to the folder **checkrista** and again activate the virtual environment  
  
  ![Github image](/images/activation.PNG)
  
   and then move where **manage.py** file resides in our case **checker** 
   
   ![Github image](images/checker.PNG)
   
   There is a django package **sentry-sdk** I installed because this is a must-have tool for any Django project as it’s key that we stay informed about all the code-based issues in the application. But it is supposed to be downloaded on your system too using ``$ pip install --upgrade sentry-sdk`` its configuration is already added.

   
   Now run the server 
   
   ![Github images](/images/runningServer.PNG)
   
   The ``python manage.py runserver`` will run server
   
   7. Copy the url as shown above and paste it in the chrome and write it as follow
   
   ![Github Image](/images/urlCopied.PNG)
   
   write it as ``http://127.0.0.1:8000/tool/`` to make the url run 
   
   8. The following page will be displayed
   
   ![Github image](/images/page1.PNG)
   
   Write your text in the box given.
   and click on the ViewResult to display the result page as follow
   
   ![Github image](/images/resultPage.PNG)
   
   
   >Note: All the django installations are done in the virtual environment locally just fir the project not on the entire system globally   and  If you ran into some while running server want to run again first **CTrL+C** to break through the previous one then again run the server as explained above .
   
## 🖥 Environment

|**Sr.no** |**Softwares/IDEs** |**Version** |**Reason**|
----------|--------------|------------|----------
|1.        |Windows       | 10.0.18363 |Default OS on laptop|
|2.        |Vs Code       | 1.47.3     |Vs Code is very easy to use|
|3.        |PyCharm       | 192.6817.19|PyCharm is the best editor for python programs.|
|4.        |db.sqllite3   |  3.28.0    |lightweight database server comes built in with the django installation|



|**Sr.no** |**Languages/Framework/Modules** |**Version** |**Reason**|
----------|--------------|------------|----------
|1.        |Python3       | 3.8.2      |Python is considered a very easy yet very powerful programming language.|
|2.        |Django       | 3.0.8     |Django the open source web framework 100% written in python. Provides many facilities in the development process.|
|3.        |Pip    |    20.2.1    |   The Package manager, Most of the python distributions comes with pip installled    |

 
 
  
 ## 🔑 LICENSE
 
 
 MIT
