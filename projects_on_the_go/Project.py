"""
COMP.CS.100 Programming 1 - round 12.
Names: Antton Alivuotila - Johan Nygård
Student IDs: 151259218 - 151394568
Email: antton.alivuotila@tuni.fi - johan.nygård@tuni.fi

Assignment: Project: Battleship
"""


class Ship:

    def __init__(self, name, coordinates):
        """
        Initializes the ship object.
        :param name: str, the name of the ship.
        :param coordinates: dict, the coordinates of the ship in a dict,
        with each coordinate having a bool-value indicating its status.
        """

        self.__name = name
        self.__coordinates = coordinates

    def sunk(self):
        """
        Checks if the ship is sunk by going through its bool-values.
        :return: bool, returns True if ship is sunk and vice-versa.
        """

        for key in self.__coordinates:
            if not self.__coordinates[key]:
                return False

            else:
                pass

        return True

    def check_hit(self, xy, shot_list):
        """
        Checks if the shot entered by the user hit the ship.
        :param xy: str, the coordinates entered by the user.
        :param shot_list, a list of shots made by the user
        :return: str, tells the user what outcome the shot had.
        """

        if xy in shot_list:
            return "shot_already"

        for key in self.__coordinates:

            if xy.upper() == key and not self.__coordinates[key]:
                self.__coordinates[key] = True
                return "hit"

        return "miss"

    def get_name(self):
        """
        Gets the name of the ship.
        :return: str, the name of the ship.
        """

        return self.__name

    def get_coordinates(self):
        """
        Gets the coordinate dictionary of the ship.
        :return: Dict, coordinates of the ship.
        """

        return self.__coordinates


def update_damage(ships, xy, game_map, shot_list):
    """
    Updates the consequences of the shot made by the user into the map.
    :param ships: list, list of each ship object.
    :param xy: str, coordinates entered by the user.
    :param game_map: str, the current state of the games map.
    :param shot_list: list, shots made by the user.
    :return: str, the updated map
    """

    xy = xy.upper()

    for ship in ships:
        result = ship.check_hit(xy, shot_list)

        if result == "hit":
            shot_list.append(xy)

            if ship.sunk():
                game_map = update_map(xy, game_map, ship, "sunk")
                print(f"You sank a", ship.get_name(), end="!\n")

            else:
                game_map = update_map(xy, game_map, ship, "hit")

            return game_map

        elif result == "shot_already":
            print("Location has already been shot at!")
            return game_map

        else:
            if ship == ships[-1]:
                shot_list.append(xy)
                game_map = update_map(xy, game_map, ship, "miss")

            else:
                pass

    return game_map


def create_map():
    """
    Creates a blank map for the game.
    :return: str, the blank map.
    """

    a_to_j = "  A B C D E F G H I J"
    the_rest = '\n'.join(f"{number}{21 * ' '}{number}" for number in range(10))
    game_map = f"{a_to_j}\n{the_rest}\n{a_to_j}"

    return game_map


def update_map(xy, game_map, ship, result):
    """
    updates the map of the ship by taking the previous map
    and modifying each row at a time in the correct way
    depending on the status of the ship and the effect that
    the shot had.

    :param xy: str, the coordinates entered by the user.
    :param game_map: str, the map to be updated
    :param ship: object, the ship that could be affected.
    :param result: str, the effect of the shot.
    :return: str, the new and updated map.
    """

    map_marks = {"hit": "X", "miss": "*", "sunk": ship.get_name()[0].upper()}
    x_to_num = {"a": 3, "b": 5, "c": 7, "d": 9, "e": 11, "f": 13, "g": 15, "h": 17, "i": 19, "j": 21}
    map_rows = game_map.split("\n")[1:-1]
    row_list = ["  A B C D E F G H I J"]
    ships_location = ship.get_coordinates()
    new_row = ""

    for row in map_rows:
        new_row_changed = False

        if ship.sunk() and result != "miss":

            for coordinates in ships_location:
                index = x_to_num[coordinates[0].lower()]

                if row[0] == coordinates[1] and new_row_changed:
                    new_row = new_row[:index - 1] + map_marks[result] + row[index:]

                elif row[0] == coordinates[1]:
                    new_row = row[:index - 1] + map_marks[result] + row[index:]
                    new_row_changed = True

            if new_row_changed:
                row_list.append(new_row)

            else:
                row_list.append(row)

        elif row[0] == xy[1]:
            index = x_to_num[xy[0].lower()]
            new_row = row[:index - 1] + map_marks[result] + row[index:]
            row_list.append(new_row)

        else:
            row_list.append(row)

    game_map = row_list[0] + "\n" + "\n".join(row_list[1:]) + "\n" + row_list[0]
    return game_map


