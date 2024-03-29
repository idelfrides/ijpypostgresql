#!/usr/bin/python

"""
------------------------------------------------------
   ====  PACKAGE INFORMATION  ====
 App name: ijpypostgresql
 Version: 1.0.0
 Description: module to handle data from postgreSQL
              DB with python 3.x
 @utor: Engineer Idelfrides Jorge
 Date started: aug. 3rd, 2019
 Date finished: aug. 8th, 2019
 License: on the README.md file
 Email: idelfridesjorgepapai@gmail.com
 GitHub: @idelfrides(https:\\github.com/idelfrides/)
 ------------------------------------------------------
   ====  TECHNICAL INFORMATION  ====
 Python Interpreter:
 --> Python 3.6.2

Python driver for postgreSQL database:
   --> psycopg2 v2.8.3
   -*- Coding: UTF-8 -*-
 connectiontent-type: script/python; utf-8
 ------------------------------------------------------
"""

# --------------------------------------------------
# importing my owm modules
# --------------------------------------------------
from HelperModule import HelperModule

# --------------------------------------------------
# importing the python module
# --------------------------------------------------

import psycopg2   # postgresql db driver for python
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class ModulePostgreSQLdb(object):
    """
       ---------------------------------------------------
          ====  OPERATIONAL INFORMATION  =====
         This module will be my library for python
         appications working with postgreSQL DB.
         The module will create all method needed to
         manage a db app and more other methods.
       ---------------------------------------------------
    """

    # create an o=instance of HelperModule module
    hmo = HelperModule()


    # ----------------------------------------------
    # set db and all tables name bere to better
    # connectiontrole this app.
    # --------------------------------------------

    def __init__(self, conn_params):
        """
           -------------------------------------------------
            The thunder init method inicialize and show
            the module information to user via terminal by
            calling method 'app_info()'
           --------------------------------------------------

           :type self: auto reference parameter
           :rtype: None
        """

        # self.hmo.app_info()
        self.host = conn_params['host']     # 127.0.0.1 | localhost
        self.database = conn_params['database']
        self.user = conn_params['user']
        self.password = conn_params['password']
        self.port = conn_params['port']


    def connect2db(self):
        """
           ------------------------------------------------------
             This method set connection to the local server,
             with a 'database' created. It need to set a DB.
             This method is only called on your main module,
             the same used to test the 'ijpypostgresql' package.
             Return  'connection' with db and 'cursor'
             to execute quereis.
           ------------------------------------------------------
           :type self: auto reference parameter
           :rtype: connection with postgre | cursor of that connection
        """

        ''' connectionnect to the postgreSQL database server '''
        connectionn = None
        cursor = None
        try:

            connectionn = psycopg2.connectionnect(
                host=self.host,
                port = self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )

            connectionn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor = connectionn.cursor()
            prop = connectionn.get_dsn_parameters()
            print('\n PostgresSQL connectionnecion proprieties \n {}'.format(prop) )

            cursor.execute('SELECT version()')
            version = cursor.fetchone()
            print('\n You are connectionnected to server \n {}'.format(version))
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error while tring to connectionnect to POSTGRESQL DB: {}. \n Server reponse: {}'.format('test', error))
        finally:
            if connectionn is not None:
                print('\n connection setted up successfuly \n')

        return connectionn, cursor


    def create_db(self, cursor, db_name):
        """
           -------------------------------------------------
             This method create a DB to be used on
             this package. The db is define by you/user as
             an attribute of this module(see on the to).
           -------------------------------------------------


           :type cursor: cursor of postgreSQL connection
           :type db: database name to be created
           :rtype: None
        """

        try:
            sql = "CREATE DATABASE IF NOT EXISTS " + db_name
            cursor.execute(sql)
            print(f"\n Database {db_name} created successfully. \n ")
        except Exception as err:
            print(f'Error by try to CREATE DB: {db_name}. \n Server reponse: {err}')



    def activate_db(self, connectionn, cursor, db):
        """
           -------------------------------------------------
            This method activate the DB to be used to test
            this package.
           -------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type db: data base name to be created
           :rtype: None
        """

        try:
            connectionn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            sql_use = "USE " + db
            cursor.execute(sql_use)
            print('\n Database {} activated successfuly'.format(db))
        except Exception as error:
            print('\n Error try to activate DB {}. \n Server said: {}'.format(db, error))



    def create_table_player(self, cursor, mytb):
        """
           --------------------------------------------------
            This method create a table to the DB and be
            used on this package. Al tables is defined by
            you/user like  an attribute of this
            module(see on the to).
           --------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type mydb: database name where a table will be created
           :rtype: None
        """

        # cursor_connectionec = self.set_connectionec_with_db()
        sql_create = "CREATE TABLE IF NOT EXISTS " + mytb
        fields = " (id BIGSERIAL NOT NULL PRIMARY KEY, " \
                   " name VARCHAR(255)," \
                   " money INT," \
                   " position VARCHAR(255))"

        full_sql = sql_create +  fields

        try:
            cursor.execute(full_sql)
            print(f"\n Table {mytb} created successfully. \n ")
        except Exception as erro:
            print(f'\nError by try to create the table: {mytb}. \n Server reponse: {erro}')



    def create_table_property(self, mytb):
        """
           --------------------------------------------------
            This method create a table to the DB and be
            used on this package. Al tables is defined by
            you/user like  an attribute of this
            module(see on the to).
           --------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type mydb: database name where a table will be created
           :rtype: None
        """

        try:
            sql_use = "USE " + db
            cursor.execute(sql_use)
            print('\n Database {} activated successfuly'.format(db))
        except Exception as error:
            print('\n Error try to activate DB {}. \n Server said: {}'.format(db, error))



    def create_table(self, cursor, mytb):
        """
           --------------------------------------------------
            This method create a table to the DB and be
            used on this package. Al tables is defined by
            you/user like  an attribute of this
            module(see on the to).
           --------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type mydb: database name where a table will be created
           :rtype: None
        """

        # cursor_connectionec = self.set_connectionec_with_db()
        sql_create = "CREATE TABLE IF NOT EXISTS " + mytb
        myfields = " (id BIGSERIAL NOT NULL PRIMARY KEY, " \
                   " name VARCHAR(255)," \
                   " gender VARCHAR(50)," \
                   " company VARCHAR(255), " \
                   " age INT, " \
                   " salary NUMERIC(7, 2))"

        full_sql = sql_create +  myfields

        try:
            cursor.execute(full_sql)
            print(f"\n Table {mytb} created successfully. \n ")
        except Exception as erro:
            print(f'\n Error by try to create the table: {mytb}. \n Server reponse: {erro}')



    def alter_table(self, cursor, mytb, oper, atrib):
        """
           -------------------------------------------------
             This method alter a table present on DB.
             The method provide 3 operations: add, drop
             and modify. The tables and operation are
             defined by you/user like an attribute(tables)
             of this module(see on the to).
           -------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type mydb: database name, witch connectiontain the
                       table that the attibute gonna be altered
           :type oper: the operation to be perform over the attribute atrib
           :type atrib: attibute will be altered
           :rtype: None
        """

        # cursor = self.set_connectionec_with_db()
        if oper == 'add':
            sql_1 = " ALTER TABLE " + mytb
            newattri = " ADD COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + newattri
            print(sql)
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper == 'drop':
            sql_1 = "ALTER TABLE " + mytb
            drop_attri = " DROP COLUMN " + atrib
            sql = sql_1 + drop_attri
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        elif oper == 'mod':
            sql_1 = "ALTER TABLE " + mytb
            mod_attri = " MODIFY COLUMN " + atrib + " VARCHAR(255)"
            sql = sql_1 + mod_attri
            try:
                cursor.execute(sql)
                print("\n Table {} altered successfully. \n ".format(mytb))
            except Exception as erro:
                print('\n Error by try to alter the table: {}. \n Server reponse: {}'.format(mytb, erro))
        else:
            pass



    def drop_struct(self, connection, cursor, code, entity):
        """
        ---------------------------------------------------------
            This method DROP a db/table exists.
            The method has 3 parameters: cursor of connectionection,
            code of struct and the name(entity) of the same.
        ---------------------------------------------------------

           :type connection: connection with postgreSQL DB
           :type cursor: cursor of postgreSQL connection
           :type code: code of struct. Can be database (db) or table (tb)
           :type entity: name of the structure defined by code parameter.
           :rtype: None
        """

        # cursor = self.set_connectionec_with_db()
        op = self.hmo.info_danger(code, entity)
        if code == 'db':
            if op == 1:   # drop
                sql = " DROP DATABASE IF EXISTS " + entity
                try:
                    cursor.execute(sql)
                    # connection.comit()
                    print("\n Database {}  was droped  successfully. \n ".format(entity))
                except Exception as erro:
                    print('\n Error try to DROP the Database: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:   # operation aborted
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
        elif code == 'tb':
            if op == 1:
                # sql = " DROP TABLE IF EXISTS " + entity
                sql = " DROP TABLE " + entity
                try:
                    cursor.execute(sql)
                    # connection.comit()
                    print("\n Table {} was droped successfully. \n ".format(entity))
                except Exception as erro:
                    print('\n Error try to DROP the table: {}. \n Server reponse: {}'.format(entity, erro))
            elif op == 0:
                print('\n YOU CHOSE TO QUIT \n INTELIGENT DECISION.')
            else:
                pass
        else:
            pass


    def truncate(self, connection, cursor, mytb):
        """
           --------------------------------------------------
             This method TRUNCATE a table presents on DB.
             The method has 3 parameters: connection, cursor
             and the table that going to be truncated.
          --------------------------------------------------

           :type connection: connection with postgreSQL DB
           :type cursor: cursor of postgreSQL connection
           :type mydb: database name, witch connectiontain the
                       table that the attibute gonna be truncated
           :rtype; None
        """

        try:
            sql = " TRUNCATE TABLE " + mytb
            cursor.execute(sql)
            # connection.comit()
            print("\n Table {} TRUNCATED successfully. \n ".format(mytb))
        except Exception as error:
            print('\n Error by try to TRUNCATE the table: {}. \n Server reponse: {}'.format(mytb, error))



    def entity_verify(self, cursor, entity):
        """
            -----------------------------------------------------
              This method make a verification of a struct: db
              or table presents on DB.
              The method show(via run terminal) all db existis
              on the localhost or all tables on a specific db.
            ------------------------------------------------------

            :type cursor: cursor of postgreSQL connection
            :type entity: name of the structure: db or tb.
            :rtype: None
        """

        if entity == 'db':
            print('\n VERIFY DB')
            try:
                cursor.execute("SHOW DATABASES")
                for db in cursor:
                    print('\n tipo: ', type(db))
                    print(' {}'.format(db))
            except Exception as error:
                print('Error by try to show all DB. \n Server said: {}'.format(error))
        elif entity == 'tb':
            print('\n VERIFY TB')
            try:
                cursor.execute("SHOW TABLES")
                for tb in cursor:
                    print('\n tipo: ', type(tb))
                    print(' {}'.format(tb))
            except Exception as error:
                print('Error by try to show all tables. \n Server said: {}'.format(error))
        else:
            pass


    def unique_constraint(self, cursor, attr, table, oper):
        """
           ------------------------------------------------------
             This method alter a table present on DB to make
             an attr as UNIQUE. It provide 2 operations: Add | Drop
             The table, operation and attribute
             are defined by you/user as arguments of method.
           ------------------------------------------------------

           :type cursor: cursor of postgreSQL connection
           :type attr: attibute to make unique
           :type cursor: cursor of postgreSQL connection
           :type attr: attibute to make unique
           :type table: the table that connectiontain the attribute
           :type oper: the operations to be perform
           :rtype: None
        """

        unique_connectionst_name = table + '_' + attr + '_' + 'key'

        if oper == 'add':
            print('\n ADDING ATTR {} AS UNIQUE IN TABLE {}'.format(attr, table))
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' ADD connectionSTRAINT ' + unique_connectionst_name + ' UNIQUE(attr)'
                sql = sql_1 + sql_2
                cursor.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to MAKE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        elif oper == 'drop':
            print('\n DROPPING UNIQUE connectionSTRAINT FROM ATTR {} IN TABLE {}'.format(attr, table))
            try:
                sql_1 = " ALTER TABLE " + table
                sql_2 = ' DROP connectionSTRAINT ' + unique_connectionst_name
                sql = sql_1 + sql_2
                cursor.execute(sql)
                print('\n Operation done SUCCESSFULY')
            except Exception as error:
                print('Error by tring to REMOVE {} as UNIQUE. \n\n Server said: {}'.format(attr, error))
        else:
            pass


    def close_pg_connection(self, connection, cursor):
        """
           ---------------------------------------------------
             This method close the connection with mySQL
             server. The connectionn only or cursor only or both them
           ---------------------------------------------------

           :type connection: connection with postgreSQL DB
           :type cursor: cursor of postgreSQL connection
           :rtype: None
        """

        try:
            cursor.close()
            connection.close()
            print('\n PostgreSQL connection is closed successfuly \n')
        except Exception as error:
            print('Error by tring to CLOSE the connection with PostgreSQL server {}. \n\n Server said: {}'.format(connection, error))
