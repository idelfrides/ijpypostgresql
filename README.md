# ijpypostgresql API


## Project Information

This is an API created to work with postgreSQL DB in Python 3. It's a Python Package, an **API**  available to be used as a library/package on Python projects that need to handle data from  a postgreSQL DB.

The package  use **OOP** and four modules/files. All them has one Class with the same file name, the classes contain many methods used to build this app, exept process_data_form.py.
* ModulePostgreSQLdb.py - configuration module and connection to local server, creating and changing the structure of db and tables.
* HandleDataFromTerminal.py - Input data processing module via Run terminal.
* HelperModule.py - contain some auxiliar methods, wich used to help user understanding what is going on.
* Crud_oper.py  -  CRUD module (CREATE | READ | UPDATE | DELETE): responsible for indexing and manipulating records in tables. 
* process_data_form.py - module responsible for processing data from a HTML form, do not work yet.



## Execution information
 App name: ijpypostgresql
 
 Description: This project is mine one of monst important project. It'is a package to handle data on postgreSQL DB with python.
              
 @utor: Engineer Idelfrides Jorge
 
 Date started: aug. 3td, 2019
 
 Date finished: aug. 8th, 2019
 
 License: on the README.md file
 


 ## Technical Information   
 Python Interpreter:
 
   --> Python 3.6.2
   
  --> Path on windows: C:\Users\user_name\AppData\Local\Programs\Python\Python36\python.exe

 Python driver for PostgreSQL database:
 
   --> Psycopg2 v2.8.3
      
 -- Coding: UTF-8 --
 
 content-type: script/python; utf-8
 
 ## HOW TO USE: Steps to use this package
 Follow next steps to use this package in your python project or to make a simple test and learn more.
 
 ### Step 1:
Download **ijpypostgresql** and unpack the folder. Move package into your  python project.

 ### Step 2:
Read the file LEIAME fully, or for other way, you can do it here on github repository.
After that, take a look to understand project structure, to understand mostly, the fields of the table.
So, in this point, you may make some changes on it or create your own DB/table to use.

 ### Step 3:
If you want, you can make some modifications to the package. If not, so you just need to use it like I am goint to tell you next.
Create a python file  to be a main one. Create a method inside that file.This goint to be, therefore the main method of your python project. After that follow next steps. 

 ### Step 4:
Import modules inside **ijpypostgresql** and python time module you gonna use in your project like this.
* Example: from ijpyposgresql import ModulePostgreSQLdb as mdb
* Example: import time as t.

 ### Step 5:
Inside the main method you have to create an object of module you goint to need imediatily or for all modules, (I recomend the first way). Take a look a real example.
* Example: mdbo = mdb.ModulePostgreSQLdb() 

 ### Step 6:
  Call the method to set up a conection to local server
   * Example: conec, cursor = mdbo.connect2db()

    # ----------------------------------------------
    #  connect2db()
    # -----
    # This method set up aconection to the localhost 
    # (local server), with na 'database' created. 
    # It need to set a DB.  This method is only 
    # called on your main module/file, the is same 
    # used to test the 'ijpymyql' package.
    # Teturn 'conection' with db and 'cursor'
    # to execute quireis.
    # ----------------------------------------------

 ### Step 7:
  Verify database existence. Make sure that db was successfuly created. For that, call method  verification(cursor, 'db').
   * Example: resp = mdbo.verification(cursor, 'db')
   
    # ----------------------------------------------
    #  verification(cursor, entity)
    # -----
    # This method verify if the entity (string 'db' or table, 'tb') is realy
    # exists in the local server.
    # It return 1 if the entity exists or
    # 0 if not exists.
    # ----------------------------------------------
    
 If resp is 0, you gonna need to create a new database. To do that, call method  create_db(self, cursor, db) like next.
   * Example: mdbo.create_db(cursor, mdbo.appdb)
   
    # ----------------------------------------------
    #  create_db(cursor, mdbo.appdb)
    # ---------
    # This method create a DB to be used on
    # your module. The db is define by you/user as
    # an attribute of ModuleMySQLdb module 
    # (see the module in package).
    # ----------------------------------------------
   
    Then, you should call verifiction method again.
    
 ### Step 8:
   Activate a db to be used in your app. For that, call  method  mdbo.activate_db(cursor).
   * Example: mdbo.activate_db(cursor).
   
   
    # ----------------------------------------------
    #  activate_db(cursor, mdbo.appdb)
    # --------
    # This method activate the DB to be used to test
    # this package.
    # ----------------------------------------------
    
    
 ### Step 9:
   Now, call the verification method to make sure that some table exists.
   * Example: resp = mdbo.verification(cursor, 'tb')
     
    # ----------------------------------------------
    #  verification(cursor, entity)
    # --------
    # This is the same method described at Step 7.
    # ----------------------------------------------
  
 If resp is 0, you gonna need to create a new table. To do that, call method create_table(self,  cur, mytb) like next.
   * Example: mdbo.create_table(cursor, mdbo.dev_table)
   
 
 ### Step 10:
   Finaly, you must  alter table to drop some attribute then add others. To make this right, call method alter_table(self, cur, mytb, oper, atrib).
   * Example: mdbo.alter_table(cursor, mdbo.dev_table, 'drop', 'age')
   
    
    # ------------------------------------------------------
    #  alter_table(cursor, mdbo.dev_table, 'drop', 'age')
    # -------------
    # This method alter a table present on DB.
    # The method provide 3 operations: add, drop
    # and modify. The table and operation are
    # defined by you/user as an attribute (tables)
    # of ModuleMySQLdb module (see the module in package).
    # ------------------------------------------------------
   
   Run alter table method to alter two attributes: age and gender as follows:
   
    # ----------------------------------
    # drop: age | gender
    # ----------------------------------
    mdbo.alter_table(cursor, mdbo.dev_table, 'drop', 'age')
    mdbo.alter_table(cursor, mdbo.dev_table, 'drop', 'gender')

    # ----------------------------------
    # add: funcao(role) | adress
    # ----------------------------------
    mdbo.alter_table(cursor, mdbo.dev_table, 'add', 'role')
    mdbo.alter_table(cursor, mdbo.dev_table, 'add', 'adress')

 After these steps, you are now free to play with the package like you want.
 
 ### Contributions
 
Maybe WE (me and you) can build the best **Python package for handle data on postgreSQL DB**  to help other pythpn developers emprove their job. So feel free to start a chat or send pull requests.
 
 
 ----
 
 @uthor: IDELFRIDES JORGE | Mail me by idelfridesjorgepapai@gmail.com

 FOLLOW ME ON GITHUB: ENG. [IDELFRIDES JORGE](https://github.com/idelfrides/) 
