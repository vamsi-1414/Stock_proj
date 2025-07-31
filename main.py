import time
import random
from stock_price_generator import StockPriceGenerator
from news_generator import NewsGenerator

def choose_sentiment():
    # Simulate sentiment trend
    return random.choices(
        ["positive", "negative", "neutral"],
        weights=[0.4, 0.3, 0.3],  # Adjust if needed
        k=1
    )[0]

def main():
    price_model = StockPriceGenerator(base_price=1500.0)
    news_model = NewsGenerator()

    for step in range(100):  # Number of time steps in simulation
        sentiment = choose_sentiment()
        price = price_model.update_price(sentiment)
        news = news_model.generate_news(sentiment)

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Price: ₹{price} | {sentiment.upper():<8} | News: {news}")

        time.sleep(0.5)  # Adjust the delay as needed (0.5 sec here)

if __name__ == "__main__":
    main()

