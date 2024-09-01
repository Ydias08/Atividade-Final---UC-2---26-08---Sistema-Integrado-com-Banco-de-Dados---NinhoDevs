from Conexao import Conexao

# Criar a instância da conexão
conexaoBD = Conexao("localhost", "root", "mysql", "")

# Conectar ao banco de dados (sem especificar o banco de dados)
conexaoBD.conectar()

# Deletar o banco de dados, se já existir
conexaoBD.manipular('''
    DROP DATABASE IF EXISTS gestaoescolar;
''')

# Criar o banco de dados
conexaoBD.manipular('''
    CREATE DATABASE gestaoescolar;
''')

# Selecionar o banco de dados
conexaoBD.manipular('''
    USE gestaoescolar;
''')

# Criar tabelas e inserir dados
conexaoBD.manipular('''
    CREATE TABLE Aluno (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_aluno VARCHAR(255) NOT NULL,
        dt_nascimento DATE NOT NULL,
        telefone_aluno CHAR(11)
    );''')

conexaoBD.manipular('''
        CREATE TABLE Disciplina (
        id_disciplina INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_disciplina VARCHAR(255) NOT NULL
    );''')    

conexaoBD.manipular('''
        CREATE TABLE Professor (
        id_professor INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome_professor VARCHAR(255)
    );
                    ''')

conexaoBD.manipular('''
  CREATE TABLE Turma (
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
                    ''')

conexaoBD.manipular('''
    CREATE TABLE Matricula (
    id_matricula INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    data_matricula DATE DEFAULT (CURRENT_DATE),
    nota DECIMAL(3,1) DEFAULT 0.0,
    id_aluno INT,
    id_turma INT,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_turma) REFERENCES Turma(id_turma)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );  
                    ''')

conexaoBD.manipular(''' INSERT INTO Aluno (nome_aluno, dt_nascimento, telefone_aluno) VALUES
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
                    ''')
    
conexaoBD.manipular('''INSERT INTO Disciplina (nome_disciplina) VALUES
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
                    ''')
    
conexaoBD.manipular('''INSERT INTO Professor (nome_professor) VALUES
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
                    ''')
    
conexaoBD.manipular('''INSERT INTO Turma (turno_turma, id_disciplina, id_professor) VALUES
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
                    ''')



# Fechar a conexão após terminar tudo
conexaoBD.desconectar()
