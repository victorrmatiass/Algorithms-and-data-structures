class Pasta:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.anterior = None
        self.proximo = None

class LinkedList:
    def __init__(self) -> None:
        self.inicio = None
        self.ultimo = None
        self.tamanho = 0

    def adicionar(self, pasta) -> None:
        if not self.inicio:
            self.inicio = pasta
            self.ultimo = pasta
        else:
            self.ultimo.proximo = pasta
            pasta.anterior = self.ultimo
            self.ultimo = pasta
        self.tamanho += 1

    def canonizar(self) -> None:
        pasta = self.inicio
        for i in range(self.tamanho):            
            if pasta.nome == "..":
                if pasta.anterior and pasta.anterior.anterior:
                    pasta.anterior.anterior.proximo = pasta.proximo
                    if pasta.proximo: pasta.proximo.anterior = pasta.anterior.anterior
                    self.tamanho -= 2
                else:
                    self.inicio = pasta.proximo
                    if pasta.proximo:
                        pasta.proximo.anterior = None
                    self.tamanho -= 1
            pasta = pasta.proximo
    
    def retornar_caminho(self) -> str:
        caminho_canonizado = '/'
        while self.inicio != None:
            if self.inicio.proximo:
                caminho_canonizado += self.inicio.nome + '/'
            else: caminho_canonizado += self.inicio.nome
            self.inicio = self.inicio.proximo
        return caminho_canonizado

def main():
    receber_entradas = True
    while receber_entradas:
        try:
            entrada = str(input())
        except EOFError:
            receber_entradas = False
        else:

            #Inicio do split
            pasta = ""
            lista_caminho = LinkedList()
            caractere_anterior = ""
            for i in range(len(entrada)):
                if i != 0:
                    if entrada[i] == "/":
                        if caractere_anterior == "/" or caractere_anterior == ".":
                            pass
                        else:
                            lista_caminho.adicionar(Pasta(pasta))
                            pasta = ""
                    elif entrada[i] == ".":
                        if caractere_anterior == ".":
                            lista_caminho.adicionar(Pasta(".."))
                    else:
                        pasta += entrada[i]
                        if i == len(entrada) - 1: lista_caminho.adicionar(Pasta(pasta))
                caractere_anterior = entrada[i]
            #Fim do Split

            lista_caminho.canonizar()
            caminho = lista_caminho.retornar_caminho()
            print(caminho)

if __name__ == '__main__':
    main()