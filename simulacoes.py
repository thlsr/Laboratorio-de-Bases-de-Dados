'''
Este arquivo contem as execucoes de querys que criam as simulacoes para cada usuario
'''
class Simulacoes:
    def criar_prontuario(connection):
        id_paciente = input("Insira o ID do paciente: ")
        id_prontuario = input("Insira o ID do prontuario: ")

        insert_query = "INSERT INTO temp_prontuario (id_prontuario,id_paciente) VALUES ({},{});".format(id_prontuario, id_paciente)
        query = "SELECT * FROM temp_prontuario"
        connection.execute(insert_query); 
        print('\nProntuario numero {} para o paciente {} criado com sucesso!'.format(id_paciente, id_prontuario))


    def alterar_prontuario(connection):
        id_prontuario = input("Insira o ID do prontuario para alteração: ")
        id_paciente = input("Insira o ID do novo paciente: ")
        update_query = '''UPDATE  temp_prontuario 
                          SET  id_paciente={}
                          WHERE id_prontuario={}'''.format(id_paciente,id_prontuario)
        connection.execute(update_query);
        print('\nAlteracao no pronutuario {} para o paciente {} realizada com sucesso para simulacao!'.format(id_prontuario, id_paciente)) 


    def criar_atendimento(connection):
        id_atendimento = input("Insira o ID do atendimento: ")
        data = input("Insira a data no formato 'yyyy-mm-dd': ")
        grau_avaliacao = input("Insira o grau de avaliacao: ")
        observacoes = input("Insira as observacoes: ")
        id_medico = input("Insira o ID do medico: ")
        id_paciente = input("Insira o ID do paciente: ")
        id_prontuario = input("Insira o ID do prontuario: ")

        
        insert_query = '''INSERT INTO temp_atendimento 
                        (id_atendimento,data,grau_avaliacao,observacoes,id_medico,id_paciente,id_prontuario) VALUES 
                        ({},TO_DATE('{}', 'yyyy-mm-dd'),'{}','{}',{},{},{});'''.format(id_atendimento, data, grau_avaliacao, observacoes, id_medico, id_paciente, id_prontuario)
        query = "SELECT * FROM temp_atendimento"
        connection.execute(insert_query) 
        print('\nAtendimento {} criado com sucesso para simulacao!'.format(id_atendimento))


    def alterar_atendimento(connection):
        id_atendimento = input("Insira o ID do atendimento para alteração: ")
        data = input("Insira a nova data no formato 'yyyy-mm-dd': ")
        grau_avaliacao = input("Insira o novo grau de avaliacao: ")
        observacoes = input("Insira as novas observacoes: ")
        id_medico = input("Insira o novo ID do medico: ")
        id_paciente = input("Insira o novo ID do paciente: ")
        id_prontuario = input("Insira o novo ID do prontuario: ")
        update_query ='''UPDATE  temp_atendimento 
                          SET  data={},grau_avaliacao='{}',observacoes='{}',id_medico={},id_paciente={},id_prontuario={}
                          WHERE id_atendimento={}'''.format(data, grau_avaliacao, observacoes, id_medico, id_paciente, id_prontuario,id_atendimento)
        connection.execute(update_query)
        print('\nAtendimento {} alterado com sucesso para simulacao!'.format(id_atendimento))

    def criar_amostra(connection):
        id_amostra = input("Insira o ID da amostra: ")
        data = input("Insira a data no formato 'yyyy-mm-dd': ")
        resultado = input("Insira o resultado: ")
        id_laboratorio = input("Insira o ID do laboratorio: ")
        id_paciente = input("Insira o ID do paciente: ")
        id_pesquisador = input("Insira o ID do pesquisador: ")

        insert_query = '''INSERT INTO temp_amostra 
                        (id_amostra,data,resultado,id_laboratorio,id_paciente,id_pesquisador) VALUES 
                        ({},TO_DATE('{}', 'yyyy-mm-dd'),'{}',{},{},{});'''.format(id_amostra, data, resultado, id_laboratorio, id_paciente, id_pesquisador)
        query = "SELECT * FROM temp_amostra"
        connection.execute(insert_query)
        print('\nAmostra {} criada com sucesso para simulacao!'.format(id_amostra))


    def alterar_amostra(connection):
        id_amostra = input("Insira o ID da amostra para alteração: ")
        data = input("Insira a nova data no formato 'yyyy-mm-dd': ")
        resultado = input("Insira o novo resultado: ")
        id_laboratorio = input("Insira o novo ID do laboratorio: ")
        id_paciente = input("Insira o novo ID do paciente: ")
        id_pesquisador = input("Insira o novo ID do pesquisador: ")
        update_query ='''UPDATE  temp_amostra 
                          SET  data='{}',resultado='{}',id_laboratorio={},id_paciente={},id_pesquisador={}
                          WHERE id_amostra={}'''.format(data, resultado, id_laboratorio, id_paciente, id_pesquisador,id_amostra)
        connection.execute(update_query)
        print('\nAmostra {} aleterada com sucesso para simulacao!'.format(id_amostra))