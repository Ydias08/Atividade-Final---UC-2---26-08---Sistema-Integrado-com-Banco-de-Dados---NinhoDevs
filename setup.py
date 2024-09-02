from Conexao import Conexao

#Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS gestaoescolar")
conexaoBD.manipular("CREATE DATABASE gestaoescolar")

#Criar as Tabelas
tabelaAluno = '''
    CREATE TABLE gestaoescolar.aluno (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_aluno VARCHAR(255) NOT NULL,
        dt_nascimento DATE NOT NULL,
        telefone_aluno CHAR(11)
    );'''
tabelaDisciplina = '''
    CREATE TABLE gestaoescolar.disciplina (
        id_disciplina INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_disciplina VARCHAR(255) NOT NULL
    );'''
tabelaProfessor = '''
    CREATE TABLE gestaoescolar.professor (
        id_professor INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_professor VARCHAR(255)
    );
'''
tabelaTurma = '''
    CREATE TABLE gestaoescolar.turma (
        id_turma INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        turno_turma CHAR(1),
        id_disciplina INT,
        id_professor INT,
        FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id_disciplina)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
'''
tabelaMatricula = '''
    CREATE TABLE gestaoescolar.matricula (
        id_matricula INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        data_matricula DATE DEFAULT (CURRENT_DATE),
        nota1 DECIMAL(3,1) DEFAULT 0.0,
        nota2 DECIMAL(3,1) DEFAULT 0.0,
        id_aluno INT,
        id_turma INT,
        FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (id_turma) REFERENCES Turma(id_turma)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );  
'''
conexaoBD.manipular(tabelaAluno)    
conexaoBD.manipular(tabelaDisciplina)
conexaoBD.manipular(tabelaProfessor)
conexaoBD.manipular(tabelaTurma)
conexaoBD.manipular(tabelaMatricula)

print('Banco de Dados criado com sucesso!')

#Adicionar inserts

insertAluno = ''' INSERT INTO gestaoescolar.aluno (nome_aluno, dt_nascimento, telefone_aluno) VALUES
    ('Ana Silva', '2002-03-15', '85999999999'),
    ('Bruno Costa', '2001-07-22', '85988888888'),
    ('Carlos Souza', '2000-11-30', '85977777777'),
    ('Daniela Oliveira', '1999-05-10', '85966666666'),
    ('Eduardo Pereira', '2002-08-25', '85955555555'),
    ('Fernanda Mendes', '2003-12-19', '85944444444'),
    ('Gabriel Lima', '1998-01-02', '85933333333'),
    ('Helena Fernandes', '2000-04-04', '85922222222'),
    ('Igor Ramos', '1997-09-18', '85911111111'),
    ('Juliana Rocha', '2001-06-14', '85900000000'),
    ('Karen Borges', '2002-10-20', '85899999999'),
    ('Leonardo Almeida', '2001-02-27', '85888888888'),
    ('Marcela Cardoso', '1999-03-07', '85877777777'),
    ('Nicolas Santos', '2000-12-15', '85866666666'),
    ('Olivia Moreira', '2001-05-23', '85855555555');
'''
insertDisciplina = '''INSERT INTO gestaoescolar.disciplina (nome_disciplina) VALUES
    ('Matemática'),
    ('Português'),
    ('História'),
    ('Geografia'),
    ('Física'),
    ('Química'),
    ('Biologia'),
    ('Inglês'),
    ('Educação Física'),
    ('Artes'),
    ('Filosofia'),
    ('Sociologia'),
    ('Informática'),
    ('Literatura'),
    ('Espanhol');
'''

insertProfessor = '''INSERT INTO gestaoescolar.professor (nome_professor) VALUES
    ('Maria das Graças'),
    ('João da Silva'),
    ('Carlos Alberto'),
    ('Fernanda Souza'),
    ('Paulo Mendes'),
    ('Rita de Cássia'),
    ('Marcos Lima'),
    ('Ana Clara'),
    ('José Henrique'),
    ('Tatiana Oliveira'),
    ('Ricardo Pereira'),
    ('Luciana Costa'),
    ('Roberto Lopes'),
    ('Viviane Moreira'),
    ('Renato Barbosa');      
'''

insertTurma = '''INSERT INTO gestaoescolar.turma (turno_turma, id_disciplina, id_professor) VALUES
    ('M', 1, 1),
    ('T', 2, 2),
    ('N', 3, 3),
    ('M', 4, 4),
    ('T', 5, 5),
    ('N', 6, 6),
    ('M', 7, 7),
    ('T', 8, 8),
    ('N', 9, 9),
    ('M', 10, 10),
    ('T', 11, 11),
    ('N', 12, 12),
    ('M', 13, 13),
    ('T', 14, 14),
    ('N', 15, 15);
'''

insertMatricula = '''INSERT INTO gestaoescolar.matricula (data_matricula, nota1, nota2, id_aluno, id_turma) VALUES
    ('2024-09-01', 8.5, 7.0, 1, 1),
    ('2024-09-01', 7.0, 6.5, 2, 2),
    ('2024-09-01', 9.0, 8.3, 3, 3),
    ('2024-09-01', 6.5, 7.7, 4, 4),
    ('2024-09-01', 8.0, 6.9, 5, 5),
    ('2024-09-01', 7.5, 7.5, 6, 6),
    ('2024-09-01', 8.2, 8.1, 7, 7),
    ('2024-09-01', 6.8, 6.4, 8, 8),
    ('2024-09-01', 9.3, 7.8, 9, 9),
    ('2024-09-01', 7.7, 7.0, 10, 10),
    ('2024-09-01', 8.9, 6.6, 11, 11),
    ('2024-09-01', 6.7, 8.4, 12, 12),
    ('2024-09-01', 9.1, 7.2, 13, 13),
    ('2024-09-01', 7.2, 8.9, 14, 14),
    ('2024-09-01', 8.6, 6.7, 15, 15),
    ('2024-09-01', 7.8, 8.3, 1, 2),
    ('2024-09-01', 8.1, 7.1, 2, 3),
    ('2024-09-01', 6.9, 7.9, 3, 4),
    ('2024-09-01', 8.4, 6.8, 4, 5),
    ('2024-09-01', 7.6, 8.2, 5, 6),
    ('2024-09-01', 9.0, 7.3, 6, 7),
    ('2024-09-01', 8.3, 7.7, 7, 8),
    ('2024-09-01', 6.5, 6.5, 8, 9),
    ('2024-09-01', 7.9, 8.0, 9, 10),
    ('2024-09-01', 8.7, 6.3, 10, 11),
    ('2024-09-01', 7.4, 7.8, 11, 12),
    ('2024-09-01', 8.2, 8.6, 12, 13),
    ('2024-09-01', 6.6, 7.5, 13, 14),
    ('2024-09-01', 9.2, 8.1, 14, 15),
    ('2024-09-01', 8.0, 7.4, 15, 1),
    ('2024-09-01', 7.1, 8.7, 1, 3),
    ('2024-09-01', 8.8, 7.6, 2, 4),
    ('2024-09-01', 6.4, 7.9, 3, 5),
    ('2024-09-01', 9.0, 6.2, 4, 6),
    ('2024-09-01', 7.5, 8.5, 5, 7);
'''

conexaoBD.manipular(insertAluno)
conexaoBD.manipular(insertDisciplina)
conexaoBD.manipular(insertProfessor)
conexaoBD.manipular(insertTurma)
conexaoBD.manipular(insertMatricula)

print('Inserts adicionados com sucesso!')