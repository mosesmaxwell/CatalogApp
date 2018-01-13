# Catalog App
----------------
The Catalog App consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

# Steps to Run:
----------------
1. Clone the project from https://github.com/mosesmaxwell/CatalogApp.git

2. Launch the Vagrant VM from inside the *vagrant* folder with:

``` vagrant up```

3. Then access the shell with:

``` vagrant ssh```

4. Then move inside the catalog folder:

`cd /vagrant/catalog`

5. Then run the database configuration using below command (to load with default values):

`python loaddata.py`

6. Then run the application:

`python catalogapp.py`

7. After the last command you are able to browse the application at this URL:

`http://localhost:5000/`