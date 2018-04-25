from pprint import pprint as pp
class Flight:

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}".format(number))
        if not number[:2].isupper():
            raise ValueError("No airline code in '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number=number
        self._aircraft=aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating=[None]+[{letter: None for letter in seats} for _ in rows]
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def airmodel(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        rows,seat_letters=self._aircraft.seating_plan()
        letter=seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))
        row_text=seat[:-1]
        try:
            row=int(row_text)
        except ValueError:
            raise ValueError('Invalid seat row {}'.format(row_text))
        if row not in rows:
            raise ValueError('Invalid row number {}'.format(row))
        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied'.format(seat))
        self._seating[row][letter]=passenger

    def make_flight(self):
        f = Flight("AA1668", Aircraft("E-TUP", "AIRBUS", 22, 6))
        f.allocate_seat("10B", "xingwen")
        f.allocate_seat("10A", "chenggang")
        f.allocate_seat("1C", "xuxiaodi")
        f.allocate_seat("1F", "liujuan")

    def console_card_print(self,passenger,seat, flight_number,aircraft):
        output="| Name: {0}"    \
               " Flight: {1}"   \
               " Seat: {2}"     \
               " Aircraft: {3}" \
               " |".format(passenger,flight_number,seat,aircraft)
        banner='+'+'-'*(len(output)-2)+'+'
        border='|'+' '*(len(output)-2)+'|'
        lines=[banner,border,output,border,banner]
        card='\n'.join(lines)
        print(card)
        print()

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration=registration
        self._model=model
        self._num_rows=num_rows
        self._num_seats_per_row=num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

if __name__=="__main__":
    f = Flight("AA1668", Aircraft("E-TUP", "AIRBUS", 22, 6))
    f.make_flight()
    f.console_card_print("chenggang","8A","AA1668",Aircraft("E-TUP", "AIRBUS", 22, 6))

