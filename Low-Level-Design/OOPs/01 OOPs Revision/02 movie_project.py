"""
Create a class Movie with the following:

Attributes:
movie_name -> name of the movie
total_seats -> total seats available in the theatre
ticket_price-> price per ticket
booked_seats -> starts at 0

Methods:
book_ticket(num_tickets) - books the given number of tickets. If enough seats are available, 
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() - displays movie name, seats available, and seats booked so far

"""
class Movie:
    def __init__(self, name:str, seats:int, prices:int) -> None:
        self.movie = name
        self.seats = seats
        self.prices = prices
        self.booked_seats = 0

    def show_status(self) -> None:
        print(f"The name of the movie is: {self.movie}, the seats available are: {self.seats}, the seats booked so far: {self.booked_seats}")

    def book_ticket(self, num_tickets:int) -> None:
        self.num_tickets = num_tickets
        if self.seats >= self.num_tickets:
            self.seats -= self.num_tickets
            self.booked_seats += self.num_tickets
            print(f"The total amount to pay is {self.prices*num_tickets}, the booking will be confirmed")
        else:
            print("Sorry enough seats are not available")
m1 = Movie("Endgame", 10, 280)
m1.show_status()
m1.book_ticket(8)
m1.show_status()
m1.book_ticket(3)

