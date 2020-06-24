import psycopg2
import datetime

'''
Aqui esta presente o codigo que inicia a conexao com o banco de dados.
Optamos por utilizar um arquivo separado para deixar mais organizado e intuitivo o codigo da aplicacao

## IMPORTANTE: 
	Na funcao def __init__ deve-se verificar se a porta e o nome da base estao 
	devidamente conficurados conforme foi avisado no relatorio do trabalho
'''
class Connection:
	def __init__(self):
		print('Faça o login para iniciar...')
		usuario = input('Usuario: ')
		user = usuario
		senha = input('Senha: ')
		self.connection =  psycopg2.connect(user = usuario, password = senha, host = "localhost", port = "5432", database = "db_covid")
		self.cursor = self.connection.cursor()
		print("Conexao iniciada")

	def __del__(self):
		self.cursor.close()
		self.connection.close()
		print("Conexao encerrada!")

	def execute(self, command):
		try:
			self.cursor.execute(command)
		except psycopg2.Error as e:
			print(e.pgerror)
		self.connection.commit()

	def fetchone(self):
		return self.cursor.fetchone()

	def fetchall(self):
		return self.cursor.fetchall()

	def get_user(self):
		get_us = 'SELECT CURRENT_USER;'
		self.cursor.execute(get_us)
		self.connection.commit()
		got = self.cursor.fetchall()
		current_user = got[0][0]
		return current_user
