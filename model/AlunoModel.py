class AlunoModel:

  def __init__(self):
    self.__matricula = str
    self.__email = str
    self.__nome = str
    self.__genero=str
    self.__senha= str


  def setNome(self, nome):
    self.__nome = nome

  def setMatricula(self,matricula):
    self.__matricula = matricula
  
  def setEmail(self,email):
    self.__email=email

  def setGenero(self,genero):
    self.__genero = genero

  def setSenha(self,senha):
    self.__senha = senha

  def getNome(self):
    return self.__nome

  def getMatricula(self):
    return self.__matricula

  def getEmail(self):
    return self.__email 

  def getGenero(self):
    return self.__genero

  def getSenha(self):
    return self.__senha


  def getDados(self):
    todos = ""
    return todos


  def pegarDados(self):
     matricula = self.getMatricula()
     nome = self.getNome()
     email = self.getEmail()
     genero = self.getGenero()
     senha = self.getSenha()

     todos = matricula + nome + email+  genero + senha
     return todos

  def cadastrar(self):
    arq = open('model/tabela-aluno.txt','a')
    matricula = self.getMatricula()
    nome = self.getNome()
    email = self.getEmail()
    genero = self.getGenero()
    senha = self.getSenha()
    
    todos = matricula + ';' + nome + ';' + email + ';' +  genero + ';' + senha +'\n'
    
    arq.write(todos)
    arq.close()
    
    return 'Cadastro realizado com sucesso!'


  