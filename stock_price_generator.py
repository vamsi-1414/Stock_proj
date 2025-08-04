iimport random

class StockPriceGenerator:
    def __init__(self, base_price=1500.0):
        self.price = base_price
        self.tick_count = 0
        self.trend = "up"  # Current trend: up, down, flat
        self.trend_duration = random.randint(50, 100)
        self.volatility = 0.002  # Will change per trend

    def _switch_trend(self):
        self.trend = random.choice(["up", "down", "flat"])
        self.trend_duration = random.randint(50, 100)
        if self.trend == "up":
            self.volatility = random.uniform(0.002, 0.004)
        elif self.trend == "down":
            self.volatility = random.uniform(0.002, 0.004)
        else:  # flat
            self.volatility = random.uniform(0.0005, 0.0015)

    def update_price(self, sentiment):
        self.tick_count += 1

        # Switch trend when current one expires
        if self.tick_count % self.trend_duration == 0:
            self._switch_trend()

        # Base drift per trend
        if self.trend == "up":
            drift = 1.0008  # slight upward push
        elif self.trend == "down":
            drift = 0.9992  # slight downward push
        else:  # flat
            drift = 1.0

        # Sentiment modifier (small)
        sentiment_drift = {
            "positive": 0.0005,
            "negative": -0.0005,
            "neutral": 0
        }[sentiment]

        # Noise: random fluctuation
        noise = random.gauss(0, self.volatility)

        # Final price change
        change_factor = drift + sentiment_drift + noise
        self.price *= max(0.98, min(1.02, change_factor))  # clamp swing to ±2%

        return round(self.price, 2)

