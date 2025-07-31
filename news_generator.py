import random

class NewsGenerator:
    def __init__(self):
        self.templates = {
            "positive": [
                "Infosys secures a multi-billion dollar deal with US client",
                "Infosys to expand operations and hire 10,000 new employees",
                "Strong Q2 results push Infosys stock higher",
            ],
            "negative": [
                "Infosys faces SEC probe into accounting practices",
                "Market reacts negatively to Infosys CEO resignation",
                "Infosys stock drops after missing earnings expectations",
            ],
            "neutral": [
                "Infosys to conduct annual general meeting next week",
                "Infosys opens new training center in Mysuru",
                "Infosys celebrates foundation day with events across campuses",
            ]
        }

    def generate_news(self, sentiment):
        return random.choice(self.templates[sentiment])

