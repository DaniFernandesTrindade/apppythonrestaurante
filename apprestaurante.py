class PedidoRestaurante:
    def _init_(self, cliente, mesa):
        self.cliente = cliente
        self.mesa = mesa
        self.itens = []
        self.total = 0.0

    def adicionar_item(self, nome_item, preco):
        self.itens.append((nome_item, preco))
        self.total += preco
        print(f"Item '{nome_item}' adicionado por R${preco:.2f}.")

    def ver_pedido(self):
        if not self.itens:
            print(" Nenhum item no pedido ainda.")
            return
        print(f"\n Pedido de {self.cliente} - Mesa {self.mesa}")
        for nome, preco in self.itens:
            print(f" - {nome}: R${preco:.2f}")
        print(f" Total até agora: R${self.total:.2f}\n")

    def fechar_conta(self):
        print(f"\n Conta final de {self.cliente} - Mesa {self.mesa}")
        for nome, preco in self.itens:
            print(f" - {nome}: R${preco:.2f}")
        print(f" Total a pagar: R${self.total:.2f}")
        print("Obrigada pela preferência!\n")


def menu_restaurante():
    cardapio = {
        1: ("Sushi", 32.50),
        2: ("Temaki", 25.00),
        3: ("Guioza", 18.00),
        4: ("Yakissoba", 28.00),
        5: ("Refrigerante", 6.00),
        6: ("Água", 4.00)
    }

    print(" Bem-vindo ao Restaurante Katsu-ya!")
    cliente = input("Digite o nome do cliente: ")
    mesa = input("Digite o número da mesa: ")

    pedido = PedidoRestaurante(cliente, mesa)

    while True:
        print("\n Menu:")
        for codigo, (item, preco) in cardapio.items():
            print(f"{codigo} - {item} (R${preco:.2f})")
        print("7 - Ver pedido")
        print("8 - Fechar conta")
        print("0 - Sair sem fechar conta")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Opção inválida. Tente novamente.")
            continue

        if opcao in cardapio:
            nome_item, preco = cardapio[opcao]
            pedido.adicionar_item(nome_item, preco)
        elif opcao == 7:
            pedido.ver_pedido()
        elif opcao == 8:
            pedido.fechar_conta()
            break
        elif opcao == 0:
            print(" Saindo sem finalizar o pedido.")
            break
        else:
            print(" Opção inválida. Tente novamente.")

menu_restaurante()
