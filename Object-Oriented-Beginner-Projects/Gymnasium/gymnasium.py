class Membership:
    def __init__(self, membership_type: str):  # defining the proper attributes
        self.membership_type = membership_type  # setting membership type
        self.room_access = []  # list of rooms associated with each membership

    def add_room_access(self, room: str):  # method to add room access
        self.room_access.append(room)

    def get_membership_type(self):  # method to get membership type
        return self.membership_type

    def __repr__(self):  # representation of Membership object
        return f"Membership Type: {self.membership_type}, Rooms Access: {', '.join(self.room_access)}"


class BasicMembership(Membership):  # inheriting from Membership class

    def __init__(self, membership_type: str, basic_plan_cost: float):  # initializing attributes
        super().__init__(membership_type)
        self.basic_plan_cost = basic_plan_cost  # setting basic plan cost

    def get_basic_plan_cost(self):  # method to get basic plan cost
        return self.basic_plan_cost

    def add_room_access(self, room: str):  # method to add room access
        self.room_access.append(room)


class ThreeMonthlyMembership(Membership):  # inheriting from Membership class
    additional_cost_percentage = 0.1  # defining additional cost percentage

    def __init__(self, membership_type: str, basic_plan_cost: float):  # initializing attributes
        super().__init__(membership_type)
        self.basic_plan_cost = basic_plan_cost  # setting basic plan cost

    def three_monthly_membership_cost(self, basic_plan_cost: float):  # calculating cost for three-monthly plan
        membership_cost = basic_plan_cost * self.additional_cost_percentage
        return f"membership_cost for three monthly plan is : {membership_cost}"

    def add_room_access(self, room: str):  # method to add room access
        self.room_access.append(room)


class AnnualMembership(Membership):  # inheriting from Membership class
    def __init__(self, membership_type: str):  # initializing attributes
        super().__init__(membership_type)
        self.all_rooms_access = []  # list containing all available rooms

    @staticmethod
    def additional_annual_membership_cost():  # additional cost for annual membership
        return "There is no additional cost for this plan"

    def get_all_rooms_access(self):  # method to get all rooms access
        return self.all_rooms_access

class Room:
    def __init__(self, room_name: str):  # initializing room name
        self.room_name = room_name

    def is_included_in_membership(self, membership):  # checking room access based on membership type

        # Checking membership types and room access
        if membership == "Annual":
            return f"With annual subscription, access for {self.room_name} room is free of charge"
        elif membership == "ThreeMonthly":
            if self.room_name == "Climbing Wall":
                return f"With ThreeMonthly, access for {self.room_name} room requires 10% additional cost"
            else:
                return f"With ThreeMonthly, access for {self.room_name} room is free of charge"
        elif membership == "Basic":
            if self.room_name == "Climbing Wall":
                return f"With Basic plan, access for {self.room_name} room is not allowed"
            else:
                return f"With Basic plan, access for {self.room_name} room is free of charge"

class Customer:
    customer_list = []  # list to hold customers

    def __init__(self, name: str, subscription_type: str):  # initializing customer attributes
        self.name = name  # setting customer name
        self.subscription_type = subscription_type  # setting subscription type
        Customer.customer_list.append(self)  # adding customer to list

    def remove_customer_from_list(self):  # method to remove customer from list
        if self in Customer.customer_list:
            Customer.customer_list.remove(self)
            return f"Customer '{self.name}' has been removed."
        else:
            return "Customer not found in the list."

    @classmethod
    def show_customers(cls):  # method to display customers
        sorted_customers = sorted(cls.customer_list, key=lambda x: x.name)  # sorting customers alphabetically
        print("Customers:")
        for customer in sorted_customers:
            print(customer.name, "-", customer.subscription_type)  # printing customer name and subscription type

    def get_name(self):  # method to get customer name
        return self.name

    def get_membership_type(self):  # method to get subscription type
        return self.subscription_type

# Testing Room Class
# Creating room instances
room1 = Room("Weight Room")
room2 = Room("Swimming Pool")
room3 = Room("Climbing Wall")

# Check access for rooms based on membership types
# Printing room access based on different memberships
print(room1.is_included_in_membership("Basic"))
print(room2.is_included_in_membership("Basic"))
print(room3.is_included_in_membership("Basic"))

print(room1.is_included_in_membership("ThreeMonthly"))
print(room2.is_included_in_membership("ThreeMonthly"))
print(room3.is_included_in_membership("ThreeMonthly"))

print(room1.is_included_in_membership("Annual"))
print(room2.is_included_in_membership("Annual"))
print(room3.is_included_in_membership("Annual"))

# Testing Customer Class
# Creating Customer instances
customer1 = Customer("Alice", "Basic")
customer2 = Customer("Bob", "ThreeMonthly")
customer3 = Customer("Charlie", "Annual")

# Check the membership type of specific customers
print(customer1.get_membership_type())
print(customer2.get_membership_type())
print(customer3.get_membership_type())

# Display list of customers with alphabetic order
Customer.show_customers()

# Modifying the list of customers
new_customer1 = Customer("Ali", "Basic")
new_customer2 = Customer("Bamdad", "Annual")
new_customer3 = Customer("Hossein", "Annual")
new_customer4 = Customer("Melisa", "ThreeMonthly")
new_customer5 = Customer("Zac", "ThreeMonthly")

Customer.show_customers()

Customer.remove_customer_from_list(new_customer1)
Customer.show_customers()

# Getting new customers' membership_type
print(new_customer3.get_membership_type())
print(new_customer4.get_membership_type())
print(new_customer5.get_membership_type())

