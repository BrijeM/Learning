class Flight:
    def __init__(self,number,aircraft): # An object of aircraft class is passed ch:1

        ''' Class invariants are thruths about an object that endure throught its life time.
            SN060 : Airline code should have first two letters as capital
                    The next 3 0r 4 digits should specify the route number.'''

        if not number[:2].isalpha():
            raise ValueError('No airline code in {}'.format(number))
        if not number[:2].isupper():
            raise ValueError('Invalid airline code {}'.format(number))
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError('Invalid route number {}'.format(number))

        self._number = number
        self._aircraft=aircraft


    def flight_number(self):
        return self._number

    def airline_number(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()    # New method is added to the class Flight to get aircraft model which returns the model() function of Aircraft class. ch:1


class Aircraft:
    def __init__(self,registration,model,no_of_rows,no_of_seats_per_row):
        self._registration = registration
        self._model=model
        self._no_of_rows = no_of_rows
        self._no_of_seats_per_row=no_of_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_arrangement(self):
        return (range(1,self._no_of_rows + 1),"ABCDEFGHJK"[:self._no_of_seats_per_row])