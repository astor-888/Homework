class CashRegister:
    def __init__(self):
        self.money = 0

    def top_up(self, X):
        self.money += X

    def count_1000(self):
        return self.money // 1000

    def take_away(self, X):
        if X > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= X