from model.AlunoModel import AlunoModel

class AlunoController:

    def __init__(self):
        pass

    def pegarDados(self, AlunoView):
       matricula = AlunoView.getTexto(4)
       nome = AlunoView.getTexto(6)
       email = AlunoView.getTexto(8)
       genero = AlunoView.getTexto(10)
       senha = AlunoView.getTexto(12)

       funcao = AlunoModel()
       funcao.setMatricula(matricula)
       funcao.setNome(nome)
       funcao.setEmail(email)
       funcao.setGenero(genero)
       funcao.setSenha(senha)
       return funcao.cadastrar()