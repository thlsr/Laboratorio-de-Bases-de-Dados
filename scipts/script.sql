CREATE TABLE logs(
	quem VARCHAR(15) NOT NULL,
	horario VARCHAR(30) NOT NULL
);

CREATE ROLE medicina LOGIN ENCRYPTED PASSWORD 'medicina';
CREATE ROLE pesquisa LOGIN ENCRYPTED PASSWORD 'pesquisa';
CREATE USER admincovid SUPERUSER ENCRYPTED PASSWORD 'superadmin';

GRANT INSERT ON logs TO medicina;
GRANT INSERT ON logs TO pesquisa;

GRANT SELECT ON amostra TO medicina;
GRANT SELECT ON amostra TO pesquisa;

GRANT SELECT ON atendimento TO medicina;
GRANT SELECT ON atendimento TO pesquisa;

GRANT SELECT ON hospital TO medicina;
GRANT SELECT ON hospital TO pesquisa;

GRANT SELECT ON laboratorio TO medicina;
GRANT SELECT ON laboratorio TO pesquisa;

GRANT SELECT ON historico_pessoal TO medicina;
GRANT SELECT ON historico_pessoal TO pesquisa;

GRANT SELECT ON historico_dos_hospitais TO medicina;

GRANT SELECT ON Historico_de_Atendimento_dos_Municipios TO medicina;

GRANT SELECT ON Historico_de_Amostras TO pesquisa;

GRANT SELECT ON Historico_de_Laboratórios TO pesquisa;

GRANT SELECT ON prontuario TO medicina;
GRANT SELECT ON prontuario TO pesquisa;

GRANT SELECT ON pessoa TO medicina;
GRANT SELECT ON paciente TO medicina;
GRANT SELECT ON pessoa TO pesquisa;
GRANT SELECT ON paciente TO pesquisa;
