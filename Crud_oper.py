# ----------------------------------------
#   importing modules
# ----------------------------------------
from ijpypostgresql import ModulePostgreSQLdb as mdb
from ijpypostgresql import HelperModule as hm


# --------------------------------------------
# CRUD class(module) - contain all methods
# to build a CRUD features
#---------------------------------------------
class Crud_oper(object):
    # ----------------------------------------
    # create an object of module ModuleMySQLdb()
    # ----------------------------------------
    mdbo = mdb.ModulePostgreSQLdb()
    hmo = hm.HelperModule()

    # ----------------------------------------------
    # the thunder init method inicialize and show
    # the module information to user via terminal by
    # calling method 'module_info()'
    # ----------------------------------------------
    def __init__(self):
        self.hmo.module_crud_info()

    # ----------------------------------------
    # CREATE one record on the table.
    # It INSERT one dev to the table
    # ----------------------------------------
    def create(self, con, cur, mytb, data):
        try:
            sql = "INSERT INTO " + mytb + "(name, company, salary, role, adress) VALUES (%s, %s, %s, %s, %s)"
            myvalues = (data[0], data[1], data[2], data[3], data[4])
           #  print("\n eu sou data: {}".format(data))
            # print("\n eu sou val: {}".format(myvalues))
            cur.execute(sql, myvalues)
            con.commit()
            print(" {} Dev inserted. \n Dev ID: {}".format(cur.rowcount, cur.lastrowid))
        except Exception as erro:
            print('\n Error try to INSERT INTO the table: {}. \n Server reponse: {}'.format(mytb, erro))

    # ------------------------------------------
    # CREATE many records on the table.
    # It INSERT a number of devs to the table.
    # The number mushnbe greater than 1
    # and it is defined by user.
    # ------------------------------------------
    def create_many(self, con, cur, mytb, list_data):
        try:
            i = 0
            j = 5
            loop = True
            mylist_values = list()
            n = list_data.__len__()
            while loop is True:
                data_dev = list_data[i:j]
                tuple_data_dev = tuple(data_dev)  # transforme the list data_dev to a tuple
                mylist_values.append(tuple_data_dev)
                i = j
                j = j + 5
                if i is n:
                    loop = False
                else:
                    pass

            sql = "INSERT INTO " + mytb + "(name, company, salary, role, adress) VALUES (%s, %s, %s, %s, %s)"
            cur.executemany(sql, mylist_values)
            con.commit()
            print(" {} Dev inserted.".format(cur.rowcount))
        except Exception as error:
            print('\n Error try to INSERT INTO the table: {}. \n Server reponse: {}'.format(mytb, error))


    # ------------------------------------------
    # READ one record from the table.
    # It SELECT all records, than converter the
    # result set to a list of tuples. And than
    # get FIRT dev(tuple) of list.
    # ------------------------------------------
    def read_one(self, cur, mytb):
        print('\n I AM GONNA READ ONE \n')
        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            myresult = cur.fetchone()
            print('\n The first row {}'.format(myresult))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))

    # ------------------------------------------
    # READ all records from the table.
    # It SELECT all devs recorded on the table.
    # ------------------------------------------
    # TODO: do not working. i don´t know why.
    def read_all(self, cur, mytb):
        # fetch -> buscar | fetches -> busca
        # fetchall() -> busca todas as linhas do conjunto de resultado de consulta sql
        # e retorna uma lista de tuplas. Caso o  result set for null,
        # fetchall/fetchone/fetchmany  retorna uma lista vazia
        # executemany(sql, val)

        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            results = cur.fetchall()
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))

    # --------------------------------------------
    # READ one record from the table.
    # It SELECT one specific record from table
    # by using the clause WHERE. It use filter
    # by 'name' of dev informed by user.
    # --------------------------------------------
    def read_one_filter(self, cur, mytb, dev_name):
        print('\n READ ONE: {} \n'.format(dev_name))
        try:
            sql = "SELECT * FROM " + mytb + " WHERE name = %s"
            atrib = (dev_name)
            cur.execute(sql, atrib)
            myresult = cur.fetchone()
            print('\n The first row {}'.format(myresult))
        except Exception as error:
            print('\n Error try to SELECT FROM  table: {}. \n Server reponse: {}'.format(mytb, error))


    # ------------------------------------------
    # READ one record from the table.
    # It SELECT some specific attibutes for all
    # developer, all record from table
    # The attibutes are informed by user.
    # ------------------------------------------
    def read_some_attr(self, cur, mytb, atr1, atr2):
        print('\n I AM GONNA READ SOME \n')
        try:
            sql = " SELECT " + atr1 + "," + atr2 + " FROM " + mytb
            cur.execute(sql)
            results = cur.fetchall()
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM table: {}. \n Server reponse: {}'.format(mytb, error))


    # ---------------------------------------------
    # READ one record from the table.
    # It SELECT all attributes for some developer
    # The quantity of record to be shown is
    # informed by user.
    # ---------------------------------------------
    def read_some_dev(self, cur, mytb, num_dev):
        print('\n I AM GOING TO READ SOME \n')
        try:
            sql = "SELECT * FROM " + mytb
            cur.execute(sql)
            results = cur.fetchmany(size=num_dev)
            for x in results:
                print('\n {}'.format(x))
        except Exception as error:
            print('\n Error try to SELECT FROM table: {}. \n Server reponse: {}'.format(mytb, error))

    # ------------------------------------------------
    # UPDATE one atribute of a record. The method
    # takes six(6) arguments. conection | cursor |
    # table | attribute (column) | new value | id of
    # tuple(record)
    # ------------------------------------------------
    def update(self, con, cur, mytb, atr, new_value, myid):
        try:
            sql = "UPDATE " + mytb + " SET " + atr + " = %s  WHERE id = %s"
            val = (new_value, myid)
            cur.execute(sql, val)
            con.commit()
            print('\n Lines affected {}'.format(cur.rowcount))
        except Exception as error:
            print('\n Error try to UPDATE table: {}. \n Server reponse: {}'.format(mytb, error))

    # ------------------------------------------------
    # DALETE one record(tuple) of table.
    # It takes four(4) arguments. conection | cursor |
    # table (column) | id of tuple(record)
    # ------------------------------------------------
    def delete(self,  con, cur, mytb, thename):
        try:
            sql = " DELETE FROM " + mytb + " WHERE name = %s"
            val = (thename)
            cur.execute(sql, val)
            con.commit()
            print('\n Record deleted: {}'.format(cur.rowcount))
            self.restart_pk(con, cur, mytb)   # restar the pk
        except Exception as error:
            print('\n Error try to DELETE FROM  table: {}. \n Server reponse: {}'.format(mytb, error))


    # --------------------------------------------------
    # This method lets you free to make a custom query
    # to your DB. You by yourself write a SQL string
    # comand completely  and inform it to this method.
    # The method shows via run terminal  the result.
    # --------------------------------------------------
    def custom_query(self, con, cur, mysql):
        print('\n\n THIS IS YOUR OWM QUERY STRING \n')
        try:
            cur.execute(mysql)
            con.comit()
            print('\n\n QUERY SUCCESSFULL \n\n')
        except Exception as error:
            print('\n Error by executing YOUR QUERY. \n Server said: {}'.format(error))



    # --------------------------------------------------
    # This method restart the PRIMARY KEY of a table.
    # That table is defined by user.
    # --------------------------------------------------
    #  TODO: i need to fix this method later.
    def restart_pk(self, con, cur, mytb):
        seq = mytb + "_id_seq"
        try:
            # sql = ' ALTER TABLE ' + mytb + 'AUTO_INCREMENT = 1'
            # sql = ' ALTER SEQUENCE ' + seq + ' ARESTART WITH %s'
            sql = ' ALTER SEQUENCE ' + seq + ' ARESTART WITH = %s'
            start = 1
            cur.execute(sql, start)
            con.comit()
            print('\n Primary key restarted SUCCESSFULY for table {}'.format(mytb))
        except Exception as error:
            print('\n Error by try restarting the primary key of {}. \n\n Server said: {}'.format(mytb, error))