def check_action(action):
    """
    Checks what the str entered by the user does.
    :param action: str, the user's action.
    :return: str, corresponding keyword for each action.
    """

    if action == "q":
        return "quit"

    elif ok_format([action]):
        return "shot_fired"

    else:
        return "user_tweaking"


def all_sunk(ships):
    """
    Goes through each ship one at a time, checking if they are afloat.
    :param ships: list, The list of all ships in the game.
    :return: bool, tells if the game ends or not.
    """

    for ship in ships:
        if not ship.sunk():
            return False

    return True


def ok_format(xy):
    """
    Checks if the coordinates entered by the user are in the right format.
    :param xy: str, the coordinates entered by the user.
    :return: bool - tells if the coordinates are okay.
    """

    ok_letters = "abcdefghij"
    ok_numbers = "0123456789"
    checks_out = []

    try:
        for coordinates in xy:
            checks_out.append(len(coordinates) == 2)
            checks_out.append(coordinates[0].lower() in ok_letters)
            checks_out.append(coordinates[1] in ok_numbers)

        if False in checks_out:
            return False

        else:
            return True

    except IndexError:
        return False


def overlapping(open_file):
    """
    Combines all the coordinates into one string to check
    if any of the coordinates appear more than once.
    :param open_file: list, containing each row in the file.
    :return: bool, tells if there are overlapping ships.
    """

    xy_lists = list(row.rstrip().split(";")[1:] for row in open_file)
    xy = sum(xy_lists, [])

    for coordinates in xy:
        if xy.count(coordinates) > 1:
            return True


def read_inputfile():
    """
    Asks the name of a file from the user and tries to read it,
    checks if the coordinates overlap,
    checks if the coordinates are in the correct format,
    and creates a list of each ship object if everything checks out.
    :return: bool/list, depending on if the file is okay.
    """

    ship_list = []
    file_name = input("Enter file name: ")

    try:
        temporary = open(file_name, mode="r")
        open_file = list(row for row in temporary)

        if overlapping(open_file):
            print("There are overlapping ships in the input file!")
            return False

        for row in open_file:
            row = row.rstrip().split(";")

            if not ok_format(row[1:]):
                print("Error in ship coordinates!")
                return False

            name = row[0]
            coordinates = {xy: False for xy in row[1:]}
            ship_list.append(Ship(name, coordinates))

        return ship_list

    except OSError:
        print("File can not be read!")


def main():
    """
    Creates a list of ship-objects and a map, and turns on the game.
    Game loops until every ship is sunk.
    """

    game_map = create_map()
    list_of_ships = read_inputfile()
    game_on = True
    shot_list = []

    if not list_of_ships:
        return

    while game_on:

        print()
        print(game_map)
        print()
        action = input("Enter place to shoot (q to quit): ")

        if check_action(action) == "shot_fired":
            game_map = update_damage(list_of_ships, action, game_map, shot_list)

            if all_sunk(list_of_ships):
                print()
                print(game_map)
                print()
                print("Congratulations! You sank all enemy ships.")
                game_on = False

            else:
                pass

        elif check_action(action) == "quit":
            print("Aborting game!")
            game_on = False

        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
