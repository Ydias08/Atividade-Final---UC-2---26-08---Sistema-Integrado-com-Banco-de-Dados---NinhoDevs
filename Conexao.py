import mysql.connector

class Conexao:
    def __init__(self, host, usuario, senha, banco_dados=None):
        self._host = host
        self._usuario = usuario
        self._senha = senha
        self._banco_dados = banco_dados
        self._conexao = None
        self._cursor = None

    def conectar(self):
        if self._conexao is None:
            try:
                self._conexao = mysql.connector.connect(
                    host=self._host,
                    user=self._usuario,
                    password=self._senha,
                    database=self._banco_dados
                )
                self._cursor = self._conexao.cursor()
            except mysql.connector.Error as e:
                print("Erro de SQL:", e)
            except Exception as e:
                print("Erro:", e)

    def desconectar(self):
        if self._cursor:
            self._cursor.close()
        if self._conexao:
            self._conexao.close()
            self._conexao = None
            self._cursor = None

    def criarBancoDeDados(self, nome_bd):
        self.conectar()
        try:
            self._cursor.execute(f"DROP DATABASE IF EXISTS {nome_bd}")
            self._cursor.execute(f"CREATE DATABASE {nome_bd}")
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)

    def usarBancoDeDados(self, nome_bd):
        self.conectar()
        try:
            self._cursor.execute(f"USE {nome_bd}")
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)

    def manipular(self, sql):
        self.conectar()
        try:
            self._cursor.execute(sql)
            self._conexao.commit()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)

    def manipularComParametros(self, sql, parametros):
        self.conectar()
        try:
            self._cursor.execute(sql, parametros)
            self._conexao.commit()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)

    def consultar(self, sql):
        self.conectar()
        resultado = []
        try:
            self._cursor.execute(sql)
            resultado = self._cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)
        return resultado

    def consultarComParametros(self, sql, parametros):
        self.conectar()
        resultado = []
        try:
            self._cursor.execute(sql, parametros)
            resultado = self._cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)
        return resultado
