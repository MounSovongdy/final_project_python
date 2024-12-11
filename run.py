# run.py

from ship import ShipManager  # Ensure this matches the class name in ship.py


def print_board(board, ships):
    print("-------")
    for y in range(len(board)):
        row = []
        for x in range(len(board[y])):
            cell = board[y][x]
            if cell == 'X':
                row.append('X')  # Hit
            elif cell == 'O':
                row.append(' ')  # Miss
            else:
                # Find the ship that occupies this cell
                ship = next((s for s in ships if s.coordinates == (x, y)), None)
                if ship and not ship.sunk:
                    row.append(ship.symbol)  # Display ship symbol if not sunk
                else:
                    row.append(' ')  # Empty space if no ship

        print("|" + "".join(row) + "|")
    print("-------")


def main():
    board_size = 5
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]  # Initialize board with spaces

    ship_manager = ShipManager(board_size)  # Create an instance of ShipManager
    ships = ship_manager.create_ships()  # Call create_ships on the instance

    print("Game started. Fire at will!")

    for attempts in range(10):
        coords = input(f"Enter X, Y coordinate [{attempts + 1}/10]: ")
        try:
            x, y = map(int, coords.split(','))
        except ValueError:
            print("Invalid coordinates. Try again.")
            continue

        if not (0 <= x < board_size and 0 <= y < board_size):
            print("Invalid coordinates. Try again.")
            continue

        hit_ship = ship_manager.get_ship_at(x, y)  # Assuming this method checks for a hit
        if hit_ship:
            print(f"You sank {hit_ship}!")
            board[y][x] = 'X'  # Mark hit on the board
            for ship in ships:
                if ship.coordinates == (x, y):
                    ship.sunk = True  # Mark the ship as sunk
            print_board(board, ships)  # Print the updated board
        else:
            print("Miss!")
            board[y][x] = 'O'  # Mark miss on the board
            print_board(board, ships)  # Print the updated board

        if all(ship.sunk for ship in ships):  # Check if all ships are sunk
            print("Congratulations! All ships are sunk.")
            break


if __name__ == "__main__":
    main()