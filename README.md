# cent-cloud-security

#### This project contains two parts of coding

* **Store Folder**
  * Static Theme files (like HTML, CSS, JS)
  * This part is running on shopify Sass Platform
  * Basically you could ignore this coding part, since you can see and play everything on https://the-market-group-project-demo-store.myshopify.com/  with access code **Pa$$w0rd**
  
- - -
* **HRmanagement Folder**
  * A python Django app
  * Provides a simple employee management feature like 
      * Adding a new employee
      * Editing a existed employee profile
      * Deleting a left employee record
      * Logging Employee operations
      * Changing employee permissions

#### How to set up and run HRmanagement on your local

1. install [python 3.7 +](https://www.python.org/) 
2. install [pipenv](https://github.com/pypa/pipenv) - a virtual environment tool
3. download or git clone this project repository
4. Open your terminal and follow the listed commands below:
```bash
$ cd HRmanagement/ # change into python root folder
$ pipenv shell # start python virtual environment, and please make sure you are running on python 3.7+ 
$ pipenv install -r requirements.txt # install dependencies
$ cd theMarketGroup/ # change into the project app folder
$ python manage.py makemigration # prepare for user model init
$ python manage.py migrate # import customized user / admin table into database
$ python manage.py createsuperuser # create a admin user
$ python manage.py runserver # Run the app
```
5. Open your Browser and go to localhost http://localhost:8000/xadmin/  and log in the system with your super user credential
