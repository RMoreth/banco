import modulo
from time import sleep
if __name__ == "__main__":
    pessoas = []
    carteira = {}
    login = None
    while True:
        modulo.menu_pessoa()
        opcao = str(input(""))
        match opcao:
            case '1':
                print("cadastrar nome")
                nome = str(input("Digite o nome a ser adicionado"))
                modulo.cadastrar(pessoas, carteira, nome)
            case '2':
                print('Deletar nome')
                nome = str(input("Digite o nome a ser excuido"))
                modulo.deletar(pessoas, nome)
            case '3':
                print("Entrar no aplicativo")
                nome = str(input("Digite o nome do titular"))
                login = modulo.login(pessoas, nome)
                if login is False:
                    continue
                else:
                    while True:
                        print(f"conectado a conta de {nome}")
                        modulo.menu_carteira()
                        resp = str(input(""))
                        match resp:
                            case '1':
                                print(f"Saldo: R${carteira['saldo']}")
                            case '2':
                                print("Deposito")
                                valor = float(
                                    input("Deposite o valor desejado: "))
                                x = carteira['saldo'] + valor
                                carteira['saldo'] = x
                                print(f"o valor {valor} foi depositado")
                            case '3':
                                print("Saque")
                                valor = float(
                                    input("Saque o valor desejado: "))
                                x = carteira['saldo'] - valor
                                if x < 0:
                                    print("Saldo insuficiente")
                                else:
                                    carteira['saldo'] = x
                                    print(f"o valor {valor} foi sacado")

            case '4':
                print(f"carteira = {carteira}")
                print(f"pessoas = {pessoas}")

            case _:
                print("opção invalida")
                sleep(3)
                continue
