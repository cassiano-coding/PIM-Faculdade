import os
import time
import webbrowser
from datetime import datetime

# Dicionário para armazenar os usuários e seus cursos concluídos
usuarios = {}
cursos_concluidos = {}

# URLs dos vídeos dos cursos
videos_cursos = {
    "1": "https://www.youtube.com/watch?v=9fNHAD7ZDL4&list=PL-QAz5R5Rlm7wn20xLTIr84gbS2XkzqEZ",  # Introdução à Informática
    "2": "https://www.youtube.com/watch?v=p_SZ7L1R2qg&list=PL3bIgPf3B5vjbJk28rdBywHCHbE1ydMRT",  # Navegação em Redes Sociais
    "3": "https://www.youtube.com/watch?v=xQf53cj33PY&list=PLxNM4ef1Bpxj2_IG3rboXJBSCTxPlESBU"   # Informática para Negócios
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    limpar_tela()
    print("=== GERAÇÃO SABER CURSOS ONLINE ===")
    print("1. Cadastrar")
    print("2. Login")
    print("3. Sair")
    return input("Escolha uma opção: ")

def cadastrar_usuario():
    limpar_tela()
    print("=== CADASTRO DE USUÁRIO ===")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    #verifica se o usuario ja existe
    if nome in usuarios:
        print("Usuário já existe!")
        time.sleep(2)
        return False
    
    usuarios[nome] = senha
    cursos_concluidos[nome] = []
    print("Cadastro realizado com sucesso!")
    time.sleep(2)
    return True

def fazer_login():
    limpar_tela()
    print("=== LOGIN ===")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    
    if nome in usuarios and usuarios[nome] == senha:
        print(f"Bem-vindo(a), {nome}!")
        time.sleep(2)
        return nome
    else:
        print("Usuário ou senha incorretos!")
        time.sleep(2)
        return None
#menu de cursos
def menu_cursos(usuario):
    while True:
        limpar_tela()
        print(f"=== CURSOS - {usuario} ===")
        print("1. Introdução à Informática")
        print("2. Navegação em Redes Sociais")
        print("3. Informática para Negócios")
        print("4. Voltar")
        
        opcao = input("Escolha um curso (1-4): ")
        
        if opcao == "4":
            break
        #verifica se o usuario ja concluiu o curso
        if opcao in ["1", "2", "3"]:
            if opcao in cursos_concluidos[usuario]:
                print("Você já concluiu este curso!")
                time.sleep(2)
                continue
        #menu de cursos
            while True:
                limpar_tela()
                print(f"=== CURSO {opcao} ===")
                print("1. Assistir aula")
                print("2. Concluir curso")
                print("3. Voltar")
                
                escolha = input("O que deseja fazer? (1-3): ")
                
                if escolha == "1":
                    webbrowser.open(videos_cursos[opcao])
                elif escolha == "2":
                    cursos_concluidos[usuario].append(opcao)
                    print("Curso concluído com sucesso!")
                    time.sleep(2)
                    
                    # Verifica se todos os cursos foram concluídos
                    if len(cursos_concluidos[usuario]) == 3:
                        limpar_tela()
                        print("🎉 PARABÉNS! 🎉")
                        print("🎆 Você concluiu todos os cursos! 🎆")
                        print("🎊 Muito bem! 🎊")
                        time.sleep(5)
                        return
                    break
                elif escolha == "3":
                    break

def main():
    while True:
        opcao = menu_principal()
        #cadastro de usuario
        if opcao == "1":
            cadastrar_usuario()
        #login
        elif opcao == "2":
            usuario = fazer_login()
            if usuario:
                menu_cursos(usuario)
        elif opcao == "3":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção inválida!")
            time.sleep(2)

if __name__ == "__main__":
    main() 
