print("Constructor and Destructor")


class Students:
    def __init__(self, name, age, house, rollnum):
        print("This is constructor")
        self.name = name
        self.age = age
        self.house = house
        self.rollnum = rollnum

    def __del__(self):
        print("This is Destructor")

    def DS(self):
        print("Day scholar")

    def HS(self):
        print("Hostel student")


Aclass = Students("Ronaldo", 12, "red", 100237)
print(Aclass.name, Aclass.age, Aclass.house, Aclass.rollnum)
Aclass.DS()    # () is required to call the method


Bclass = Students("Messi", 10, "blue", 100010)
print(Bclass.name, Bclass.age, Bclass.house, Bclass.rollnum)
Bclass.HS()    # () is required to call the method


Cclass = Students("Yamal", 8, "orange", 1000154)
print(Cclass.name, Cclass.age, Cclass.house, Cclass.rollnum)

# Delete Cclass object
del Cclass

print("Cclass is deleted")

'''Constructor and Destructor
This is constructor
Ronaldo 12 red 100237
Day scholar
This is constructor
Messi 10 blue 100010
Hostel student
This is constructor
Yamal 8 orange 1000154
This is Destructor
Cclass is deleted
This is Destructor
This is Destructor

=== Code Execution Successful ==='''
