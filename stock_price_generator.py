import random

class StockPriceGenerator:
    def __init__(self, base_price=1500.0):
        self.price = base_price

    def update_price(self, sentiment):
        drift = {"positive": 1.01, "negative": 0.99, "neutral": 1.0}
        noise = random.gauss(0, 0.005)  # small random fluctuation
        self.price *= drift[sentiment] + noise
        return round(self.price, 2)

