import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mercado.settings')
django.setup()

from consultas.models import produto, pessoa, tipo_pessoa
from consultas.models.pessoa import senha_dono



# pessoa1 = pessoa.Pessoa(nome="Ana Silva", tipo= tipo_pessoa.Tipo_pessoa.CLIENTE, cpf="123.456.789-00")
# pessoa1.save()
#
# pessoa2 = pessoa.Pessoa(nome="João Souza", tipo= tipo_pessoa.Tipo_pessoa.CLIENTE, cpf="987.654.321-00")
# pessoa2.save()
#
# pessoa3 = pessoa.Pessoa(nome="Maria Oliveira", tipo= tipo_pessoa.Tipo_pessoa.FUNCIONARIO, cpf="456.789.123-00")
# pessoa3.save()
#
# pessoa4 = pessoa.Pessoa(nome="Carlos Pereira", tipo=tipo_pessoa.Tipo_pessoa.FUNCIONARIO, cpf="321.654.987-00")
# pessoa4.save()
#
# pessoa5 = pessoa.Pessoa(nome="Gerson Luiz", tipo=tipo_pessoa.Tipo_pessoa.DONO, cpf="853.654.123-00")
# pessoa5.save()
#
#
# produto1 = produto.Produto(nome="Picanha", tipo="Carne", preco=20.00, estoque=100)
# produto1.save()
#
# produto2 = produto.Produto(nome="Del Vale", tipo="Suco", preco=8.50, estoque=50)
# produto2.save()
#
# produto3 = produto.Produto(nome="Coca-cola", tipo="Refrigerante", preco=5.00, estoque=200)
# produto3.save()
#
# produto4 = produto.Produto(nome="Polar", tipo="Cerveja", preco=10.00, estoque=150)
# produto4.save()



def main():
    while True:
        print("\nMenu:")
        print("1. Listar produtos")
        print("2. Buscar produto por nome")
        print("3. Buscar produto por tipo")
        print("4. Cadastrar produto")
        print("5. Excluir produto")
        print("6. Alterar valor de produto")
        print("7. Alterar estoque de produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produto.listar_produtos()
        elif opcao == '2':
            nome = input("Digite o nome do produto: ")
            produto.buscar_produto_nome(nome)
        elif opcao == '3':
            tipo = input("Digite o tipo do produto: ")
            produto.buscar_produto_tipo(tipo)
        elif opcao == '4':
            senha = input("Digite o senha do priprietário: ")
            if senha == senha_dono:
                nome = input("Digite o nome do produto: ")
                while True:
                    try:
                        preco = float(input("Digite o preço do produto: "))
                        break
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido para o preço.")
                while True:
                    try:
                        estoque = int(input("Digite o estoque do produto: "))
                        break
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido para o estoque.")
                tipo = input("Digite o tipo do produto: ")
                produto.cadastrar_produto(nome, preco, estoque, tipo)
            else:
                input("Você não tem permissão para executar essa operação!")
        elif opcao == '5':
            senha = input("Digite o senha do priprietário: ")
            if senha == senha_dono:
                while True:
                    try:
                        codigo = int(input("Digite o ID do produto a ser excluído: "))
                        produto.excluir_produto(codigo)
                        break
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido.")
            else:
                input("Você não tem permissão para executar essa operação!")
        elif opcao == '6':
            senha = input("Digite o senha do priprietário: ")
            if senha == senha_dono:
                while True:
                    try:
                        codigo = int(input("Digite o ID do produto: "))
                        break
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido.")
                while True:
                    try:
                        novo_preco = float(input("Digite o novo preço do produto: "))
                        break  #
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido.")
                produto.alterar_valor_produto(codigo, novo_preco)
            else:
                input("Você não tem permissão para executar essa operação!")
        elif opcao == '7':
            senha = input("Digite o senha do priprietário: ")
            if senha == senha_dono:
                while True:
                    try:
                        codigo = int(input("Digite o ID do produto: "))
                        break  # Sai do loop se a entrada for válida
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido.")
                while True:
                    try:
                        novo_estoque = int(input("Digite o novo estoque do produto: "))
                        break
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número válido.")
                produto.alterar_estoque_produto(codigo, novo_estoque)
            else:
                input("Você não tem permissão para executar essa operação!")
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()