from random import randint

class Dado:
  def __init__(self, valor):
    self.valor = valor

  def jogar_dado(self): 
     self.valor = randint(1, 20)

  def __str__ (self):
    return f"O valor do dado foi: {self.valor}" 
