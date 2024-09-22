from time import sleep
#Definindo a função para realizar o calculo IMC
class Imc():
  #Starting the program according to the data received
  def __init__(self, peso, altura):
    self.peso = peso
    self.altura = altura
    self.Animacao()

  #Calculating IMC
  def Indice_De_Massa(self):

    #Here we are calculating the IMC and printing the
    #result to have a better undertanding of the user

    self.pesotratado = float(self.peso)
    self.alturatratado = float(self.altura)
    self.imc = self.pesotratado / (self.alturatratado * self.alturatratado)
    print(f"O peso informado foi {self.pesotratado:.2f}kg\nA altura informada foi {self.alturatratado}m")
    print(f"O Indice de massa corporal é: {self.imc:.2f}")
    sleep(1)
    lista = ["muito abaixo do peso!", "abaixo do peso!", "no peso normal!", "acima do peso!", "com obesidade nível 1!",
             "com obesidade nível 2 (Severa)!", "com obesidade nível 3 (Mórbida)!"]
    if self.imc < 17:
      print(f"O paciente está {lista[0]}")
    elif self.imc >= 17 and self.imc <= 18.49:
      print(f"O paciente está {lista[1]}")
    elif self.imc >=18.5 and self.imc<=24.99:
      print(f"O paciente está {lista[2]}")
    elif self.imc >= 25 and self.imc <= 29.99:
      print(f"O paciente está {lista[3]}")
    elif self.imc >= 30 and self.imc <= 34.99:
      print(f"O paciente está {lista[4]}")
    elif self.imc >= 35 and self.imc <= 39.99:
      print(f"O paciente está {lista[5]}")
    elif self.imc >40:
      print(f"O paciente está {lista[6]}")
    print("\n")
    print("=-="*12)
  #Exibindo o resultado formatado e mais dinâmico

  def Animacao(self):
    '''
    Animating to have a better user experience
    '''
    print("Carregando resultado", end="")
    for c in range(0,3):
      ponto = str('.')
      print(f'{ponto}', end="")
      ponto += str('.')
      sleep(0.5)
    print("\n")
    self.Indice_De_Massa()
