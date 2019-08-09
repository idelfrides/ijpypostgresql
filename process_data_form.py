# ---------------------------------------------
#   ====  MODULE INFORMATION  ====
# ---------------------------------------------
# this module proccess form. recover values of
# form process them and insert on the table
# ---------------------------------------------

# ---------------------------------------------
# import python modules
# ---------------------------------------------
from ijpymysql import ModuleMySQLdb as mdb
from  ijpymysql import Crud_build as cb
import cgi   # common geteway interface support

# ---------------------------------------------
#  create an object of cgi to get data form
# ---------------------------------------------
myform = cgi.FieldStorage()


# --------------------------------------------
# tratamento de dados vindos do formulário
# --------------------------------------------
name = myform.getvalue("n_uname")
company = myform.getvalue("n_comp")
salary = myform.getvalue("n_salary")
role = myform.getvalue('n_role')
adress = myform.getvalue('n_adress')

#  REGULAR EXPRESSION PYTHONS

# ---------------------------------------------
#  show data individualy
# ---------------------------------------------
print('\n {}\n {}\n {}\n {} \n {}'.format(name, company, salary, role, adress))

# ---------------------------------------------
# create a list called data o store data on it
# ---------------------------------------------
data = list()  #

# ---------------------------------------------
# add values recovered from form to data list
# ---------------------------------------------
data.append(name)
data.append(company)
data.append(salary)
data.append(role)
data.append(adress)


# ---------------------------------------------
#  create objects from  modules of ijpymysql_package package
# ---------------------------------------------
mdbo = mdb.ModuleMySQLdb()
cbo = cb.Crud_build()

# ---------------------------------------------
#  set conection to local server
# ---------------------------------------------
con, cur = mdbo.set_conec_with_db()


# ---------------------------------------------
#  get table name
# ---------------------------------------------
devtb = mdbo.dev_table

# ---------------------------------------------
#  create an  record on the table
# ---------------------------------------------
cbo.create(con, cur, devtb, data)


