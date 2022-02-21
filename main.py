import time
from numpy import number
import pygame
import os
from pygame.locals import *
from pygame import mixer


def load(file, type):
  if type == "img":
    return pygame.image.load(file)
  elif type == "sound":
    return mixer.Sound(file)
  elif type == "music":
    return mixer.music.load(file)

def cursorIsAt(x, y, offsetX, offsetY):
  pos = pygame.mouse.get_pos()
  xpos = pos[0]
  ypos = pos[1]
  if xpos > x and ypos > y and xpos < (x + offsetX) and ypos < (y + offsetY):
    return True
  else:
    return False

def button(x, y, weight, height, texture, textureLit):
  if cursorIsAt(x, y, weight, height):
    screen.blit(textureLit, (x, y))
    if event.type == pygame.MOUSEBUTTONDOWN:
      return True
    else:
      return False
  else:
    screen.blit(texture, (x, y))
    return False

def holeNumber(number):
  number = str(number)
  if number.find("."):
    return int(number[:number.find(".")])
  else:
    return int(number)

def printNum(x, y, number):
  number = str(number)
  offset = 0
  if len(number) == 1:
    screen.blit(number0, (x, y))
    offset = 32
  for i in number:
    x = x + offset
    if i == "0":
      screen.blit(number0, ((x + offset), y))
    if i == "1":
      screen.blit(number1, ((x + offset), y))
    if i == "2":
      screen.blit(number2, ((x + offset), y))
    if i == "3":
      screen.blit(number3, ((x + offset), y))
    if i == "4":
      screen.blit(number4, ((x + offset), y))
    if i == "5":
      screen.blit(number5, ((x + offset), y))
    if i == "6":
      screen.blit(number6, ((x + offset), y))
    if i == "7":
      screen.blit(number7, ((x + offset), y))
    if i == "8":
      screen.blit(number8, ((x + offset), y))
    if i == "9":
      screen.blit(number9, ((x + offset), y))
    offset = offset + 32

version = "Alpha 0.0"

pygame.init()

screen_width = 512
screen_height = 576

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('_ChESS')
programIcon = load('black_king.png', "img")
pygame.display.set_icon(programIcon)

# load sounds
game_start = load("game_start.wav", "sound")
game_end = load("game_end.wav", "sound")
game_end_stalemate = load("game_end_stalemate.wav", "sound")
game_end_checkmate = load("game_end_checkmate.wav", "sound")
game_move = load("game_move.wav", "sound")
game_capture = load("game_capture.wav", "sound")
game_castle = load("game_castle.wav", "sound")
game_check = load("game_check.wav", "sound")

menu_click = load("menu_click.wav", "sound")

# load boards
board1 = load("board1.png", "img")
board1mini = load("board1mini.png", "img")
board2 = load("board2.png", "img")
board2mini = load("board2mini.png", "img")
board3 = load("board3.png", "img")
board3mini = load("board3mini.png", "img")

# load menu parts
menuimg = load("menu.png", "img")
playBtn = load("playBtn.png", "img")
playBtnLit = load("playBtnLit.png", "img")
styleBtn = load("styleBtn.png", "img")
styleBtnLit = load("styleBtnLit.png", "img")
arrow_right = load("arrow_right.png", "img")
arrow_left = load("arrow_left.png", "img")
arrow_rightLit = load("arrow_rightLit.png", "img")
arrow_leftLit = load("arrow_leftLit.png", "img")
backBtn = load("backBtn.png", "img")
backBtnLit = load("backBtnLit.png", "img")
gameSettings = load("gameSettings.png", "img")
playGameBtn = load("playGameBtn.png", "img")
playGameBtnLit = load("playGameBtnLit.png", "img")
smallArrowUp = load("smallArrowUp.png", "img")
smallArrowUpLit = load("smallArrowUpLit.png", "img")
smallArrowDown = load("smallArrowDown.png", "img")
smallArrowDownLit = load("smallArrowDownLit.png", "img")
twoDots = load("twoDots.png", "img")

