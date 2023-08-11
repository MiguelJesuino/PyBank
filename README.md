# PyBank


						 _______             _______                       __       
						/       \           /       \                     /  |      
						$$$$$$$  | __    __ $$$$$$$  |  ______   _______  $$ |   __ 
						$$ |__$$ |/  |  /  |$$ |__$$ | /      \ /       \ $$ |  /  |
						$$    $$/ $$ |  $$ |$$    $$<  $$$$$$  |$$$$$$$  |$$ |_/$$/ 
						$$$$$$$/  $$ |  $$ |$$$$$$$  | /    $$ |$$ |  $$ |$$   $$<  
						$$ |      $$ \__$$ |$$ |__$$ |/$$$$$$$ |$$ |  $$ |$$$$$$  \ 
						$$ |      $$    $$ |$$    $$/ $$    $$ |$$ |  $$ |$$ | $$  |
						$$/        $$$$$$$ |$$$$$$$/   $$$$$$$/ $$/   $$/ $$/   $$/ 
							  /  \__$$ |                                        
							  $$    $$/                                         
							   $$$$$$/
														     

Um projeto desenvolvido como parte do Desafio Prático no bootcamp Potência Tech powered by iFood da DIO. O PyBank é uma simulação de sistema bancário que permite operações de depósito, saque e exibição de extrato.

## Funcionalidades

- **Depósito:** Permite depositar valores positivos na conta bancária.
- **Saque:** Permite realizar até 3 saques diários, cada um com um limite máximo de R$ 500,00.
- **Extrato:** Exibe o histórico de depósitos e saques.

## Como Usar

1. Clone este repositório.
2. Execute o arquivo principal do projeto (por exemplo, `main.py`).
3. Siga as instruções no console para realizar operações.

## Exemplo de Código

Aqui está um exemplo de como fazer um depósito:

```python
def deposito(self):
    depositos = []
    opc = ""
    dps = 0
    while opc != "n":
        print(Fore.LIGHTBLUE_EX + f"\n{f' Deposito {dps + 1} ':=^20}", Fore.RESET)
        lista = []

        valor = float(input("Valor do deposito: "))

        # verificando se o valor é negativo
        if valor < 0:
            print(Fore.RED + "Não é possivel depositar um valor negativo" + Fore.RESET)

        # se não for negativo então ele sera depositado na conta
        else:
            self.conta += valor
            valor = f"{valor:.2f}"
            lista.append(valor)
            depositos.append(lista[:])
            dps += 1

            print(Fore.LIGHTGREEN_EX + "Deposito feito com sucesso!!" + Fore.RESET)

            ver_depositos = input("Deseja ver os depositos[S/N]? ")[0].lower()
            if ver_depositos == "s":
                print(Fore.BLUE + f'{depositos}' + Fore.RESET)

        opc = input("Deseja continuar [S/N]? ")[0].lower()
```

## Dependências
Nenhuma dependência externa é necessária.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request.

Licença
Este projeto está sob a Licença MIT.
