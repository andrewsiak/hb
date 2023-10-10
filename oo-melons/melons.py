# """Classes for melon orders."""


# class DomesticMelonOrder:
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder:
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code


"""Classes for melon orders."""

from random import randint
import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    order_type = None
    tax = 0
    base_price = 5
    

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        
        if self.qty > 100:
            raise TooManyMelonsError

    def get_total(self):
        """Calculate price, including tax."""
        base_price = AbstractMelonOrder.get_base_price()

        if self.species.lower() == "christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        
        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    @staticmethod
    def get_base_price():
        """Returns a random base price number"""
        rush_hour_increase = 4
        if AbstractMelonOrder.is_it_rush_hour():
            return randint(5,9) + rush_hour_increase
        else:
            return randint(5,9)

    @staticmethod
    def is_it_rush_hour():
        """Determins if it is Mon-Fri and between 8-11am"""
        order_placed_moment = datetime.datetime.now() 
        today = datetime.datetime.weekday(order_placed_moment) 
        return order_placed_moment.hour >= 8 and order_placed_moment.hour <= 11 and today < 5


class DomesticMelonOrder(AbstractMelonOrder): 
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "us-government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed_inspection):
        """Update inspection status when passed_inspection == True"""
        #error if not True (something else)
        passed_collection = [True, 'y', 'yes', 'yeah', 'okay', 'confirmed', 'pass', 'passed', 'passes']
        if passed_inspection not in passed_collection:
            print("Error: Only update Inspection status after melons have passed inspection.")
        else:
            self.passed_inspection = True

        # or method running, updates to True
        


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    small_order_fee = 3

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

    def get_total(self):
        if self.qty < 10:
            return super().get_total() + self.small_order_fee       
        else:
            return super().get_total()

class TooManyMelonsError(ValueError):
    
    def __init__(self):
        """Initialize TooManyMelonsError using init method from ValueError."""

        super().__init__("Order can be no more than 100 melons.")
