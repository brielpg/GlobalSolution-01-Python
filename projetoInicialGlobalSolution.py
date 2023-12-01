# Gabriel Fossatti Beltran 552798
# Gabriel Pescarolli Galiza 554012
# Pedro Nogueira Garcez 553902

import time
from colorama import init, Fore

init(autoreset=True)
def titulo():
    print(f"================-({Fore.LIGHTGREEN_EX}MENU{Fore.RESET})-================")

lista_cadastro = []

def cadastrar(nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude, titular_convenio,
             email, telefone, contato_emergencia, tipo_sanguineo, alergias):

    cadastro_pessoa = (nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude,
                       titular_convenio, email, telefone, contato_emergencia, tipo_sanguineo, alergias)

    lista_cadastro.append(cadastro_pessoa)
    return f"{Fore.LIGHTGREEN_EX}Dados do Cadastro:{Fore.RESET}\n{lista_cadastro}"

def visualizar_dados_de_cadastro(cpf):
    for cadastro in lista_cadastro:
        if cadastro[3] == cpf:
            return cadastro
    return None

# validar se o cpf ja foi cadastrado
def cpf_ja_cadastrado(cpf):
    for cadastro in lista_cadastro:
        if cadastro[3] == cpf:
            return True
    return False

# fazendo o menu
def menu():
    while True:
        titulo()
        # deixando o usúario escolher a função que deseja
        escolha_opcao=str(input(f"Escolha a funcionalidade que deseja:"
                                f"\n{Fore.LIGHTBLUE_EX}1.{Fore.RESET} Fazer cadastro"
                                f"\n{Fore.LIGHTBLUE_EX}2.{Fore.RESET} Visualizar dados de cadastro"
                                f"\n{Fore.LIGHTBLUE_EX}3.{Fore.RESET} Contato"
                                f"\n{Fore.LIGHTBLUE_EX}4.{Fore.RESET} Sair"
                                f"\nEscreva aqui: "))
        
# caso ele escolha a primeira opção, pede todos os dados e salva em variaveis
        if escolha_opcao=='1' or escolha_opcao.lower()=="fazer cadastro":
            print(f"{Fore.LIGHTYELLOW_EX}Preencha os dados do cadastro abaixo:")

            nome = str(input("Nome: "))
            sobrenome = str(input("Sobrenome: "))
            data_de_nascimento = str(input("Data de Nascimento: "))
            cpf = str(input("CPF: "))
            if cpf_ja_cadastrado(cpf):
                print("Este CPF ja esta cadastrado")
                continue
            rg = str(input("RG: "))
            convenio = str(input("Convênio: "))
            nm_carteira = str(input("Número carteirinha do convênio: "))
            plano_saude = str(input("Plano de Saúde: "))
            titular_convenio = str(input("Titular: "))
            email = str(input("Email: "))
            telefone = str(input("Telefone: "))
            contato_emergencia = str(input("Contato para emergência: "))
            tipo_sanguineo = str(input("Tipo Sanguíneo: "))
            alergias = str(input("Tem alergia a algo? Se sim ao que: "))

            cadastrar(nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude, titular_convenio, email, telefone, contato_emergencia, tipo_sanguineo, alergias)

        #caso escolha a segunda função  ele ira vizualizar os dados
        elif escolha_opcao == '2' or escolha_opcao.lower() == "visualizar dados de cadastro":
            cpf = str(input("Insira o CPF do cadastrado: "))
            dados = visualizar_dados_de_cadastro(cpf)
            if dados is not None:
                print(dados)
            else:
                print("Nao ha usuario cadastrado com esse CPF")

        elif escolha_opcao=='3' or escolha_opcao.lower()=="contato":
            print(f"Dúvidas? Entre em contato e fale com um de nossos especialistas: {Fore.LIGHTCYAN_EX}0800 015 3855.")
            time.sleep(0.65)

        elif escolha_opcao=='4' or escolha_opcao.lower()=="sair":
            print(f"{Fore.LIGHTRED_EX}Saindo...")
            time.sleep(0.45)
            exit()

        else:
            print("Valor inválido, tente novamente.")

menu()
