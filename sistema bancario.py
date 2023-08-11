from colorama import Fore


class Banco:
    def __init__(self):
        self.conta = 0
        self.main()

    def deposito(self):
        self.conta = 0
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
        self.main()

    def saque(self):
        saques = list()
        qtd_saques = 0
        opc = ""

        # enquanto a opção for continuar o looping será efetuado
        while opc != "n":
            print(Fore.LIGHTCYAN_EX + f"\n{f' Saque {qtd_saques + 1} ':=^20}", Fore.RESET)
            lista = []

            valor = int(input("Quanto deseja sacar? "))

            # verificando se pode sacar a partir do total de saques ja realizados e valor do saque
            if qtd_saques <= 3 and valor < self.conta:
                if valor <= 500:
                    print(Fore.LIGHTGREEN_EX + "Saque feito com sucesso!!!" + Fore.RESET)
                    qtd_saques += 1
                    self.conta -= valor
                    valor = f"{valor:.2f}"
                    lista.append(valor)
                    saques.append(lista[:])
                    
                else:
                    print(Fore.RED + "Não foi possivel sacar o valor pois ele escede o limite", Fore.RESET)

            else:
                print(Fore.RED + "Não foi possivel sacar o valor pois ele escede o limite", Fore.RESET)
                ver_saque = input("Deseja ver os Saques [S/N]? ")[0].lower()

                if ver_saque == "s":
                    print(Fore.BLUE + f'{saques}' + Fore.RESET)

            opc = input("Deseja continuar [S/N]? ")[0].lower()
        self.main()

    def main(self):
        print("============================================================= PyBANK ============================================================")
        print("=            [1] Deposito                                                                                                        ")
        print("=            [2] Saque                                                                                                           ")
        print("=            [3] Sair                                                                                                            ")
        print(f"=                                                     Valor na conta {self.conta}                                               ")
        print("=================================================================================================================================")

        escolha = int(input("escolha sua opção: "))
        if escolha == 1:
            self.deposito()
        elif escolha == 2:
            self.saque()
        else:
            exit()


banco = Banco()
