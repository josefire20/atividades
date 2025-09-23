# Exceção personalizada para número ímpar
class NumeroImparError(Exception):
    pass

def verificar_par():
    """Exercício 1: Verifica se o número digitado é par"""
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 != 0:
            raise NumeroImparError("Erro: O número digitado é ímpar!")
        print(f"O número {numero} é par!")
    except NumeroImparError as e:
        print(e)
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido!")
    finally:
        print("Execução finalizada (verificação de paridade).\n")


def dividir_por_numero():
    """Exercício 2: Divide 10 pelo número digitado"""
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero == 0:
            raise ZeroDivisionError("Erro: Não é possível dividir por zero!")
        resultado = 10 / numero
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Erro: O valor digitado não é um número inteiro válido!")
    finally:
        print("Execução finalizada (divisão).\n")


# -------- Programa Principal --------
while True:
    print("=== MENU ===")
    print("1 - Verificar se o número é par")
    print("2 - Dividir 10 pelo número digitado")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        verificar_par()
    elif opcao == "2":
        dividir_por_numero()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!\n")