# load numbers
number0 = load("number0.png", "img")
number1 = load("number1.png", "img")
number2 = load("number2.png", "img")
number3 = load("number3.png", "img")
number4 = load("number4.png", "img")
number5 = load("number5.png", "img")
number6 = load("number6.png", "img")
number7 = load("number7.png", "img")
number8 = load("number8.png", "img")
number9 = load("number9.png", "img")

# load pieces
pieces = {}

wpawn_img = load('white_pawn.png', "img")
wrook_img = load('white_rook.png', "img")
wknight_img = load('white_knight.png', "img")
wbishop_img = load('white_bishop.png', "img")
wqueen_img = load('white_queen.png', "img")
wking_img = load('white_king.png', "img")

pieces["wpawn"] = wpawn_img
pieces["wrook"] = wrook_img
pieces["wknight"] = wknight_img
pieces["wbishop"] = wbishop_img
pieces["wqueen"] = wqueen_img
pieces["wking"] = wking_img

bpawn_img = load('black_pawn.png', "img")
brook_img = load('black_rook.png', "img")
bknight_img = load('black_knight.png', "img")
bbishop_img = load('black_bishop.png', "img")
bqueen_img = load('black_queen.png', "img")
bking_img = load('black_king.png', "img")

pieces["bpawn"] = bpawn_img
pieces["brook"] = brook_img
pieces["bknight"] = bknight_img
pieces["bbishop"] = bbishop_img
pieces["bqueen"] = bqueen_img
pieces["bking"] = bking_img

# load game textures

frame = load("frame.png", "img")
blankFrame = load("blankFrame.png", "img")
litFrame = load("litFrame.png", "img")

board = board1
choosen = 0
positions = {}

class piece():
  global positions

  def __init__(self, path): # i dont actually know why this needs to be there but it doesen't work without it :\
    pass

  def put(piece, field): # puts piece on specified field
    global positions
    fieldStr = "field" + str(field[0]) + str(field[1])
    positions[fieldStr] = piece

  def whatIs(field): # returns name of piece on specified field
    global positions
    fieldStr = "field" + str(field[0]) + str(field[1])
    if fieldStr in positions:
      if positions[fieldStr] != None:
        name = positions[fieldStr]
        return name
    return None

  def move(field, newField): # for moving with pieces form one position to new one
    piece.put(piece.whatIs(field), newField)
    piece.put(None, field)

  def isLegalMove(pieceField, moveField):
    if pieceField != moveField:
      if piece.whatIs(pieceField) == "wpawn": # /////////////////////////////////////////////// white pawn
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("b"):
          if pieceField[0] - 2 == moveField[0] and pieceField[1] == moveField[1] and pieceField[0] == 7:
            return True
          elif pieceField[0] - 1 == moveField[0] and pieceField[1] == moveField[1] and piece.whatIs(moveField) == None:
            return True
          elif pieceField[0] - 1 == moveField[0] and pieceField[1] != moveField[1] and str(piece.whatIs(moveField)).startswith("b"):
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "bpawn": # /////////////////////////////////////////////// black pawn
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("w"):
          if pieceField[0] + 2 == moveField[0] and pieceField[1] == moveField[1] and pieceField[0] == 2:
            return True
          elif pieceField[0] + 1 == moveField[0] and pieceField[1] == moveField[1] and piece.whatIs(moveField) == None:
            return True
          elif pieceField[0] + 1 == moveField[0] and pieceField[1] != moveField[1] and str(piece.whatIs(moveField)).startswith("w"):
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "wking": # /////////////////////////////////////////////// white king
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("b"):
          if pieceField[0] + 1 == moveField[0] or pieceField[0] - 1 == moveField[0] or pieceField[0] == moveField[0]:
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1] or pieceField[1] == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "bking": # /////////////////////////////////////////////// black king
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("w"):
          if pieceField[0] + 1 == moveField[0] or pieceField[0] - 1 == moveField[0] or pieceField[0] == moveField[0]:
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1] or pieceField[1] == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "wknight": # /////////////////////////////////////////////// black knight
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("b"): 
          if pieceField[0] + 2 == moveField[0] or pieceField[0] - 2 == moveField[0]:
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1]:
              return True
          if pieceField[0] + 1 == moveField[0] or pieceField[0] - 1 == moveField[0]:
            if pieceField[1] + 2 == moveField[1] or pieceField[1] - 2 == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "bknight": # /////////////////////////////////////////////// white knight
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("w"): 
          if pieceField[0] + 2 == moveField[0] or pieceField[0] - 2 == moveField[0]:
            if pieceField[1] + 1 == moveField[1] or pieceField[1] - 1 == moveField[1]:
              return True
          if pieceField[0] + 1 == moveField[0] or pieceField[0] - 1 == moveField[0]:
            if pieceField[1] + 2 == moveField[1] or pieceField[1] - 2 == moveField[1]:
              return True

      elif piece.whatIs(pieceField) == "wrook": # /////////////////////////////////////////////// white rook
        if piece.whatIs(moveField) == None or str(piece.whatIs(moveField)).startswith("b"):
          checkField = moveField
          if moveField[1] == pieceField[1]: # moving up or down
            if moveField[0] < pieceField[0]:
              for i in range(pieceField[0] - moveField[0] - 1):
                checkField = checkField 
                pass
            else:
              pass
          elif moveField[0] == pieceField[0]: # moving left or right
            case = "x"
    return False

  def render(): # for rendering all pieces on the borad
    field = [0, 0]
    for i in range(8):
      for o in range(8):
        field[0] = i + 1
        field[1] = o + 1
        name = piece.whatIs(field)
        if name != None:
          if name.startswith("w"): # white or black piece
            color = "w"
          else:
            color = "b"
          name = name[1:]
          x = field[1] * 64 - 64
          y = field[0] * 64
          screen.blit(pieces[color + name], (x, y))

