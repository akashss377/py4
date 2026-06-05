from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year
    def years_on_platform(self):
        return 2025 - self.joining_year
    @abstractmethod
    def get_role(self):
        pass
    def display_info(self):
        print(f"Name: {self.name}, Role: {self.get_role()}, Years on Platform: {self.years_on_platform()}")
class Customer(User):
    def get_role(self):
        return "Customer"
class Vendor(User):
    def get_role(self):
        return "Vendor"
customer = Customer("Alice", 2020)
vendor = Vendor("Bob", 2018)
customer.display_info()
vendor.display_info()
