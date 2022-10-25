############ Read Me #############
# Left click to chose the cell
# Right click to start the game.

import pygame
import sys

width, height = 1001, 501
square = 20

pygame.init()
board = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

for i in range(width // square + 1):
    pygame.draw.line(board, (255, 182, 193), (square * i, 0), (square * i, height))
    pygame.draw.line(board, (255, 182, 193), (0, square * i), (width, square * i))

def check(x, y):
    row = [x - square, x, x + square]
    column = [y + square, y, y - square]
    neighbor = 0

    for j in row:
        for n in column:
            z = board.get_at([j + square // 4, n + square // 4])
            if j == x and n == y:
                pass
            elif z == (255, 192, 203, 255):
                neighbor += 1
    return neighbor

array = []
check_that_no_change = []

################### section 1 #####################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    position = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if position[0] % 20 != 0:
            a = position[0] % square
            x = position[0] - a
        if position[1] % 20 != 0:
            b = position[1] % square
            y = position[1] - b
        color = board.get_at(position)
        if color == (0, 0, 0, 255):
            pygame.draw.rect(board, (255, 192, 203), ((x + 1, y + 1), (square - 1, square - 1)))
            array.append([x, y])
            pygame.time.wait(300)

        elif color == (255, 192, 203, 255):
            pygame.draw.rect(board, (0, 0, 0), ((x + 1, y + 1), (square - 1, square - 1)))
            print(position)
            array.remove([x, y])
            pygame.time.wait(300)
    if pressed[2]:
        print("right click")
        break

    pygame.display.update()



################### section 2 #####################
while True:
    to_be_change_to_black = []
    to_be_change_to_pink = []
    to_be_change_to_pink.clear()
    to_be_change_to_black.clear()

    for i in array:
        row = [i[0] - square, i[0], i[0] + square]
        column = [i[1] + square, i[1], i[1] - square]
        for q in row:
            for w in column:
                if check(q, w) == 2 and board.get_at((q + square // 4, w + square // 4)) == (255, 192, 203, 255):
                    if [q, w] not in to_be_change_to_pink:
                        to_be_change_to_pink.append([q, w])
                elif check(q, w) > 3:
                    if [q, w] not in to_be_change_to_black:
                        to_be_change_to_black.append([q, w])
                elif check(q, w) < 2:
                    if [q, w] not in to_be_change_to_black:
                        to_be_change_to_black.append([q, w])
                elif check(q, w) > 2:
                    if [q, w] not in to_be_change_to_pink:
                        to_be_change_to_pink.append([q, w])


    pygame.time.wait(500)
    for i in to_be_change_to_black:
        pygame.draw.rect(board, (0, 0, 0), ((i[0] + 1, i[1] + 1), (square - 1, square - 1)))

    for i in to_be_change_to_pink:
        pygame.draw.rect(board, (255, 192, 203), ((i[0] + 1, i[1] + 1), (square - 1, square - 1)))

    array = to_be_change_to_pink
    pygame.display.update()

    if array == check_that_no_change:
        break
    check_that_no_change = array
