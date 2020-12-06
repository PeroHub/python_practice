class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher")

class Customer(User):
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        
        self.membership = new_membership

    def read_customer():
        print("Reading Customer")

    def __str__(self):
        
        return self.name + " " + self.membership

    def print_all_customers(Customers):
        for customer in Customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        return False

    __repr__ = __str__
        

users = [Customer("caleb", "Gold"),Customer("Peter", "Bronze"), Teacher()]



for user in users:
    user.log()

