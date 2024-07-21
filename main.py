class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Member(Person):
    def __init__(self, name, age, membership_type):
        super().__init__(name, age)
        self.membership_type = membership_type

    def __str__(self):
        return f"Member - {super().__str__()}, Membership Type: {self.membership_type}"


class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}"


class Gun(Item):
    def __init__(self, name, serial_number, model, quantity):
        super().__init__(name, quantity)
        self.serial_number = serial_number
        self.model = model

    def __str__(self):
        return f"Gun - Serial Number: {self.serial_number}, Model: {self.model}, {super().__str__()}"


class GunClub:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.inventory = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_name):
        for member in self.members:
            if member.name == member_name:
                self.members.remove(member)
                return True
        return False

    def add_item(self, item):
        found = False
        for existing_item in self.inventory:
            if isinstance(existing_item, type(item)) and existing_item.name == item.name:
                existing_item.quantity += item.quantity
                found = True
                break
        if not found:
            self.inventory.append(item)

    def remove_item(self, item_name, quantity):
        for item in self.inventory:
            if isinstance(item, Gun) and item.name == item_name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.inventory.remove(item)
                    return True
        return False

    def list_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            print(member)

    def list_inventory(self):
        print(f"Inventory of {self.name}:")
        for item in self.inventory:
            print(item)


if __name__ == "__main__":
    club = GunClub("Python Gun Club")

    while True:
        print("\n=== Gun Club Management ===")
        print("1. Add Member")
        print("2. Add Gun to Inventory")
        print("3. Remove Member")
        print("4. Remove Gun from Inventory")
        print("5. List Members")
        print("6. List Inventory")
        print("0. Exit")
        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            name = input("Enter member's name: ")
            age = int(input("Enter member's age: "))
            membership_type = input("Enter membership type (Regular/Premium): ")
            member = Member(name, age, membership_type)
            club.add_member(member)
            print(f"{name} has been added as a member.")

        elif choice == "2":
            name = input("Enter gun's name: ")
            serial_number = input("Enter gun's serial number: ")
            model = input("Enter gun's model: ")
            quantity = int(input("Enter quantity: "))
            gun = Gun(name, serial_number, model, quantity)
            club.add_item(gun)
            print(f"{name} has been added to the inventory.")

        elif choice == "3":
            member_name = input("Enter member's name to remove: ")
            if club.remove_member(member_name):
                print(f"{member_name} has been removed from the club.")
            else:
                print(f"{member_name} not found in the club.")

        elif choice == "4":
            gun_name = input("Enter gun's name to remove from inventory: ")
            quantity = int(input("Enter quantity to remove: "))
            if club.remove_item(gun_name, quantity):
                print(f"{quantity} {gun_name}(s) removed from inventory.")
            else:
                print(f"Could not remove {quantity} {gun_name}(s) from inventory (not enough quantity).")

        elif choice == "5":
            club.list_members()

        elif choice == "6":
            club.list_inventory()

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 6.")
