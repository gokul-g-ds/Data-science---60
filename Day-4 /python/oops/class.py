#creating class 

print("Creating class")

class cars:
    no_of_seats = 7
    no_of_airbags = 6
    no_of_speaker = 9
    no_of_wheels = 4
    fuel = "petrol"
    
    def mf(self):
      print("Moving forward")
      
    def bf(self):
      print("moving backward")
      
print("*****Benz cars*****")
Benz = cars()
print("seats",Benz.no_of_seats)
print("Airbage",Benz.no_of_airbags)
Benz.fuel = "Diesel"
print("Fuel",Benz.fuel)

print("*****Toyota cars*****")
Toyota = cars()
print("seats",Toyota.no_of_seats)
Toyota.bf()
Toyota.no_of_speaker = 12
print("speaker",Toyota.no_of_speaker)

'''Creating class
*****Benz cars*****
seats 7
Airbage 6
Fuel Diesel
*****Toyota cars*****
seats 7
moving backward
speaker 12

=== Code Execution Successful ==='''
