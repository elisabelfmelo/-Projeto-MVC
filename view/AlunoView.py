from view.Tkfull import Janela
from controller.controller import AlunoController

class AlunoView:
  
  titulo= [[None,{'Cadastro De Aluno \n':'assets/imagens/aluna.png'}]]
  campo = [[None,''],
           [None,'Matrícula:',input],
           [None,'Nome:',input],
           [None,'Email:',input],
           [None,'Gênero:',('feminino','masculino')],
           [None,'Senha',complex], [''],
        [None,None,{'*Cadastrar':'assets/imagens/registro.png'}],[''],[None,None,'*Sair']]

  def __init__(self):
   self.jan = Janela()
   self.jan.gerar(self.titulo)
   self.jan.gerar(self.campo)
   self.jan.setEvento(14,self.evento)
   self.jan.setEvento(16,self.sair)
   self.jan.start()

  def evento(self):
    funcao = AlunoController()
    msg = funcao.pegarDados(self.jan)
    self.jan.mensagem(msg)

  def sair(self):
    self.jan.fechar()
  

