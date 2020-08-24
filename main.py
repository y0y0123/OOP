class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


#c = Customer("Go", "Silver")
#print(c.name, c.membership_type)

#c2 = Customer("Bayu", "Gold")
#print(c2.name, c2.membership_type)

customers = [Customer("Go", "Silver"),
             Customer("Bayu", "Gold")]

print(customers[0].name)