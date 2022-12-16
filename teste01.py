def gerarextrato(self):
    print(f"Numero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}")


def transferevalor(self, contadestino, valor):
    if self.saldo < valor:
        print("Saldo Insuficiente")
    else:
        contadestino.depositar(valor)
        self.saldo -= valor
        return "Tranferencia realizada"