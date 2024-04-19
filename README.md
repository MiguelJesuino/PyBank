# PyBank
		  _____               _____                        __                          _____  
		/       \           /       \                     /  |                        /      \ 
		$$$$$$$  | __    __ $$$$$$$  |  ______   _______  $$ |   __        __     __ /$$$$$$  |
		$$ |__$$ |/  |  /  |$$ |__$$ | /      \ /       \ $$ |  /  |      /  \   /  |$$____$$ |
		$$    $$/ $$ |  $$ |$$    $$<  $$$$$$  |$$$$$$$  |$$ |_/$$/       $$  \ /$$/  /    $$/ 
		$$$$$$$/  $$ |  $$ |$$$$$$$  | /    $$ |$$ |  $$ |$$   $$<         $$  /$$/  /$$$$$$/  
		$$ |      $$ \__$$ |$$ |__$$ |/$$$$$$$ |$$ |  $$ |$$$$$$  \         $$ $$/   $$ |_____ 
		$$ |      $$    $$ |$$    $$/ $$    $$ |$$ |  $$ |$$ | $$  |         $$$/    $$       |
		$$/        $$$$$$$ |$$$$$$$/   $$$$$$$/ $$/   $$/ $$/   $$/           $/     $$$$$$$$/ 
			  /  \__$$ |                                                                   
			  $$    $$/                                                                    
			   $$$$$$/

PyBank é um simulador de sistema bancário desenvolvido como parte do Desafio Prático no bootcamp Potência Tech powered by iFood da DIO. O PyBank permite operações de depósito, saque, exibição de extrato, criação de contas e gerenciamento de usuários.

## Funcionalidades

-  **Depósito:** Permite depositar valores positivos na conta bancária. A função de depósito foi implementada para receber os argumentos apenas por posição (position only). 
-  **Saque:** Permite realizar saques com limite diário de R$ 500,00 e limite de 3 saques. A função de saque foi implementada para receber os argumentos apenas por chave (key only). 
-  **Extrato:** Exibe o histórico de transações, incluindo depósitos e saques. A função de exibir o extrato foi implementada para receber um argumento por posição e outro por chave.
-  **Nova conta:** Permite criar novas contas associadas a usuários existentes. 
-  **Listar contas:** Exibe as informações básicas das contas existentes. 
-  **Novo Usuário:** Permite criar novos usuários para associar a contas.
-  **Sair:** Encerra o programa.

## Pré-requisitos

- Python 3.11
- Biblioteca `colorama` (pode ser instalada via `pip install colorama`)

## Como Usar

1. Clone este repositório ou faça o download do código-fonte.
2. Certifique-se de ter o Python 3.11 instalado.
3. Instale a biblioteca `colorama` usando o comando `pip install colorama`.
4. Execute o arquivo `PybankV2.py` com o comando `python3 PybankV2.py`

## Contribuições

Este pequeno projeto foi desenvolvido para fins didáticos, como uma atividade de um curso. Sinta-se à vontade para acrescentar ideias ou fazer modificações.

## Licença

Este projeto está sob a [Licença MIT](https://opensource.org/licenses/MIT).

----------

Desenvolvido por [MiguelJesuino](https://github.com/MiguelJesuino/).
