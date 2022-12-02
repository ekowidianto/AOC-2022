def move_score(move):
    score_map = {'X': 1, 'Y': 2, 'Z': 3}
    return score_map[move]


def move_map(move, opp_move):
    maps = {'X C': 6, 'Y A': 6, 'Z B': 6, 'X A': 3,
            'Y B': 3, 'Z C': 3, 'X B': 0, 'Y C': 0, 'Z A': 0}
    return maps[move + ' ' + opp_move]


def compute_score(move, opp_move):
    return move_score(move) + move_map(move, opp_move)


def find_move(opp_move, result):
    maps = {'A Y': 'X', 'B Y': 'Y', 'C Y': 'Z',
            'A X': 'Z', 'B X': 'X', 'C X': 'Y',
            'A Z': 'Y', 'B Z': 'Z', 'C Z': 'X'}
    return maps[opp_move + ' ' + result]


def total_score():
    strategy = read_file('input.txt')
    total_scores = 0

    for move in strategy:
        moves = move.split()
        my_move = find_move(moves[0], moves[1])
        total_scores += compute_score(my_move, moves[0])

    print(total_scores)
    return total_scores


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    total_score()
