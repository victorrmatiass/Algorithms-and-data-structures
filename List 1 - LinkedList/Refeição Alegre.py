#Classe do cliente onde contem o valor que vai gastar e o cliente atras dele
class Cliente:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.anterior = None

#Classe da lista encadeada, cada guiche tera uma lista onde sabemos quem e o primeiro e o ultimo
class LinkedList:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, cliente) -> None:
        if not self.primeiro:
            self.primeiro = cliente
            self.ultimo = cliente
        else:
            self.ultimo.anterior = cliente
            self.ultimo = cliente

    def remover(self) -> None:
        if not self.primeiro:
            return "Fila vazia"
        else:
            self.primeiro = self.primeiro.anterior

    def valor_perdido(self) -> int:
        if self.primeiro:
            Valor_perdido = self.primeiro.valor
            while self.primeiro.anterior != None:
                Valor_perdido += self.primeiro.anterior.valor
                self.primeiro = self.primeiro.anterior
            return Valor_perdido
        else: return 0

def main():
    #Criacao de uma fila para cada caixa/guiche
    Guiche1 = LinkedList()
    Guiche2 = LinkedList()
    Guiche3 = LinkedList()

    #Flag que vai manter o loop ate nao receber mais entradas
    receber_entradas = True

    while receber_entradas:
        try:
            entrada = str(input()).split()
        except EOFError:
            receber_entradas = False
        else:
            if entrada[0] == "PROXIMO":
                if entrada[1] == "1":
                    Guiche1.remover()

                elif entrada[1] == "2":
                    Guiche2.remover()
                
                else:
                    Guiche3.remover()

            else:
                if entrada[0] == "1":
                    Guiche1.adicionar(Cliente(int(entrada[1])))

                elif entrada[0] == "2":
                    Guiche2.adicionar(Cliente(int(entrada[1])))

                else:
                    Guiche3.adicionar(Cliente(int(entrada[1])))

    #Depois do ultimo ciclo do while, vamos printar o valor perdido por cada caixa/guiche.
    else:
        print("Caixa 1: {}".format(Guiche1.valor_perdido()))
        print("Caixa 2: {}".format(Guiche2.valor_perdido()))
        print("Caixa 3: {}".format(Guiche3.valor_perdido()))

if __name__ == '__main__':
    main()