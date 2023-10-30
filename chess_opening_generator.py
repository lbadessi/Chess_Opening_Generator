import chess
import pandas as pd
import csv
import random
from cairosvg import svg2png
import chess.svg



def opening_fixer(input_list):
    for i in range(len(input_list)):
        if input_list[i][0].isdigit():
            input_list[i] = input_list[i][1:]
    for i in range(len(input_list)):
        if input_list[i][0] == '.':
            input_list[i] = input_list[i][1:]
    return input_list

def random_opening_generator():
    board = chess.Board()
    board.reset()
    csv_file = "chess_openings.csv"

    with open(csv_file, "r") as file:
        num_lines = sum(1 for line in file) - 1

    random_line_number = random.randint(1, num_lines)

    with open(csv_file, "r") as file:
        csvreader = csv.DictReader(file)
        for i, row in enumerate(csvreader, start=1):
            if i == random_line_number:
                random_opening = row
                break
    print(random_opening["ECO"])
    print(random_opening["name"])
    print(random_opening["moves"])

    text = random_opening["moves"].split()


    for move in opening_fixer(opening_fixer(text)):
        board.push_san(move)

    sboard = chess.svg.board(board)

    svg2png(sboard, write_to='static/example-board.png')

    image_path = 'static/example-board.png'



    return random_opening["ECO"], random_opening["name"] ,  random_opening["moves"]
    

if __name__ == '__main__':
    app.run(debug=True)

