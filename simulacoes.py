class Simulacoes:
    def criar_prontuario(connection):
        id_paciente = input("Insira o ID do paciente: ")
        id_prontuario = input("Insira o ID do prontuario: ")

        create_query = '''CREATE TEMP TABLE temp_prontuario(
                        id_prontuario INT NOT NULL, id_paciente INT NOT NULL);'''
        insert_query = "INSERT INTO temp_prontuario (id_prontuario,id_paciente) VALUES ({},{});".format(id_prontuario, id_paciente)
        query = "SELECT * FROM temp_prontuario"


    def alterar_prontuario(connection):
        return None
    def criar_atendimento(connection):
        id_atendimento = input("Insira o ID do atendimento: ")
        data = input("Insira a data no formato 'yyyy-mm-dd': ")
        grau_avaliacao = input("Insira o grau de avaliacao: ")
        observacoes = input("Insira as observacoes: ")
        id_medico = input("Insira o ID do medico: ")
        id_paciente = input("Insira o ID do paciente: ")
        id_prontuario = input("Insira o ID do prontuario: ")

        create_query = '''CREATE TEMP TABLE temp_atendimento(
                        id_atendimento INT NOT NULL,data DATE,grau_avaliacao CHAR(1), observacoes VARCHAR(256),
                        id_medico INT NOT NULL,id_paciente INT NOT NULL,id_prontuario INT NOT NULL);'''
        insert_query = '''INSERT INTO temp_atendimento 
                        (id_atendimento,data,grau_avaliacao,observacoes,id_medico,id_paciente,id_prontuario) VALUES 
                        ({},TO_DATE({}, 'yyyy-mm-dd'),{},{},{},{},{});'''.format(id_atendimento, data, grau_avaliacao, observacoes, id_medico, id_paciente, id_prontuario)
        query = "SELECT * FROM temp_atendimento"

    def alterar_atendimento(connection):
        return None
    def criar_amostra(connection):
        id_amostra = input("Insira o ID da amostra: ")
        data = input("Insira a data no formato 'yyyy-mm-dd': ")
        resultado = input("Insira o resultado: ")
        id_laboratorio = input("Insira o ID do laboratorio: ")
        id_paciente = input("Insira o ID do paciente: ")
        id_pesquisador = input("Insira o ID do pesquisador: ")

        create_query = '''CREATE TEMP TABLE temp_amostra(
	                    id_amostra  INT NOT NULL, data DATE, resultado CHAR(1) NOT NULL,
	                    id_laboratorio  INT NOT NULL, id_paciente  INT NOT NULL, id_pesquisador INT NOT NULL);'''
        insert_query = '''INSERT INTO temp_amostra 
                        (id_amostra,data,resultado,id_laboratorio,id_paciente,id_pesquisador) VALUES 
                        ({},TO_DATE({}, 'yyyy-mm-dd'),{},{},{},{});'''.format(id_amostra, data, resultado, id_laboratorio, id_paciente, id_pesquisador)
        query = "SELECT * FROM temp_amostra"


    def alterar_amostra(connection):
        return None