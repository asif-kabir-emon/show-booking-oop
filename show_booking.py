class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    __seats = {}
    __show_list = []
    
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        
        Star_Cinema.entry_hall(self)
    
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        
        seat_init = []
        for i in range(1, self.rows+1):
            row = []
            for j in range(1, self.cols+1):
                row.append(0)
            seat_init.append(row)
        
        self.__seats[id] = seat_init
    
    def book_seats(self, id):
        if id in [show[0] for show in self.__show_list]:
            number_of_ticket = int(input("Number of tickets?: "))
            else_number_of_ticket = number_of_ticket
            
            while else_number_of_ticket > 0:
                if number_of_ticket == 1:
                    seat_row = int(input("Enter row: "))
                    seat_col = int(input("Enter column: "))
                else:
                    seat_row = int(input(f"\nEnter row for {number_of_ticket - else_number_of_ticket + 1} ticket: "))
                    seat_col = int(input(f"Enter column for {number_of_ticket - else_number_of_ticket + 1} ticket: "))
                
                try:
                    if self.__seats[id][seat_row][seat_col] == 0:
                        self.__seats[id][seat_row][seat_col] = 1
                        print(f"Seat ({seat_row}, {seat_col}) booked for show {id}.")
                        else_number_of_ticket -= 1
                    else:
                        print("Seat already booked!!! Please choose another seat.")
                except:
                    print("Invalid seat!!!")
        else:
            print("Invalid show id!!! Show are not available.")
    
    def view_show_list(self):
        if self.__show_list:
            for i in self.__show_list:
                print(f"Movie Name: {i[1]}, Show ID: {i[0]}, Time: {i[2]}")
        else:
            print("No shows available")
    
    def view_available_seats(self, id):
        if id in [show[0] for show in self.__show_list]:
            available_seats = []
            for i in range(len(self.__seats[id])):
                for j in range(len(self.__seats[id][i])):
                    if self.__seats[id][i][j] == 0:
                        available_seats.append((i, j))
            
            if len(available_seats) > 0:
                print(f"\nAvailable Seats for show {id}:")
                for seat in available_seats:
                    print(f"Seat: ({seat[0]}, {seat[1]})")
                
                print("\nUpdated Seats Matrix:")
                for i in self.__seats[id]:
                    print(i)
            else:
                print("No seats available")
        else:
            print("Invalid Id!!! Show is not available.")



a = Hall(10, 10, 1)
a.entry_show(111, "The Godfather", "26/04/2024 10:00 AM")
a.entry_show(112, "The Dark Knight", "26/04/2024 01:00 PM")
a.entry_show(113, "The Shaw Shank Redemption", "26/04/2024 04:00 PM")


while True:
    print("1. View All Shows")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")
    
    option = int(input("Enter Option: "))
    
    print("-" * 20)
    
    if option == 1:
        a.view_show_list()
    elif option == 2:
        show_id = int(input("Enter Show ID: "))
        a.view_available_seats(show_id)
    elif option == 3:
        show_id = int(input("Enter Show ID: "))
        a.book_seats(show_id)
    elif option == 4:
        break
    else:
        print("Invalid Option!!!")
    
    print("-" * 20)
    print("\n")