def menu_pessoa():
    print("DIGITE A OPÇÃO ESCOLHIDA")
    print("1 - Cadastrar nome")
    print("2 - Deletar nome")
    print("3 - Entrar no aplicativo")


def cadastrar(pessoas, carteira, nome):
    carteira['nome'] = nome
    carteira['saldo'] = 0.00
    if carteira not in pessoas:
        pessoas.append(carteira)
        print(f" conta de {nome} adicionada")
    else:
        print("Ésta pessoa já possui uma carteira ")


def deletar(pessoas, carteira, nome):
    for pessoa in pessoas[:]:
        if pessoa.get('nome') == nome:
            carteira.remove(pessoa)
            print(f"cadastro de {nome} removido")
            break
        else:
            print("o nome nao esta na lista")
            continue


def login(pessoas, nome):
    for pessoa in pessoas[:]:
        if pessoa.get('nome') == nome:
            print(f"usuario logado como {nome}")
            return True
        else:
            print("Usuario não cadastrado")
            return False
