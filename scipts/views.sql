-- Este é um dos codigos que, conforme mensionado no relatorio, precisam ser executados antes da aplicacao para a criacao das views que permitirao acesso
-- aos usuarios a dados gerais do banco

/*VIEW 1
  HISTORICO_PESSOAL*/
CREATE OR REPLACE VIEW Historico_Pessoal(nome, idade, sexo, 
				data_nasc, tel, endereco, hospital) AS

	SELECT DISTINCT P.nome,  P.idade,  P.sexo,  P.data_nasc, 
					 CONCAT(P.telefone_fixo || P.telefone_celular) AS tel, 
					 CONCAT( P.cidade,CONCAT( P.estado, P.pais)) AS endereco,  
					 P.id_hospital
			FROM Pessoa P 
			JOIN Paciente G ON P.id_pessoa = G.id_paciente 
			JOIN Amostra A ON G.id_paciente = A.id_paciente 
			WHERE resultado = 'P';

/*VIEW 2
  HISTORICO_HOSPITAIS*/
CREATE OR REPLACE VIEW Historico_dos_Hospitais(nome, endereco, qtd_funcionario, qtd_leitos, qtd_atendimentos, 
				qtd_pacientes_atendidos) AS

	SELECT DISTINCT  A.nome, 
					 CONCAT(A.cidade, CONCAT( A.estado, A.pais)) AS endereco,
					 A.qtd_funcionario, A.qtd_leitos,  
					 COUNT(C.id_atendimento) as qtdAtd, COUNT(P.id_paciente) as qtdPacAtd 
			FROM Hospital A JOIN Paciente P ON P.id_hospital = A.id_hospital 
			JOIN Atendimento C ON C.id_paciente = P.id_paciente
			GROUP BY A.nome, endereco, A.qtd_funcionario, A.qtd_leitos
			ORDER BY A.nome ASC;
	
			
--DROP VIEW Historico_dos_Hospitais;
--SELECT * FROM Historico_dos_Hospitais;

/*VIEW 3
  HISTORICO_DE_ATENDIMENTO_DOS_MUNICIPIOS */

CREATE OR REPLACE VIEW Historico_de_Atendimento_dos_Municipios(Cidade, Atendimentos_Totais, Atendimentos_Mes_Janeiro, Atendimentos_Mes_Fevereiro, 
							       Atendimentos_Mes_Marco, Atendimentos_Mes_Abril, qtd_pacientes_atendidos) AS

	SELECT DISTINCT  P.cidade, 
			 COUNT(C.id_atendimento) as atdTotal,
			 COUNT(C.id_atendimento) filter (WHERE EXTRACT(MONTH FROM data) = '01') as atdMes1,
			 COUNT(C.id_atendimento) filter (WHERE EXTRACT(MONTH FROM data) = '02') as atdMes2,
			 COUNT(C.id_atendimento) filter (WHERE EXTRACT(MONTH FROM data) = '03') as atdMes3,
			 COUNT(C.id_atendimento) filter (WHERE EXTRACT(MONTH FROM data) = '04') as atdMes4,
			 COUNT(Pa.id_paciente) as qtd_pacienteAtd
			 FROM Pessoa P 
			 JOIN Paciente Pa ON P.id_pessoa = Pa.id_paciente 
			 JOIN Atendimento C ON C.id_paciente = Pa.id_paciente
			 GROUP BY P.cidade
			 ORDER BY atdTotal desc;

--DROP VIEW Historico_de_Atendimento_dos_Municipios;
--SELECT * FROM Historico_de_Atendimento_dos_Municipios;

/*VIEW 4
  HISTORICO_DE_AMOSTRAS */
CREATE OR REPLACE VIEW Historico_de_Amostras(Nome_Paciente, Idade, Sexo, Endereco_Completo, Data_Amostra,  
				                             Resultado, Laboratório) AS

	SELECT DISTINCT  P.nome, P.idade, P.sexo,
				     CONCAT( P.cidade,CONCAT( P.estado, P.pais)) AS endereco,  
					 A.data, A.Resultado, L.nome
					 FROM Pessoa P 
					 JOIN Paciente Pa ON P.id_pessoa = Pa.id_paciente 
					 JOIN Amostra A ON A.id_paciente = Pa.id_paciente
					 JOIN Laboratorio L ON L.id_laboratorio = A.id_laboratorio
					 ORDER BY A.data desc;
	
--DROP VIEW Historico_de_Amostras;
--SELECT * FROM Historico_de_Amostras;

/*VIEW 5
  HISTORICO_DE_LABORATÓRIOS */
CREATE OR REPLACE VIEW Historico_de_Laboratórios(Nome_Laboratório, Quantidade_de_Pesquisadores, Endereco_Completo, 
												 qtd_Amostra_Recebidas) AS

	SELECT DISTINCT  L.nome, L.qtd_Pesquisadores,
				     CONCAT(L.cidade,CONCAT( L.estado, L.pais)) AS endereco,  
					 COUNT(A.id_amostra)
					 FROM Laboratorio L 
					 JOIN Amostra A ON L.id_laboratorio = A.id_laboratorio
					 GROUP BY L.NOME, L.qtd_pesquisadores, endereco
					 ORDER BY L.nome asc;
	
--DROP VIEW Historico_de_Laboratórios;
--SELECT * FROM Historico_de_Laboratórios;

/*VIEW 6
  HISTORICO_DE_PESQUISADORES */
CREATE OR REPLACE VIEW Historico_de_Pesquisadores(Nome_Pesquisador, Registro_Institucional, Data_de_Contratacao, 
												 Identificador_de_Amostra, Data_da_Amostra, Resultado_da_amostra) AS

	SELECT DISTINCT  P.nome, Pesq.crm, F.data_contratacao, A.id_amostra, A.data, A.resultado
				     FROM Amostra A 
					 JOIN Pesquisador Pesq ON Pesq.id_pesquisador = A.id_pesquisador
					 JOIN Pessoa P ON Pesq.id_pesquisador = P.id_pessoa
					 JOIN Funcionario F ON P.id_pessoa = F.id_funcionario;
	
--DROP VIEW Historico_de_Pesquisadores;
--SELECT * FROM Historico_de_Pesquisadores;