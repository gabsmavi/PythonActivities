class Funcionario:
    ht = 0
    hm = 8  # hora minima
    he = 30  # horas extras
    hf = 12.5  # horas fixas
    hs = 0  # horas sobra
    ferias = 360  # horas férias

    def __init__(self, cpf, nome, senha, hora1, hora2):
        self.cpf = cpf
        self.senha = senha
        self.h1 = hora1
        self.h2 = hora2
        self.ht = (self.h2 - self.h1)
        self.hm = 8
        self.he = 20
        self.nome = nome
        self.hs = (self.ht - self.hm)
        self.hf = 12.5
        self.f = 360
        self.pm = 2400

    # DEF: Análise das Horas

    def analisehoras(self):
        if self.ht > self.hm:
            print(f"Você possui {self.hs:.2f} horas extras.")
        elif self.ht < self.hm:
            dv = self.hm - self.ht
            print(f"Você está devendo {dv:.2f} de horas fixas.")

    def analiseextra(self):
        opcao = True
        while opcao:
            if self.hs > 0:
                print(f"Você pode converter suas {self.hs:.2f} horas em folga ou bônus")
                opcao2 = input("Digite a sua escolha: ")
                match opcao2:
                    case "bônus":
                        print(f"Você tem direito a ${self.hs * self.he} reais de valor bônus")
                        opcao = False
                    case "férias":
                        print(f"Você tem direito a {self.hs:.2f} horas de folga.")
                        opcao = False
            else:
                print(f"Você não tem horas extras.")
                break

    def analisemenos(self):
        opcao = True
        while opcao:
            if self.hs < 0:
                print(f"Você está devendo {self.hs:.2f} horas. Essas horas podem ser "
                      f"retiradas das suas férias ou descontadas do salário")
                opcao2 = input("Digite a sua escolha: ")
                match opcao2:
                    case "férias":
                        print(f"Você irá retirar {self.hs:.2f} das suas férias. Lhe restarão "
                              f"{self.f - self.hs} horas.")
                        opcao = False
                    case "salário":
                        print(f"Você irá retirar {self.hs:.2f} horas de seu pagamento mensal. Com o desconto,"
                              f"seu pagamento mensal será ${self.pm + (self.hs * self.hf):.2f} reais")
                        opcao = False
            else:
                print(f"Você não tem horas faltantes.")
                break


# Criação do funcionário
Funcionario1 = Funcionario(cpf=int(input("Digite seu CPF: \n")),
                           senha=(input("Digite sua senha: \n")),
                           hora1=float(input("Digite sua hora de entrada: \n")),
                           hora2=float(input("Digite sua hora de saída: \n")),
                           nome=input("Digite seu nome: \n"))

# Balanço de Horas

print(f'Funcionário, {Funcionario1.nome}')
Funcionario1.analisehoras()
print('\n')

print(f'{Funcionario1.nome},')
Funcionario1.analiseextra()
print('\n')

print(f'{Funcionario1.nome},')
Funcionario1.analisemenos()
print('\n')

# # Criação da Conta2
# Conta2 = Conta(342323232, 1234234232, 'Mateus', 3000)
#
# # Extratos
# print('Conta1')
# Conta1.gerarextrato()
# print('\n')
#
# print('Conta2')
# Conta2.gerarextrato()
# print()
#
# # Realizando transferência
#
# Conta1.transferevalor(Conta2, 2000)
#
# # Verificando se o saldo da Conta1 foi diminuido
# print('Conta1 após transferir 2000 para a Conta2')
# Conta1.gerarextrato()
