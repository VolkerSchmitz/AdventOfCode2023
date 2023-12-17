from day2 import import_games, Game


def test_number_of_games_is_100():
    games = import_games()
    assert len(games) == 100
    game_1 = games[0]
    assert isinstance(game_1, Game)
    assert 1 == game_1.game_id


def test_number_of_sets_of_first_game_is_three():
    games = import_games()
    first = games[0]
    assert 4 == len(first.sets_of_cubes)
