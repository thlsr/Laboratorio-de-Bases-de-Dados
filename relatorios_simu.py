import pandas as pd
from temp_views import Temporary_views

pd.set_option('display.width', 100000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.max_rows', 10000000)


'''
Este arquivo contem a classe Relatorios2 que corresponde à geracao de relatorio incluindo-se as simulacoes feitas pelos usuarios
'''
class Relatorios2:
	def relatorio1(connection, offset, nome):
		Temporary_views.historico_pessoal2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM historico_pessoal2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do Paciente', 'Idade', 'Sexo', 'Data de nascimento', 'Telefone', 'Endereco', 'Id Hospital'])
			print(dt)
		elif(offset == 1):
			s = '%'
			nome = f'{s}{nome}{s}'
			query = '''SELECT * FROM historico_pessoal2 WHERE nome LIKE '{}';'''.format(nome)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do Paciente', 'Idade', 'Sexo', 'Data de nascimento', 'Telefone', 'Endereco', 'Id Hospital'])
			print(dt)
			

	def relatorio2(connection, offset, nome_hospital):
		Temporary_views.Historico_dos_Hospitais2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM Historico_dos_Hospitais2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome Hospital', 'Endereco', 'Quantidade de funcionarios', 'Quantidade de leitos', 'Quantidade de atendimentos', 'Quantidade de pacientes atendidos'])
			print(dt)
		elif(offset == 1):
			s = '%'
			nome_hospital = f'{s}{nome_hospital}{s}'
			query = '''SELECT * FROM Historico_dos_Hospitais2 WHERE nome LIKE '{}';'''.format(nome_hospital)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome Hospital', 'Endereco', 'Quantidade de funcionarios', 'Quantidade de leitos', 'Quantidade de atendimentos', 'Quantidade de pacientes atendidos'])
			print(dt)


	def relatorio3(connection, offset, cidade):
		Temporary_views.Historico_de_Atendimento_dos_Municipios2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM Historico_de_Atendimento_dos_Municipios2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Total de atendimentos', 'Atendimentos em janeiro', 'Atendimentos em fevereiro', 'Atendimentos em marco', 'Atendimentos em abril', 'Quantidade de pacientes atendidos'])
			print(dt)
		elif(offset == 1):
			s = '%'
			cidade = f'{s}{cidade}{s}'
			query = '''SELECT * FROM Historico_de_Atendimento_dos_Municipios2 WHERE cidade LIKE '{}';'''.format(cidade)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Total de atendimentos', 'Atendimentos em janeiro', 'Atendimentos em fevereiro', 'Atendimentos em marco', 'Atendimentos em abril', 'Quantidade de pacientes atendidos'])
			print(dt)


	def relatorio4(connection, offset, data):
		Temporary_views.Historico_de_Amostras2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM Historico_de_Amostras2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do paciente', 'Idade', 'Sexo', 'Endereco', 'Data da amostra', 'Resultado', 'Laboratorio'])
			print(dt)
		elif(offset == 1):
			s = '%'
			data = f'{s}{data}{s}'
			query = '''SELECT * FROM Historico_de_Amostras2 WHERE data_amostra::TEXT LIKE '{}';'''.format(data)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do paciente', 'Idade', 'Sexo', 'Endereco', 'Data da amostra', 'Resultado', 'Laboratorio'])
			print(dt)

	def relatorio5(connection, offset, laboratorio):
		Temporary_views.Historico_de_Laboratorios2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM Historico_de_Laboratorios2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do laboratorio', 'Quantidade de pesquisadores', 'Endereco', 'Quantidade de amostras recebidas'])
			print(dt)
		elif(offset == 1):
			s = '%'
			laboratorio = f'{s}{laboratorio}{s}'
			query = '''SELECT * FROM Historico_de_Laboratorios2 WHERE nome_laboratorio LIKE '{}';'''.format(laboratorio)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do laboratorio', 'Quantidade de pesquisadores', 'Endereco', 'Quantidade de amostras recebidas'])
			print(dt)


	def relatorio6(connection, offset, pesquisador):
		Temporary_views.Historico_de_Pesquisadores2(connection)
		# Quando offset for 0, sginifica que nao sera aplicado um filtro
		if(offset == 0):
			query = '''SELECT * FROM Historico_de_Pesquisadores2'''
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do pesquisador', 'Registro Institucional', 'Data de contratacao', 'Identificador de amostra', 'Data da amostra', 'Resultado da amostra'])
			print(dt)
		elif(offset == 1):
			s = '%'
			pesquisador = f'{s}{pesquisador}{s}'
			query = '''SELECT * FROM Historico_de_Pesquisadores2 WHERE nome_pesquisador LIKE '{}';'''.format(pesquisador)
			connection.execute(query)
			fetched = connection.fetchall()
			dt = pd.DataFrame(fetched, columns=['Nome do pesquisador', 'Registro Institucional', 'Data de contratacao', 'Identificador de amostra', 'Data da amostra', 'Resultado da amostra'])
			print(dt)