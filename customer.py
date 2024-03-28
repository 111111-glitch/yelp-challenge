from review import Review
from restaurant import Restaurant

class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._reviews = []
        self.all_customers.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string")
        if not (1 <= len(value) <= 25):
            raise ValueError("First name must be between 1 and 25 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        if not (1 <= len(value) <= 25):
            raise ValueError("Last name must be between 1 and 25 characters")
        self._last_name = value

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def num_negative_reviews(self):
        return sum(1 for review in self._reviews if review.rating < 3)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self._reviews)
