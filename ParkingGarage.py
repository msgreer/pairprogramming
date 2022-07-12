# Parking Garage Class

class Parking_garage():
    def __init__(self, tickets, parkingSpaces, currentticket):
        self.tickets = tickets
        self.parkingspaces = parkingSpaces
        self.currentTicket = currentticket
        self.paymentdone = 'PAID'
        self.chargeamount = 15
    
#Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1 
    def takeTicket(self):
        while True:
            tic = input("Would you like a ticket? Yes/No ").lower()
            if tic == 'yes' and self.tickets != []:
                print(f"Your ticket number is: {self.tickets.pop()}")
                self.parkingspaces.pop()
                print(f"Spots {len(chicago.parkingspaces)} remaining")
            elif tic == 'yes' and self.tickets == []:
                print("Sorry! There are no more tickets available.")
                break
            elif tic == 'no':
                break
            else: 
                print("Invalid entry; please try again.")
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
    def payForParking(self):
        d1 = {
            self.currentTicket : 'UNPAID'
        }
        while True:
            fee = input(f"Your parking fee today is ${self.chargeamount} for Ticket {d1} Please select an amount to pay. ")
            if int(self.chargeamount) - int(fee) == 0:
                print("Your ticket has been paid! Please exit the garage in the next 15 minutes.")
                d1[self.currentTicket]= self.paymentdone
                return(d1)
                
            elif int(self.chargeamount) - int(fee) != 0:
                self.chargeamount = int(self.chargeamount) - int(fee)
            else:
                print("Invalid entry, please try again.")
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)
    def leaveGarage(self):
        
        while True:
            bye = input(f"Thank you for coming! Have you paid for Ticket {self.currentTicket}? Yes/No").lower()
            if bye == "yes":
                print("Thank You, have a nice day")
                self.tickets.append(self.currentTicket)
                self.tickets.sort()
                self.parkingspaces.append(self.currentTicket)
                self.parkingspaces.sort()
                break
            elif bye == "no":
                print("You have not paid yet.")
                break

def run():
    while True:
        entrance = input('What would you like to do? Ticket/Pay/Leave ').lower()
        if entrance == 'ticket':
            chicago.takeTicket()
        elif entrance == 'pay':
            chicago.payForParking()
        elif entrance == 'leave':
            chicago.leaveGarage()
        else:
            print("Invalid Entry. Please try again.")
            break

chicago=Parking_garage([1,2,3,4],[1,2,3,4],4)
run()