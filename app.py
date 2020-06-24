from connection import Connection
from relatorios import Relatorios
from relatorios_simu import Relatorios2
from simulacoes import Simulacoes
import datetime
import pandas as pd

def tela_principal(usuario):
	print('\nTela principal para o usuario {}'.format(usuario.upper()))
	print('1 - Relatorios')
	print('2 - Simulacoes')
	print('3 - Overview')
	print('0 - Encerrar sessao')
	acao = input('O que voce deseja visualizar? ')
	if(int(acao) == 0):
		print('Encerrando sessao...')
	return int(acao)

def relat(connect, usuario):
	acao = 'z'
	while(acao != 'x'):
		print('\nRelatorios disponiveis para {}'.format(usuario.upper()))

		if(usuario == 'admincovid'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de Hospitais registrados')
			print('(c) Historico dos Atendimentos dos municipios registrados')
			print('(d) Historico de amostras geradas pelos pacientes')
			print('(e) Historico de Laboratorios e amostras recebidas')
			print('(f) Historico de Pesquisadores e amostras analisadas')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio1(connect, 0, 'none')
					offset = -1
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo nome do hospital? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_hospital = input('Digite o nome do hospital: ')
					Relatorios.relatorio2(connect, 1, nome_hospital)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio2(connect, 0, 'none')
					offset = -1			
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome da cidade? [s/n] ')
				if(filtro == 's'):
					offset = 1
					cidade = input('Digite o nome da cidade: ')
					Relatorios.relatorio3(connect, 1, cidade)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio3(connect, 0, 'none')
			elif(acao == 'd'):
				filtro = input('Voce deseja filtrar pelo data da amostra? [s/n] ')
				if(filtro == 's'):
					offset = 1
					data = input('Digite a data: ')
					Relatorios.relatorio4(connect, 1, data)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio4(connect, 0, 'none')
			elif(acao == 'e'):
				filtro = input('Voce deseja filtrar pelo nome do laboratorio? [s/n] ')
				if(filtro == 's'):
					offset = 1
					laboratorio = input('Digite o nome: ')
					Relatorios.relatorio5(connect, 1, laboratorio)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio5(connect, 0, 'none')
			elif(acao == 'f'):
				filtro = input('Voce deseja filtrar pelo nome do pesquisador? [s/n] ')
				if(filtro == 's'):
					offset = 1
					pesquisador = input('Digite o nome: ')
					Relatorios.relatorio6(connect, 1, pesquisador)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio6(connect, 0, 'none')

		elif(usuario == 'medicina'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de Hospitais registrados')
			print('(c) Historico dos Atendimentos dos municipios registrados')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio1(connect, 0, 'none')
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo nome do hospital? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_hospital = input('Digite o nome do hospital: ')
					Relatorios.relatorio2(connect, 1, nome_hospital)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio2(connect, 0, 'none')
					offset = -1
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome da cidade? [s/n] ')
				if(filtro == 's'):
					offset = 1
					cidade = input('Digite o nome da cidade: ')
					Relatorios.relatorio3(connect, 1, cidade)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio3(connect, 0, 'none')

		elif(usuario == 'pesquisa'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de amostras geradas pelos pacientes')
			print('(c) Historico de Laboratorios e amostras recebidas')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio1(connect, 0, 'none')
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo data da amostra? [s/n] ')
				if(filtro == 's'):
					offset = 1
					data = input('Digite a data: ')
					Relatorios.relatorio4(connect, 1, data)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio4(connect, 0, 'none')
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome do laboratorio? [s/n] ')
				if(filtro == 's'):
					offset = 1
					laboratorio = input('Digite o nome: ')
					Relatorios.relatorio5(connect, 1, laboratorio)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios.relatorio5(connect, 0, 'none')



def relatSimu(connect, usuario):
	acao = 'z'
	while(acao != 'x'):
		print('\nRelatorios disponiveis para {}'.format(usuario.upper()))

		if(usuario == 'admincovid'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de Hospitais registrados')
			print('(c) Historico dos Atendimentos dos municipios registrados')
			print('(d) Historico de amostras geradas pelos pacientes')
			print('(e) Historico de Laboratorios e amostras recebidas')
			print('(f) Historico de Pesquisadores e amostras analisadas')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios2.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio1(connect, 0, 'none')
					offset = -1
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo nome do hospital? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_hospital = input('Digite o nome do hospital: ')
					Relatorios2.relatorio2(connect, 1, nome_hospital)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio2(connect, 0, 'none')
					offset = -1			
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome da cidade? [s/n] ')
				if(filtro == 's'):
					offset = 1
					cidade = input('Digite o nome da cidade: ')
					Relatorios2.relatorio3(connect, 1, cidade)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio3(connect, 0, 'none')
			elif(acao == 'd'):
				filtro = input('Voce deseja filtrar pelo data da amostra? [s/n] ')
				if(filtro == 's'):
					offset = 1
					data = input('Digite a data: ')
					Relatorios2.relatorio4(connect, 1, data)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio4(connect, 0, 'none')
			elif(acao == 'e'):
				filtro = input('Voce deseja filtrar pelo nome do laboratorio? [s/n] ')
				if(filtro == 's'):
					offset = 1
					laboratorio = input('Digite o nome: ')
					Relatorios2.relatorio5(connect, 1, laboratorio)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio5(connect, 0, 'none')
			elif(acao == 'f'):
				filtro = input('Voce deseja filtrar pelo nome do pesquisador? [s/n] ')
				if(filtro == 's'):
					offset = 1
					pesquisador = input('Digite o nome: ')
					Relatorios2.relatorio6(connect, 1, pesquisador)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio6(connect, 0, 'none')

		elif(usuario == 'medicina'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de Hospitais registrados')
			print('(c) Historico dos Atendimentos dos municipios registrados')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios2.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio1(connect, 0, 'none')
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo nome do hospital? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_hospital = input('Digite o nome do hospital: ')
					Relatorios2.relatorio2(connect, 1, nome_hospital)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio2(connect, 0, 'none')
					offset = -1
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome da cidade? [s/n] ')
				if(filtro == 's'):
					offset = 1
					cidade = input('Digite o nome da cidade: ')
					Relatorios2.relatorio3(connect, 1, cidade)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio3(connect, 0, 'none')

		elif(usuario == 'pesquisa'):
			print('(a) Historico pessoal de pacientes testados positivo')
			print('(b) Historico de amostras geradas pelos pacientes')
			print('(c) Historico de Laboratorios e amostras recebidas')
			print('(x) Voltar ao menu anterior')
			acao = input('Qual relatorio voce deseja visualizar? ')
			offset = -1
			if(acao == 'a'):
				filtro = input('Voce deseja filtrar pelo nome do paciente? [s/n] ')
				if(filtro == 's'):
					offset = 1
					nome_paciente = input('Digite o nome do paciente: ')
					Relatorios2.relatorio1(connect, 1, nome_paciente)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio1(connect, 0, 'none')
			elif(acao == 'b'):
				filtro = input('Voce deseja filtrar pelo data da amostra? [s/n] ')
				if(filtro == 's'):
					offset = 1
					data = input('Digite a data: ')
					Relatorios2.relatorio4(connect, 1, data)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio4(connect, 0, 'none')
			elif(acao == 'c'):
				filtro = input('Voce deseja filtrar pelo nome do laboratorio? [s/n] ')
				if(filtro == 's'):
					offset = 1
					laboratorio = input('Digite o nome: ')
					Relatorios2.relatorio5(connect, 1, laboratorio)
					offset = -1
				elif(filtro == 'n'):
					offset = 0
					Relatorios2.relatorio5(connect, 0, 'none')




def overview(connect):
	acao = 'z'
	while(acao != 'x'):
		print('\n(a) Total de casos positivos da COVID-19')
		print('(b) Total de casos suspeitos da COVID-19')
		print('(c) 20 Hospitais com mais pacientes no ultimo mes')
		print('(d) 20 laboratorios com mais analises realizadas no ultimo mes')
		print('(e) 20 cidades com mais casos positivos no ultimo mes')
		print('(f) 20 cidades com mais casos suspeitos no ultimo mes')
		print('(x) Voltar ao menu anterior')
		acao = input('Qual informacao voce deseja visualizar? ')

		if(acao == 'a'):
			query = '''SELECT count(*) FROM amostra WHERE resultado = 'P';'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\n{} casos confirmados de COVID-19\n'.format(fetched[0][0]))

		elif(acao == 'b'):
			query = '''SELECT count(*) FROM atendimento;'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\n{} casos suspeitos de COVID-19\n'.format(fetched[0][0]))

		elif(acao == 'c'):
			query = '''SELECT hospital.nome AS "Hospital", 
						COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
							FROM hospital
								INNER JOIN paciente ON hospital.id_hospital = paciente.id_hospital
								INNER JOIN 	(SELECT id_paciente, data FROM atendimento
											WHERE data::TEXT LIKE '2020-03%') AS atend
											ON paciente.id_paciente = atend.id_paciente
							GROUP BY hospital.nome
							ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()

			print('\nOs 20 hospitais com o maior numero de pacientes em marco:')
			dt = pd.DataFrame(fetched, columns=['Hospital', 'Quantidade de pacientes'])
			print(dt)
			
		elif(acao == 'd'):
			query = '''SELECT laboratorio.nome AS "Nome", COUNT(id_amostra) AS "Quantidade de analises" 
						FROM amostra
							INNER JOIN laboratorio ON laboratorio.id_laboratorio = amostra.id_laboratorio
						WHERE amostra.data::TEXT LIKE '2020-03%'
						GROUP by laboratorio.nome
						ORDER BY COUNT(id_amostra) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nOs 20 laboratorios com o maior numero de analises em marco:')
			dt = pd.DataFrame(fetched, columns=['Laboratorio', 'Quantidade de analises'])
			print(dt)

		elif(acao == 'e'):
			query = '''SELECT hospital.cidade AS "Cidade", COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
						FROM hospital
							INNER JOIN paciente on hospital.id_hospital = paciente.id_hospital
							INNER JOIN 	(select id_paciente, data, resultado from amostra
										where data::TEXT LIKE '2020-03%' AND resultado = 'P') AS amos
										ON paciente.id_paciente = amos.id_paciente
						GROUP BY hospital.cidade
						ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nAs 20 cidades com mais casos positivos em marco:')
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Quantidade de casos confirmado'])
			print(dt)

		elif(acao == 'f'):
			query = '''SELECT hospital.cidade AS "Cidade", COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
						FROM hospital
							INNER JOIN paciente on hospital.id_hospital = paciente.id_hospital
							INNER JOIN 	(select id_paciente, data from atendimento
										where data::TEXT LIKE '2020-03%') AS atend
										ON paciente.id_paciente = atend.id_paciente
						GROUP BY hospital.cidade
						ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nAs 20 cidades com mais casos suspeitos em marco:')
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Quantidade de suspeitos'])
			print(dt)


		elif(acao == 'x'):
			return 1000


def overview2(connect):
	acao = 'z'
	while(acao != 'x'):
		print('\n(a) Total de casos positivos da COVID-19')
		print('(b) Total de casos suspeitos da COVID-19')
		print('(c) 20 Hospitais com mais pacientes no ultimo mes')
		print('(d) 20 laboratorios com mais analises realizadas no ultimo mes')
		print('(e) 20 cidades com mais casos positivos no ultimo mes')
		print('(f) 20 cidades com mais casos suspeitos no ultimo mes')
		print('(x) Voltar ao menu anterior')
		acao = input('Qual informacao voce deseja visualizar? ')

		if(acao == 'a'):
			query = '''SELECT count(*) FROM temp_amostra WHERE resultado = 'P';'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\n{} casos confirmados de COVID-19\n'.format(fetched[0][0]))

		elif(acao == 'b'):
			query = '''SELECT count(*) FROM temp_atendimento;'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\n{} casos suspeitos de COVID-19\n'.format(fetched[0][0]))

		elif(acao == 'c'):
			query = '''SELECT hospital.nome AS "Hospital", 
						COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
							FROM hospital
								INNER JOIN paciente ON hospital.id_hospital = paciente.id_hospital
								INNER JOIN 	(SELECT id_paciente, data FROM temp_atendimento
											WHERE data::TEXT LIKE '2020-03%') AS atend
											ON paciente.id_paciente = atend.id_paciente
							GROUP BY hospital.nome
							ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()

			print('\nOs 20 hospitais com o maior numero de pacientes em marco:')
			dt = pd.DataFrame(fetched, columns=['Hospital', 'Quantidade de pacientes'])
			print(dt)
			
		elif(acao == 'd'):
			query = '''SELECT laboratorio.nome AS "Nome", COUNT(id_amostra) AS "Quantidade de analises" 
						FROM temp_amostra
							INNER JOIN laboratorio ON laboratorio.id_laboratorio = temp_amostra.id_laboratorio
						WHERE temp_amostra.data::TEXT LIKE '2020-03%'
						GROUP by laboratorio.nome
						ORDER BY COUNT(id_amostra) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nOs 20 laboratorios com o maior numero de analises em marco:')
			dt = pd.DataFrame(fetched, columns=['Laboratorio', 'Quantidade de analises'])
			print(dt)

		elif(acao == 'e'):
			query = '''SELECT hospital.cidade AS "Cidade", COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
						FROM hospital
							INNER JOIN paciente on hospital.id_hospital = paciente.id_hospital
							INNER JOIN 	(select id_paciente, data, resultado from temp_amostra
										where data::TEXT LIKE '2020-03%' AND resultado = 'P') AS amos
										ON paciente.id_paciente = amos.id_paciente
						GROUP BY hospital.cidade
						ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nAs 20 cidades com mais casos positivos em marco:')
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Quantidade de casos confirmado'])
			print(dt)

		elif(acao == 'f'):
			query = '''SELECT hospital.cidade AS "Cidade", COUNT(paciente.id_paciente) AS "Quantidade de pacientes" 
						FROM hospital
							INNER JOIN paciente on hospital.id_hospital = paciente.id_hospital
							INNER JOIN 	(select id_paciente, data from temp_atendimento
										where data::TEXT LIKE '2020-03%') AS atend
										ON paciente.id_paciente = atend.id_paciente
						GROUP BY hospital.cidade
						ORDER BY COUNT(paciente.id_paciente) DESC LIMIT 20;
						'''
			connect.execute(query)	
			fetched = connect.fetchall()
			print('\nAs 20 cidades com mais casos suspeitos em marco:')
			dt = pd.DataFrame(fetched, columns=['Cidade', 'Quantidade de suspeitos'])
			print(dt)


		elif(acao == 'x'):
			return 1000

def simulacao(connect, usuario):
	acao = 'z'
	while(acao != 'x'):
		print("\nAbaixo estao as acoes disponiveis para simulacao.")
		if (usuario == 'medicina'):
			print("(a) Criar um novo prontuario")
			print("(b) Alterar um prontuario")
			print("(c) Criar um novo atendimento")
			print("(d) Alterar um atendimento")
			print("(e) Visualizar relatorios das simulações")
			print("(f) Visualizar overview das simulações")
			print("(x) Voltar ao menu anterior")
			acao = input('O que voce deseja visualizar? ')

			if (acao == 'a'):
				Simulacoes.criar_prontuario(connect)
			elif (acao == 'b'):
				Simulacoes.alterar_prontuario(connect)
			elif (acao == 'c'):
				Simulacoes.criar_atendimento(connect)
			elif (acao == 'd'):
				Simulacoes.alterar_atendimento(connect)
			elif (acao == 'e'):
				relatSimu(connect,usuario)
			elif (acao == 'f'):	
				overview2(connect)
		

		elif (usuario == 'pesquisa'):
			print("(a) Criar uma nova amostra")
			print("(b) Alterar uma amostra")
			print("(c) Visualizar relatorios das simulações")
			print("(d) Visualizar overview das simulações")
			print("(x) Voltar ao menu anterior")
			acao = input('O que voce deseja visualizar? ')

			if (acao == 'a'):
				Simulacoes.criar_amostra(connect)
			elif (acao == 'b'):
				Simulacoes.alterar_amostra(connect)
			elif (acao == 'c'):
				relatSimu(connect,usuario)
			elif (acao == 'd'):	
				overview2(connect)	

		elif (usuario == 'admincovid'):
			print("(a) Criar um novo prontuario")
			print("(b) Alterar um prontuario")
			print("(c) Criar um novo atendimento")
			print("(d) Alterar um atendimento")
			print("(e) Criar uma nova amostra")
			print("(f) Alterar uma amostra")
			print("(g) Visualizar relatorios das simulações")
			print("(h) Visualizar overview das simulações")
			print("(x) Voltar ao menu anterior")
			acao = input('O que voce deseja visualizar? ')

			if (acao == 'a'):
				Simulacoes.criar_prontuario(connect)
			elif (acao == 'b'):
				Simulacoes.alterar_prontuario(connect)
			elif (acao == 'c'):
				Simulacoes.criar_atendimento(connect)
			elif (acao == 'd'):
				Simulacoes.alterar_atendimento(connect)
			elif (acao == 'e'):
				Simulacoes.criar_amostra(connect)
			elif (acao == 'f'):
				Simulacoes.alterar_amostra(connect)
			elif (acao == 'g'):
				relatSimu(connect,usuario)
			elif (acao == 'h'):	
				overview2(connect)		
			
		else:
			print("Usuario nao cadastrado. Tente 'medicina', 'pesquisa' ou 'admincovid'.")


def aplicacao():
	conn = Connection()

	# Pega o data de hoje junto com o usuario atual e salva na tabela de logs
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	insert_query = '''INSERT INTO logs VALUES(current_user, '{}')'''.format(date)
	conn.execute(insert_query)
	temp_table1 = '''CREATE TEMP TABLE temp_amostra(
	                    id_amostra  INT NOT NULL, data DATE, resultado CHAR(1) NOT NULL,
	                    id_laboratorio  INT NOT NULL, id_paciente  INT NOT NULL, id_pesquisador INT NOT NULL);'''

	temp_table2 = '''CREATE TEMP TABLE temp_atendimento(
                        id_atendimento INT NOT NULL,data DATE,grau_avaliacao CHAR(1), observacoes VARCHAR(256),
                        id_medico INT NOT NULL,id_paciente INT NOT NULL,id_prontuario INT NOT NULL);'''

	temp_table3 = '''CREATE TEMP TABLE temp_prontuario(
                        id_prontuario INT NOT NULL, id_paciente INT NOT NULL);'''					

	conn.execute(temp_table1)
	conn.execute(temp_table2)
	conn.execute(temp_table3)

	carga1 = "INSERT INTO temp_prontuario SELECT * FROM Prontuario;"
	carga2 = "INSERT INTO temp_amostra SELECT * FROM Amostra;"
	carga3 = "INSERT INTO temp_atendimento SELECT * FROM Atendimento;"
	conn.execute(carga1)
	conn.execute(carga2)
	conn.execute(carga3)
	current = conn.get_user()

	action = 1000

	while(action != 0):
		if(current == 'medicina'):
			action = tela_principal(current)
			if(action == 1):
				relat(conn, current)
			elif(action == 2):
				simulacao(conn, current)
			elif(action == 3):
				action = overview(conn)

		elif(current == 'pesquisa'):
			action = tela_principal(current)
			if(action == 1):
				relat(conn, current)
			elif(action == 2):
				simulacao(conn, current)
			elif(action == 3):
				action = overview(conn)

		elif(current == 'admincovid'):
			action = tela_principal(current)
			if(action == 1):
				relat(conn, current)
			elif(action == 2):
				simulacao(conn, current)
			elif(action == 3):
				action = overview(conn)

		
		

aplicacao()
