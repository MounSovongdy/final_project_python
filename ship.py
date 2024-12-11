# ship.py

class Ship:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.name = f"Ship{symbol}"
        self.coordinates = (x, y)
        self.sunk = False

    def __repr__(self):
        return self.name


class ShipManager:  # Changed from Shipboard to ShipManager
    def __init__(self, board_size):
        self.board_size = board_size
        self.ships = []
        self.occupied_coords = set()
        self.symbols_taken = set()

    def create_ships(self):
        print("Creating ships...")
        while len(self.ships) < 10:
            user_input = input("> ")
            if user_input.strip().upper() == "END SHIPS":
                break

            tokens = user_input.split()
            if len(tokens) != 3:
                print("Error: <symbol> <x> <y>")
                continue

            symbol, x_str, y_str = tokens
            if not (symbol.isalpha() and 'A' <= symbol <= 'J'):
                print("Error: symbol must be between 'A'-'J'")
                continue

            try:
                x = int(x_str)
                y = int(y_str)
            except ValueError:
                print(f"Error: ({x_str}, {y_str}) is an invalid coordinate")
                continue

            if not (0 <= x < self.board_size and 0 <= y < self.board_size):
                print(f"Error: ({x}, {y}) is out-of-bounds on {self.board_size}x{self.board_size} board")
                continue

            if (x, y) in self.occupied_coords:
                print(f"Error: ({x}, {y}) is already occupied by {self.get_ship_at(x, y)}")
                continue

            if symbol in self.symbols_taken:
                print(f"Error: symbol '{symbol}' is already taken")
                continue

            ship = Ship(symbol, x, y)
            self.ships.append(ship)
            self.occupied_coords.add((x, y))
            self.symbols_taken.add(symbol)
            print(f"Success! {ship} added at ({x}, {y})")

        print(f"{len(self.ships)} ships added.")
        return self.ships

    def get_ship_at(self, x, y):
        for ship in self.ships:
            if ship.coordinates == (x, y):
                return ship.name
        return None