from colorama import Fore

menu = Fore.CYAN + r"""
============================================================= PyBANK ============================================================================
=                                         _____               _____                        __                           ____                    =
=                                       /       \           /       \                     /  |                        /      \                  =
=             [d] Depositar             $$$$$$$  | __    __ $$$$$$$  |   ____     _____   $$ |   __        __     __ /$$$$$$  |                 =
=             [s] Sacar                 $$ |__$$ |/  |  /  |$$ |__$$ | /      \ /       \ $$ |  /  |      /  \   /  |$$____$$ |                 =
=             [e] Extrato               $$    $$/ $$ |  $$ |$$    $$<  $$$$$$  |$$$$$$$  |$$ |_/$$/       $$  \ /$$/  /    $$/                  =   
=             [nc] Nova conta           $$$$$$$/  $$ |  $$ |$$$$$$$  | /    $$ |$$ |  $$ |$$   $$<         $$  /$$/  /$$$$$$/                   =
=             [lc] listar contas        $$ |      $$ \__$$ |$$ |__$$ |/$$$$$$$ |$$ |  $$ |$$$$$$  \         $$ $$/   $$ |_____                  =
=             [nu] Novo Usuario         $$ |      $$    $$ |$$    $$/ $$    $$ |$$ |  $$ |$$ | $$  |         $$$/    $$       |                 =
=             [q] Sair                  $$/        $$$$$$$ |$$$$$$$/   $$$$$$$/ $$/   $$/ $$/   $$/           $/     $$$$$$$$/                  =
=                                                 /  \__$$ |                                                                                    =
=                                                 $$    $$/                                                                                     =
=                                                  $$$$$$/                                                                                      =
=================================================================================================================================================
=> """ + Fore.RESET


class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.AGENCIA = "0001"
        self.usuarios = []
        self.contas = []
        self.main()

    def novo_usuario(self):
        cpf = input("CPF (somente números): ")
        usuario = self.filtrar_usuario(cpf, self.usuarios)

        if usuario:
            print("Já existe usuário com esse CPF!")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (Logradouro, nro, - bairro - cidade/sigla estado): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print(Fore.GREEN + "Usuário Criado com sucesso!" + Fore.RESET)
        self.main()

    def criar_conta(self,  numero_conta):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf, self.usuarios)

        if usuario:
            print(Fore.LIGHTCYAN_EX + "Conta criada com sucesso! " + Fore.RESET)
            return {"agencia": self.AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    @staticmethod
    def filtrar_usuario(cpf, usuarios):
        # percorre cada dicionário usuario na lista usuarios e verifica se o cpf é igual ao cpf fornecido.
        # Se for igual, esse usuário é adicionado à lista usuarios_filtrados.
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
            Agência:       {conta['agencia']}
            C/C            {conta['numero_conta']}
            Titular:       {conta['usuario']['nome']}"""
            print(linha)

    def deposito(self, valor, /):
        # verificando se o valor é negativo
        if valor < 0:
            print(Fore.RED + "Não é possivel depositar um valor negativo" + Fore.RESET)

        # se não for negativo então ele será depositado na conta
        else:
            self.saldo += valor
            valor = f"{valor:.2f}"
            print(Fore.LIGHTGREEN_EX + "Deposito feito com sucesso!!" + Fore.RESET)

    def saque(self, *, valor):

        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print(Fore.RED + "Operação falhou! Você não tem saldo suficiente." + Fore.RESET)

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    def imprimir_extrato(self, saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def main(self):

        opcao = input(menu)

        if opcao == "d":
            opc = ''
            dps = 0
            while opc != "n":
                print(Fore.LIGHTBLUE_EX + f"\n{f' Deposito {dps + 1} ':=^20}", Fore.RESET)

                valor = float(input("Valor do deposito: "))
                self.deposito(valor)
                dps += 1
                opc = input("Deseja continuar [S/N]? ")[0].lower()

            self.main()

        elif opcao == "s":
            opc = ''
            while opc != "n":
                print(Fore.LIGHTCYAN_EX + f"\n{f' Saque {self.numero_saques + 1} ':=^20}", Fore.RESET)
                valor = float(input("Informe o valor do saque: "))
                self.saque(valor=valor)
                opc = input("Deseja continuar [S/N]? ")[0].lower()
            self.main()

        elif opcao == "nu":
            self.novo_usuario()

        elif opcao == 'lc':
            self.listar_contas()
            self.main()

        elif opcao == "nc":
            numero_conta = len(self.contas) + 1
            conta = self.criar_conta(numero_conta)
            if conta:
                self.contas.append(conta)
            self.main()

        elif opcao == "e":
            self.imprimir_extrato(self.saldo, extrato=self.extrato)

        elif opcao == "q":
            exit()


banco = Banco()
