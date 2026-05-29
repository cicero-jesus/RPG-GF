from modules import Player, Dado

class Warrior(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.strength = 20

    def attack(self, target: Player) -> None:
        dado = Dado(0)
        dado.jogar_dado()

        dano = dado.valor + self.strength
        target.take_damage(dano)

        print(f"{self.name} atacou {target.name} causando {dano} de dano!")
        print(dado)