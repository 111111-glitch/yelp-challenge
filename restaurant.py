from review import Review
from customer import Customer

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self._reviews = []
        self.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Name must be 1 or more characters long")
        self._name = value

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set(review.customer for review in self._reviews))

    def average_star_rating(self):
        if not self._reviews:
            return 0.0
        return sum(review.rating for review in self._reviews) / len(self._reviews)

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(cls.all_restaurants, key=lambda restaurant: restaurant.average_star_rating(), reverse=True)
        return sorted_restaurants[:2]
