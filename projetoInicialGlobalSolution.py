# Gabriel Fossatti Beltran
# Gabriel Pescarolli Galiza
# Pedro Nogueira Garcez

import time
from colorama import init, Fore

init(autoreset=True)
def titulo():
    print(f"================-({Fore.LIGHTGREEN_EX}MENU{Fore.RESET})-================")

Lista_Cadastro = []

def cadastro(nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude, titular_convenio,
             email, telefone, contato_emergencia, tipo_sanguineo, alergias):

    cadastro_pessoa = (nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude,
                       titular_convenio, email, telefone, contato_emergencia, tipo_sanguineo, alergias)

    Lista_Cadastro.append(cadastro_pessoa)
    return f"{Fore.LIGHTGREEN_EX}Dados do Cadastro:{Fore.RESET}\n{Lista_Cadastro}"

def menu():
    while True:
        titulo()
        escolha_opcao=str(input(f"Escolha a funcionalidade que deseja:"
                                f"\n{Fore.LIGHTBLUE_EX}1.{Fore.RESET} Fazer Cadastro"
                                f"\n{Fore.LIGHTBLUE_EX}2.{Fore.RESET} Contato"
                                f"\n{Fore.LIGHTBLUE_EX}3.{Fore.RESET} Sair"
                                f"\nEscreva aqui: "))

        if escolha_opcao=='1' or escolha_opcao.lower()=="fazer cadastro":
            print(f"{Fore.LIGHTYELLOW_EX}Preencha os dados do cadastro abaixo:")

            nome = str(input("Nome: "))
            sobrenome = str(input("Sobrenome: "))
            data_de_nascimento = str(input("Data de Nascimento: "))
            cpf = str(input("CPF: "))
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

            cadastro(nome, sobrenome, data_de_nascimento, cpf, rg, convenio, nm_carteira, plano_saude, titular_convenio, email, telefone, contato_emergencia, tipo_sanguineo, alergias)

        elif escolha_opcao=='2' or escolha_opcao.lower()=="contato":
            print(f"Dúvidas? Entre em contato e fale com um de nossos especialistas: {Fore.LIGHTCYAN_EX}0800 015 3855.")
            time.sleep(0.65)

        elif escolha_opcao=='3' or escolha_opcao.lower()=="sair":
            print(f"{Fore.LIGHTRED_EX}Saindo...")
            time.sleep(0.45)
            exit()

        else:
            print("Valor Inválido, tente novamente.")

menu()
