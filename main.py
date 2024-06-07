import os
import modulo

if __name__ == "__main__":
    pessoas = []
    carteira = {}
    login = None
    while True:
        modulo.menu_pessoa()
        opcao = str(input("escolha a opção desejada: "))
        match opcao:
            case '1':
                print("cadastrar nome")
                nome = str(input("Digite o nome a ser adicionado"))
                modulo.cadastrar(pessoas, carteira, nome)
            case '2':
                print('Deletar nome')
                nome = str(input("Digite o nome a ser excuido"))
                modulo.deletar(pessoas, carteira, nome)
            case '3':
                print("Entrar no aplicativo")
                nome = str(input("Digite o nome do titular"))
                login = modulo.login(pessoas, nome)
                if login is False:
                    continue
                else:
                    break
            case _:
                print("opção invalida")
                continue
    
                   