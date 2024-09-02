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
        idAluno = int(input("Digite o ID do aluno: "))
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
                    SELECT Disciplina.nome_disciplina, Turma.turno_turma, Matricula.nota1, Matricula.nota2
                    FROM Matricula
                    INNER JOIN Turma ON Matricula.id_turma = Turma.id_turma
                    INNER JOIN Disciplina ON Turma.id_disciplina = Disciplina.id_disciplina
                    WHERE Matricula.id_aluno = %s;
                ''', (idAluno,))
                
                if disciplinasMatriculadas:
                    print("Disciplinas Matriculadas:")
                    for disciplina in disciplinasMatriculadas:
                        nome_disciplina = disciplina[0]
                        turno = disciplina[1]
                        nota1 = disciplina[2]
                        nota2 = disciplina[3]
                        
                        # Calcular a média e determinar o status
                        if nota1 is None and nota2 is None:
                            status = "Em Andamento"
                        else:
                            media = (nota1 + nota2) / 2
                            if media >= 7:
                                status = "Aprovado"
                            elif media >= 4:
                                status = "Recuperação"
                            else:
                                status = "Reprovado"
                        
                        print(f"- {nome_disciplina} | Turno: {turno} | Nota 1: {nota1 if nota1 is not None else 'N/A'} | Nota 2: {nota2 if nota2 is not None else 'N/A'} | Média: {media if media is not None else 'N/A'} | Status: {status}")
                else:
                    print("Nenhuma disciplina encontrada para esse aluno.")
            
            elif escolha2 == 2:
                # Mostrar disciplinas disponíveis para matrícula excluindo as já matriculadas
                disciplinasDisponiveis = conexaoBD.consultarComParametros('''
                    SELECT Disciplina.id_disciplina, Disciplina.nome_disciplina
                    FROM Disciplina
                    WHERE Disciplina.id_disciplina NOT IN (
                        SELECT Turma.id_disciplina
                        FROM Matricula
                        INNER JOIN Turma ON Matricula.id_turma = Turma.id_turma
                        WHERE Matricula.id_aluno = %s
                    );
                ''', (idAluno,))
                
                if disciplinasDisponiveis:
                    print("Disciplinas Disponíveis para Matrícula:")
                    for disciplina in disciplinasDisponiveis:
                        print(f"ID: {disciplina[0]} | {disciplina[1]}")
                    
                    idTurma = int(input("Digite o ID da turma na qual deseja se matricular: "))

                    # Verificar se o aluno já está matriculado na turma
                    jaMatriculado = conexaoBD.consultarComParametros('''
                        SELECT * FROM Matricula WHERE id_aluno = %s AND id_turma = %s;
                    ''', (idAluno, idTurma))

                    if jaMatriculado:
                        print("Erro: O aluno já está matriculado nesta turma.")
                    else:
                        # Inserir matrícula na tabela de Matricula
                        conexaoBD.manipularComParametros('''
                            INSERT INTO Matricula (id_aluno, id_turma)
                            VALUES (%s, %s);
                        ''', (idAluno, idTurma))
                        print("Matrícula realizada com sucesso.")
                else:
                    print("Nenhuma disciplina disponível para matrícula.")
    
    elif escolha1 == 2:
        idProfessor = int(input("Digite o ID do professor: "))
        while True:
            escolha3 = int(input('''
1. Ver turmas lecionadas.
2. Atualizar notas de um aluno.
3. Ver alunos matriculados em uma turma.
0. Voltar ao menu anterior.
            '''))
            
            if escolha3 == 0:
                break
            
            elif escolha3 == 1:
                # Consultar turmas que o professor leciona
                turmasLecionadas = conexaoBD.consultarComParametros('''
                    SELECT Turma.id_turma, Disciplina.nome_disciplina
                    FROM Turma
                    INNER JOIN Disciplina ON Turma.id_disciplina = Disciplina.id_disciplina
                    WHERE Turma.id_professor = %s;
                ''', (idProfessor,))
                
                if turmasLecionadas:
                    print("Turmas Lecionadas:")
                    for turma in turmasLecionadas:
                        print(f"- ID da Turma: {turma[0]} | Disciplina: {turma[1]}")
                else:
                    print("Nenhuma turma encontrada para esse professor.")
            
            elif escolha3 == 2:
                idTurma = int(input("Digite o ID da turma: "))
                idAluno = int(input("Digite o ID do aluno: "))
                
                # Verificar se o aluno está matriculado na turma especificada
                matricula = conexaoBD.consultarComParametros('''
                    SELECT * FROM Matricula WHERE id_aluno = %s AND id_turma = %s;
                ''', (idAluno, idTurma))
                
                if matricula:
                    nota1 = float(input("Digite a Nota 1: "))
                    nota2 = float(input("Digite a Nota 2: "))
                    
                    # Atualizar notas na tabela de Matricula
                    conexaoBD.manipularComParametros('''
                        UPDATE Matricula
                        SET nota1 = %s, nota2 = %s
                        WHERE id_aluno = %s AND id_turma = %s;
                    ''', (nota1, nota2, idAluno, idTurma))
                    
                    print("Notas atualizadas com sucesso.")
                else:
                    print("Aluno não está matriculado nesta turma.")
                    
            elif escolha3 == 3:
                idTurma = int(input("Digite o ID da turma: "))
                
                # Consultar alunos matriculados na turma
                alunosMatriculados = conexaoBD.consultarComParametros('''
                    SELECT Aluno.id_aluno, Aluno.nome_aluno
                    FROM Matricula
                    INNER JOIN Aluno ON Matricula.id_aluno = Aluno.id_aluno
                    WHERE Matricula.id_turma = %s;
                ''', (idTurma,))
                
                if alunosMatriculados:
                    print(f"Alunos matriculados na turma {idTurma}:")
                    for aluno in alunosMatriculados:
                        print(f"ID: {aluno[0]} | Nome: {aluno[1]}")
                else:
                    print("Nenhum aluno encontrado nesta turma.")
