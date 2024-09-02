from Conexao import Conexao

# Conexão com o banco de dados
conexaoBD = Conexao("localhost", "root", "mysql", "gestaoescolar")

while True:
    print(f"{'-' * 15} Sistema de Gestão Escolar {'-' * 15}")
    print('''
1. Área do Aluno.
2. Área do Professor.
0. Encerrar programa.
    ''')
    escolha1 = int(input("Selecione a opção que deseja: "))
    
    if escolha1 == 0:
        print("Programa Encerrado")
        break
    
    elif escolha1 == 1:
        idDigitado = int(input("Digite o ID do aluno: "))
        while True:
            escolha2 = int(input('''
1. Ver disciplinas matriculadas.
2. Matricular-se em uma disciplina.
0. Voltar ao menu anterior.
            '''))
            
            if escolha2 == 0:
                break
            
            elif escolha2 == 1:
                # Consultar disciplinas nas quais o aluno está matriculado
                disciplinasMatriculadas = conexaoBD.consultarComParametros('''
                    SELECT Disciplina.nome_disciplina
                    FROM Matricula
                    INNER JOIN Turma ON Matricula.id_turma = Turma.id_turma
                    INNER JOIN Disciplina ON Turma.id_disciplina = Disciplina.id_disciplina
                    WHERE Matricula.id_aluno = %s;
                ''', (idDigitado,))
                matriculas = conexaoBD.consultarComParametros('SELECT * FROM gestaoescolar.matricula WHERE id_aluno  = %s', (idDigitado,))
                for matricula in matriculas: 
                    nota1 = matricula[2]
                    nota2 = matricula [3]
                    media = (nota1 + nota2)/2
                
                if disciplinasMatriculadas:
                    print("Disciplinas Matriculadas:")
                for disciplina in disciplinasMatriculadas:
                    print(f"- {disciplina[0]} Nota 1: {nota1}, Nota 2: {nota2}, Média: {media}")
                else:
                    print("Nenhuma disciplina encontrada para esse aluno.")
            
            elif escolha2 == 2:
                disciplinas = conexaoBD.consultar('SELECT * FROM disciplina')
                for disciplina in disciplinas:
                    print(f'''
ID:{disciplina[0]} {disciplina[1]}''' )
                idTurma = int(input("Digite o ID da turma na qual deseja se matricular: "))
                    
                # Inserir matrícula na tabela de Matricula
                conexaoBD.manipularComParametros('''
                    INSERT INTO Matricula (id_aluno, id_turma)
                    VALUES (%s, %s);
                ''', (idDigitado, idTurma))
                
                print("Matrícula realizada com sucesso.")
    

              