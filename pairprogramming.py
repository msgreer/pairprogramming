# Parking Garage Class

class Parking_garage():
    tickets = 10
    parking_spots = 10
    def __init__(self, tickets, parking_spots):
        self.tickets = tickets
        self.parking_spots = parking_spots
        
ticket_1 = Parking_garage(9,9)
ticket_2 = Parking_garage(8,8)       
print(f"There are {ticket_1.tickets} tickets left and there are {ticket_1.parking_spots} parking spots left.")
print(f"There are {ticket_2.tickets} tickets left and there are {ticket_2.parking_spots} parking spots left.")
