import Funções, CalculoIMC
from time import sleep

hora = Funções.Funcao().hora()


# Criando a classe principal
class MeuAplicativo():
    def __init__(self):
        self.Hora_Atual = Funções.Funcao().hora()
        Mensagem_de_Alerta = Funções.Funcao().Alerta_Mensagem()
        self.horaatual = self.Hora_Atual
        self.horacalculo = self.Hora_Atual
        self.mensagem = Mensagem_de_Alerta
        self.continua = True
        return self.App()

    def App(self):
        return self.Peso()

    def Peso(self):
        print(self.Hora_Atual)
        print(self.mensagem[2])
        while True:
            self.peso = input("Digite o peso: ").upper()
            self.peso = Funções.Funcao().Tratar_Caracteres(self.peso)
            Voltar_Sair = Funções.Funcao().Sair_Voltar(self.peso)
            if Voltar_Sair == True:
                continue

            try:
                self.peso = float(self.peso)
                self.peso = Funções.Funcao().Tratar_Peso_Altura(self.peso, 600, 3, "Peso")
                try:
                    if str(self.peso[:3]) == "505":
                        print(f"{self.peso[4:]}")
                        continue
                except:
                    print(f"Peso: {str(self.peso)}")
                    return self.Altura()
                    break
            except ValueError:
                print(self.mensagem[0], self.mensagem[2])
                continue
            return self.Altura()

    def Altura(self):
        while True:
            self.altura = input("Digite uma altura: ").upper()
            self.altura = Funções.Funcao().Tratar_Caracteres(self.altura)
            Voltar_Sair = Funções.Funcao().Sair_Voltar(self.altura)
            if Voltar_Sair == True:
                continue

            try:
                self.altura = float(self.altura)
                self.altura = str(Funções.Funcao().Tratar_Peso_Altura(self.altura, 3, 2, "Altura"))
                if str(self.altura[:3]) == "505":
                    print(f"{self.altura[4:]}")
                    continue

                else:
                    print(f"Peso: {str(self.peso)}")
                    print(f"Altura: {str(self.altura)}")
                    CalculoIMC.Imc(self.peso, self.altura)
                    self.verificacao()
                    return False

            except ValueError:
                print("Altura incorreta, insira um valor válido\n Ex:\n   1,65 ou 1.65")

    def verificacao(self):
        sleep(4)
        print("Digite SIM para continuar ou NÃO para encerrar o programa...")
        pergunta = input("Deseja continuar? [SIM/NÃO]").upper()
        if pergunta[0] == "S":
            self.horaatualizada = Funções.Funcao().hora()
            self.horaatualizada = self.horaatualizada.replace(":", ".")
            self.horacalculo = self.horacalculo.replace(":", ".")
            total = float(self.horaatualizada[14:]) - float(self.horacalculo[14:])

            if total < 0.70:
                print("Voltando...")
                sleep(2)
                self.App()
                
            else:
                Funções.Funcao().Limpar_Tela()
                sleep(1)
                print("Voltando...")
                sleep(3)
                self.App()

        elif pergunta[0] == "N":
            sleep(1)
            print("Até mais")
            sleep(1)
            print("Finalizado com êxito!")
            Funções.Funcao().Interromper()


        else:
            """if nothing was understood the program go to begin automatcaly again
      """
            sleep(1)
            print("Não entendi, programa reiniciando automáticamente...")
            self.App()


try:
    # Funções.Funcao().Limpar_Tela()
    app = MeuAplicativo()

except KeyboardInterrupt:
    horaatualizada = Funções.Funcao().hora()
    horaatualizada = horaatualizada.replace(":", ".")
    hora = hora.replace(":", ".")
    total = float(horaatualizada[14:]) - float(hora[14:])
    if total < 6.0:
        pass
    else:

        print("Programa finalizado com sucesso!")

try:
    app.run()
except:
    pass
