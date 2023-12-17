import itertools
import os
import re
from typing import NamedTuple

dir_path = os.path.dirname(os.path.realpath(__file__))


class SetOfCubes(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0


class Game:
    def __init__(self, game_id: int):
        self._game_id = game_id
        self._sets_of_cubes: list[SetOfCubes] = []

    def add_set_of_cubes(self, cubes: SetOfCubes):
        self._sets_of_cubes.append(cubes)

    @property
    def sets_of_cubes(self) -> list[SetOfCubes]:
        return self._sets_of_cubes

    @property
    def game_id(self):
        return self._game_id


def game_from_text(line: str) -> Game:
    game, sets = line.split(":")
    game_id = re.search(r"Game\s+(\d+)\s*", game).group(1)
    game_instance = Game(int(game_id))
    for s in sets.strip().split(";"):
        red_regex = re.search(r"(?P<red>\d+)\s+red", s)
        red = int(red_regex.group("red") if red_regex else 0)
        green_regex = re.search(r"(?P<green>\d+)\s+green", s)
        green = int(green_regex.group("green") if green_regex else 0)
        blue_regex = re.search(rf"(?P<blue>\d+)\s+blue", s)
        blue = int(blue_regex.group("blue") if blue_regex else 0)
        game_instance.add_set_of_cubes(SetOfCubes(red, green, blue))
    return game_instance


def import_games() -> list[Game]:
    file_path = os.path.join(dir_path, "data/day2_input.txt")
    games = []
    with open(file_path, "r") as f:
        for line in f:
            games.append(game_from_text(line))
    return games


class GameAnalyzer:
    """Imports data, instantiates Games and provides infos about them"""

    def __init__(self, nbr_red: int = 0, nbr_green: int = 0, nbr_blue: int = 0):
        """Check if game is possible, given the number of red, green, blue cubes"""
        self._nbrRed = nbr_red
        self._nbrGreen = nbr_green
        self._nbrBlue = nbr_blue

    def is_possible_game(self, game: Game) -> bool:
        """Checks if `game` is possible"""
        max_set = maximum_set(game)
        return (
            0 <= max_set.red <= self._nbrRed
            and 0 <= max_set.green <= self._nbrGreen
            and 0 <= max_set.blue <= self._nbrBlue
        )


def maximum_set(game) -> SetOfCubes:
    """Return set with individual maximal cubes"""
    max_red = max(x.red for x in game.sets_of_cubes)
    max_green = max(x.green for x in game.sets_of_cubes)
    max_blue = max(x.blue for x in game.sets_of_cubes)
    return SetOfCubes(max_red, max_green, max_blue)


def get_sum_of_ids_of_possible_games(
    red: int, green: int, blue: int, games: list[Game]
) -> int:
    """Return sum of ids of all games possible"""
    analyzer = GameAnalyzer(nbr_red=red, nbr_green=green, nbr_blue=blue)
    id_sum = sum(x.game_id for x in games if analyzer.is_possible_game(x))
    return id_sum


def sum_of_power_of_minimum_sets():
    max_sets = [maximum_set(game) for game in import_games()]
    return sum(x.red * x.green * x.blue for x in max_sets)


if __name__ == "__main__":
    sum_ids = get_sum_of_ids_of_possible_games(
        red=12, green=13, blue=14, games=import_games()
    )
    sum_powers = sum_of_power_of_minimum_sets()
    print(f"Sum of ids of all possible games: {sum_ids}")
    print(f"Sum of all powers of minimum_sets: {sum_powers}")
