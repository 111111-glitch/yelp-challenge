from customer import Customer
from restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

