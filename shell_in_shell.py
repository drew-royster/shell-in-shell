from __future__ import division
from asciimatics.effects import Cycle, Snow, Print, Sprite
from asciimatics.renderers import FigletText, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.event import KeyboardEvent
import math
from asciimatics.paths import Path, DynamicPath
import sys
import random

ball_location = 1

# Shell definition
shell = """
 ___
/   \\
"""

#ball definition
ball = """

O
"""

#X definition
x = """

X
"""

def get_game(game_index, centre, screen):
    if game_index == 1:
        left_path = Path()
        left_path.jump_to(centre[0] - 9, centre[1] + 2)
        left_path.move_straight_to(centre[0] - 9, centre[1] - 1, 10),
        left_path.move_straight_to(centre[0], centre[1] - 1, 10),
        left_path.move_straight_to(centre[0], centre[1] + 2, 10),
        left_path.is_finished


        middle_path = Path()
        middle_path.jump_to(centre[0], centre[1] + 2)
        middle_path.wait(15)
        middle_path.move_straight_to(centre[0] -9, centre[1] + 2, 10)
        middle_path.wait(50)
        middle_path.is_finished

        effects = [
            Shell(screen, left_path),
            Shell(screen, middle_path),
            Print(screen, StaticRenderer(images=[shell]),
                x=centre[0] + 7,
                y=centre[1])
        ]
        return(Scene(effects, 66), 1)
    elif game_index == 2:
        right_path = Path()
        right_path.jump_to(centre[0] + 7, centre[1] + 2)
        right_path.move_straight_to(centre[0] + 7, centre[1] - 1, 10),
        right_path.move_straight_to(centre[0], centre[1] - 1, 10),
        right_path.move_straight_to(centre[0], centre[1] + 2, 10),
        right_path.is_finished


        middle_path = Path()
        middle_path.jump_to(centre[0], centre[1] + 2)
        middle_path.wait(15)
        middle_path.move_straight_to(centre[0] + 7, centre[1] + 2, 10)
        middle_path.wait(50)
        middle_path.is_finished

        effects = [
            Shell(screen, right_path),
            Shell(screen, middle_path),
            Print(screen, StaticRenderer(images=[shell]),
                x=centre[0] - 9,
                y=centre[1])
        ]
        return(Scene(effects, 66), 3)
    elif game_index == 3:
        right_path = Path()
        right_path.jump_to(centre[0] + 7, centre[1] + 2)
        right_path.move_straight_to(centre[0] + 7, centre[1] - 1, 10),
        right_path.move_straight_to(centre[0] - 9, centre[1] - 1, 20),
        right_path.move_straight_to(centre[0] - 9, centre[1] + 2, 10),
        right_path.is_finished


        middle_path = Path()
        middle_path.jump_to(centre[0], centre[1] + 2)
        middle_path.wait(15)
        middle_path.move_straight_to(centre[0] + 7, centre[1] + 2, 10)
        middle_path.wait(50)
        middle_path.is_finished
        
        left_path = Path()
        left_path.jump_to(centre[0] - 9, centre[1] + 2)
        left_path.wait(15)
        left_path.move_straight_to(centre[0], centre[1] + 2, 10)
        left_path.wait(50)
        left_path.is_finished

        effects = [
            Shell(screen, right_path),
            Shell(screen, middle_path),
            Shell(screen, left_path)
        ]
        return(Scene(effects, 85), 3)
    elif game_index == 4:
        right_path = Path()
        right_path.jump_to(centre[0] + 7, centre[1] + 2)
        right_path.wait(15)
        right_path.move_straight_to(centre[0], centre[1] + 2, 10),
        right_path.wait(50)
        right_path.is_finished


        middle_path = Path()
        middle_path.jump_to(centre[0], centre[1] + 2)
        middle_path.wait(15)
        middle_path.move_straight_to(centre[0] - 9, centre[1] + 2, 10)
        middle_path.wait(50)
        middle_path.is_finished
        
        left_path = Path()
        left_path.jump_to(centre[0] - 9, centre[1] + 2)
        left_path.move_straight_to(centre[0] - 9, centre[1] - 1, 10)
        left_path.move_straight_to(centre[0] + 7, centre[1] -1, 20)
        left_path.move_straight_to(centre[0] + 7, centre[1] + 2, 10)
        left_path.wait(50)
        left_path.is_finished

        effects = [
            Shell(screen, right_path),
            Shell(screen, middle_path),
            Shell(screen, left_path)
        ]
        return(Scene(effects, 85), 1)



