class Player:
    def __init__(self, name: str, health: int = 100, level: int = 1):
        self.name = name
        self.health = health
        self.level = level

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)

    def heal(self, amount: int) -> None:
        self.health += amount

    def __str__(self) -> str:
        return f"{self.name} (Level {self.level}) - HP: {self.health}"
