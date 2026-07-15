import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    y, x = sh // 2, sw // 2
    snake = [[y, x], [y, x-1], [y, x-2]]
    food = None 
    while food is None:
        nf = [random.randint(1, sh-3), random.randint(1, sw-3)]
        if nf not in snake:
            food = nf

    stdscr.addch(food[0], food[1], '*') # Troquei ACS_PI por '*' para garantir que apareça
    key = curses.KEY_RIGHT
   
    while True: 
        next_key = stdscr.getch()
        if next_key == curses.KEY_UP and key != curses.KEY_DOWN:
            key = next_key
        elif next_key == curses.KEY_DOWN and key != curses.KEY_UP:
            key = next_key
        elif next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
            key = next_key
        elif next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
            key = next_key
        
        head = snake[0].copy()
        if key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [random.randint(1, sh-2), random.randint(1, sw-2)]
                if nf not in snake:
                    food = nf
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        if (snake[0][0] in [0, sh-1] or 
            snake[0][1] in [0, sw-1] or 
            snake[0] in snake[1:]):
            break 

    stdscr.addch(sh // 2, sw // 2 - 4, "GAME OVER")
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)


    