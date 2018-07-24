class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    def dar_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    def dar_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes


vingadores = Filme("Vingadores guerra infinita", 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')


serie = Serie("friends", 2018, 6)
serie.dar_likes()
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} - Likes: {serie.likes}')