class KeyboardController(DynamicPath):
    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            key = event.key_code
            if key == 49:
                if (ball_location == 1):
                    Screen.wrapper(win)
                else:
                    Screen.wrapper(lose)
            elif key == 50:
                if (ball_location == 2):
                    Screen.wrapper(win)
                else:
                    Screen.wrapper(lose)
            elif key == 51:
                if (ball_location == 3):
                    Screen.wrapper(win)
                else:
                    Screen.wrapper(lose)
            else:
                return event
        else:
            return event

class X(Sprite):
    def __init__(self, screen):
        super(X, self).__init__(
          screen,
          renderer_dict={
            "default": StaticRenderer(images=[x]),
          },
          path=KeyboardController(
                screen, -1, -1)
        )

class Shell(Sprite):
    def __init__(self, screen, path, start_frame=0, stop_frame=0):
        super(Shell, self).__init__(
          screen,
          renderer_dict={
            "default": StaticRenderer(images=[shell]),
          },
          path=path,
          start_frame=start_frame,
          stop_frame=stop_frame
        )


def play_game(screen):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)

    title_effects = [
        Cycle(
            screen,
            FigletText("SHELL"),
            screen.height // 2 - 6,
            ),
        Cycle(
            screen,
            FigletText("GAME!"),
            screen.height // 2 + 1,
            ),
    ]
    scenes.append(Scene(title_effects, -1))

    middle_path = Path()
    middle_path.jump_to(centre[0], 0)
    middle_path.move_straight_to(centre[0], centre[1] + 2, 15),
    
    left_path = Path()
    left_path.jump_to(centre[0] -9, y=centre[1] + 2)


    intro_effects = [
        Print(screen, StaticRenderer(images=[ball]),
            x=centre[0],
            y=centre[1]),
        Shell(screen, left_path),
        Print(screen, StaticRenderer(images=[shell]),
            x=centre[0] + 7,
            y=centre[1]),
        Shell(screen, middle_path)
    ]
    scenes.append(Scene(intro_effects, 30))
    

    # game scene
    game = get_game(random.randint(1,4), centre, screen)
    global ball_location
    ball_location = game[1]
    scenes.append(game[0])

    intro_effects = [
        Print(screen, StaticRenderer(images=["1"]),
            x=centre[0] - 7,
            y=centre[1] - 1),  
        Print(screen, StaticRenderer(images=[shell]),
            x=centre[0] + 9,
            y=centre[1]),
        Print(screen, StaticRenderer(images=["2"]),
            x=centre[0] + 2,
            y=centre[1] - 1),
        Print(screen, StaticRenderer(images=[shell]),
            x=centre[0],
            y=centre[1]),
        Print(screen, StaticRenderer(images=["3"]),
            x=centre[0] + 11,
            y=centre[1] - 1),
        Print(screen, StaticRenderer(images=[shell]),
            x=centre[0] - 9,
            y=centre[1]),
        X(screen)
    ]
    scenes.append(Scene(intro_effects, -1))

    screen.play(scenes)


def win(screen):
    win_effects = [
            Cycle(
                screen,
                FigletText("YOU"),
                screen.height // 2 - 6,
                ),
            Cycle(
                screen,
                FigletText("WON!"),
                screen.height // 2 + 1,
                ),
        ]
    win_scene = Scene(win_effects, -1)
    screen.play([win_scene])

def lose(screen):
    lose_effects = [
            Cycle(
                screen,
                FigletText("YOU"),
                screen.height // 2 - 6,
                ),
            Cycle(
                screen,
                FigletText("LOST!"),
                screen.height // 2 + 1,
                ),
        ]
    lose_scene = Scene(lose_effects, -1)
    screen.play([lose_scene])


while True:
    try:
        Screen.wrapper(play_game)
        sys.exit(0)
    except ResizeScreenError:
        pass