def choose_style():
  global event
  global board
  global choosen
  run = True
  while run:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    screen.blit(menuimg, (0, 64)) # Backround

    if button(64, 400, 64, 96, arrow_left, arrow_leftLit):
      menu_click.play()
      if choosen > 0:
        choosen = choosen - 1
      else:
        choosen = 2
      time.sleep(0.2)
    
    if button(384, 400, 64, 96, arrow_right, arrow_rightLit):
      menu_click.play()
      if choosen < 2:
        choosen = choosen + 1
      else: 
        choosen = 0
      time.sleep(0.2)

    if button(28, 215, 64, 68, backBtn, backBtnLit):
      menu_click.play()
      run = False
      time.sleep(0.2)
    
    if choosen == 0:
      screen.blit(board1mini, (184, 380))
      board = board1
    elif choosen == 1:
      screen.blit(board2mini, (184, 380))
      board = board2
    elif choosen == 2:
      screen.blit(board3mini, (184, 380))
      board = board3

    pygame.display.update()

def settings():
  global event
  minutes = 30
  hours = 0
  run = True
  while run:

    screen.blit(board1, (0, 64))
    screen.blit(gameSettings, (116, 100))

    printNum(280, 330, str(minutes)) # display minutes
    printNum(120, 330, str(hours)) # display hours

    screen.blit(twoDots, (240, 350)) # Two dots

    if button(315, 500, 192, 72, playGameBtn, playGameBtnLit):
      game_start.play()
      time.sleep(0.1)
      game()
    
    if button(28, 128, 64, 68, backBtn, backBtnLit):
      menu_click.play()
      run = False
      time.sleep(0.1)

    if button(192, 280, 32, 32, smallArrowUp, smallArrowUpLit):
      if hours < 24:
        hours = hours + 1
        time.sleep(0.1)

    if button(192, 445, 32, 32, smallArrowDown, smallArrowDownLit):
      if hours > 0:
        hours = hours - 1
        time.sleep(0.1)

    if button(352, 280, 32, 32, smallArrowUp, smallArrowUpLit):
      if minutes < 59:
        minutes = minutes + 1
        time.sleep(0.1)
      elif minutes == 59 and hours < 24:
        minutes = 0
        hours = hours + 1

    if button(352, 445, 32, 32, smallArrowDown, smallArrowDownLit):
      if minutes > 0:
        minutes = minutes - 1
        time.sleep(0.1)

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

