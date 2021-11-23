import mysql.connector		#Importando o modulo para conexão com o servidor sql

mydb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")	#Informações do servidor sql

mycursor = mydb.cursor()	#The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object. https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html

print("digite o rg")		#Mostrar na tela "digite o rg" para melhor visualização

rg=input()			#Receber informações digitadas no terminal e guardar na variavel "rg"

print("digite o ra")		#Mostrar na tela "digite o ra" para melhor visualização
ra=input()			#Receber informações digitadas no terminal e guradar na variavel "ra"

comando="select nome from pessoas where rg='{}' and ra='{}'".format(rg,ra)	#Comando sql para selecionar a 

mycursor.execute(comando)

myresult = mycursor.fetchall()	#The method fetches all (or all remaining) rows of a query result set and returns a list of tuples. If no more rows are available, it returns an empty list. https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

print(repr(myresult))

if str(myresult) == "[]":	#Se a resposta do servidor for nula
    print("nao logado")		#Escreva "nao logado"
else:				#Se não
    print("Bem Vindo {}".format(str(myresult).replace("[('","").replace("',)]","")))	#Escrever "Bem Vindo" junto ao nome da pessoa formatado corretamente

#https://www.w3schools.com/python/python_mysql_select.asp