def game():
  run = True
  piece.put("brook", [1, 1])    # black pieces
  piece.put("bknight", [1, 2])
  piece.put("bbishop", [1, 3])
  piece.put("bqueen", [1, 4])
  piece.put("bking", [1, 5])
  piece.put("bbishop", [1, 6])
  piece.put("bknight", [1, 7])

  piece.put("brook", [1, 8])
  piece.put("bpawn", [2, 1])
  piece.put("bpawn", [2, 2])
  piece.put("bpawn", [2, 3])
  piece.put("bpawn", [2, 4])
  piece.put("bpawn", [2, 5])
  piece.put("bpawn", [2, 6])
  piece.put("bpawn", [2, 7])
  piece.put("bpawn", [2, 8])


  piece.put("wrook", [8, 1])    # white pieces
  piece.put("wknight", [8, 2])
  piece.put("wbishop", [8, 3])
  piece.put("wqueen", [8, 4])
  piece.put("wking", [8, 5])
  piece.put("wbishop", [8, 6])
  piece.put("wknight", [8, 7])
  piece.put("wrook", [8, 8])

  piece.put("wpawn", [7, 1])
  piece.put("wpawn", [7, 2])
  piece.put("wpawn", [7, 3])
  piece.put("wpawn", [7, 4])
  piece.put("wpawn", [7, 5])
  piece.put("wpawn", [7, 6])
  piece.put("wpawn", [7, 7])
  piece.put("wpawn", [7, 8])

  piece.put("wrook", [6, 5])

  choosen = None
  onTurn = "white"

  while run:
    global event

    screen.blit(board, (0, 64)) # Backround

    piece.render()
    
    pos = pygame.mouse.get_pos()
    x = holeNumber(pos[0] / 64)
    y = holeNumber(pos[1] / 64)
    x = x + 1
    screen.blit(frame, (x * 64 - 64, y * 64))

    if choosen:
      screen.blit(litFrame, (choosen[1] * 64 - 64, choosen[0] * 64))

    if event.type == pygame.MOUSEBUTTONDOWN:
      selected = [y, x]

      if choosen == None and piece.whatIs(selected) != None:
        if str(piece.whatIs(selected)).startswith("w") and onTurn == "white":
          print("Choosed " + str(selected))
          choosen = selected
        elif str(piece.whatIs(selected)).startswith("b") and onTurn == "black":
          print("Choosed " + str(selected))
          choosen = selected
      elif selected == choosen:
        print("Unchosed " + str(selected))
        choosen = None
      elif choosen != None:
        print("Played " + str(choosen) + " to " + str(selected))
        if piece.isLegalMove(choosen, selected):
          print("Is legal move")
          piece.move(choosen, selected)
          if onTurn == "white":
            onTurn = "black"
          else:
            onTurn = "white"
        else:
          print("Not a legal move")
        choosen = None
      time.sleep(0.15)

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

screen.blit(menuimg, (0, 64))

while True: # Game menu

  screen.blit(menuimg, (0, 64)) # Menu backround

  if button(168, 320, 176, 88, playBtn, playBtnLit):
    menu_click.play()
    time.sleep(0.1)
    settings()
  
  if button(168, 420, 176, 88, styleBtn, styleBtnLit):
    menu_click.play()
    time.sleep(0.1)
    choose_style()

  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()