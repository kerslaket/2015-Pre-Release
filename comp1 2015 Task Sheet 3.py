# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

from datetime import datetime
import pickle
BOARDDIMENSION = 8

class HighScores:
  def __init__(self):
    self.Name = None
    self.Colour = None
    self.Moves = None
    self.Date = None

def display_menu():
  print("Main Menu")
  print("")
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit program")

def get_menu_selection():
  print(" ")
  menuChoice = 0
  while 1 > menuChoice or menuChoice > 6:
    menuChoice = int(input("Please select an option: "))
  return menuChoice

def make_selection(menuChoice,highScores):
  playAgain = "Y"
  if menuChoice == 1:
    SampleGame = "n"
    play_game(SampleGame,highScores)
  if menuChoice == 2:
    print(" ")
  if menuChoice == 3:
    SampleGame = "y"
    play_game(SampleGame,highScores)
  if menuChoice == 4:
    display_high_scores(highScores)
  if menuChoice == 5:
    settingsMenu()
    settingsChoice()
  if menuChoice == 6:
    print("Goodbye")
    save_high_scores(highScores)
    playAgain = "N"
  return playAgain

def display_high_scores(Scores):
  print("\nHigh Scores\n")
  if len(Scores) <= 1:
    print("There are no scores")
  else:
    print("-" * 55)
    print("| {0:<12} | {1:<7} | {2:<15} | {3:<8} |".format("Name","Colour","Moves","Date"))
    for Score in Scores:
      if Score != None:
        print("-" * 55)
        print("| {0:<12} | {1:<7} | {2:<15} | {3:<8} |".format(Score.Name[0:12],Score.Colour,Score.Moves,Score.Date))
    print("-" * 55)
  print(" ")
          
def settingsMenu():
  print("\n1. Use Kashaptu Piece")
  print("9. Return to Main Menu")

def settingsChoice():
  Choice = input("\nPlease Select setting to change: ")
  if Choice == "1":
    global Kashshaptu
    Kashshaptu = input("Do you wish to use the Kashaptu piece (Y/N)? ").lower()[0]
    if Kashshaptu == "y":
      print("Kashshaptu Activated!")
    else:
      print("Kashshaptu Deactivated!")
  
def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  return TypeOfGame.lower()[0]

def DisplayWinner(WhoseTurn, MovesMade):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured in {0} moves.  White wins!".format(round(MovesMade / 2) + 1))
  else:
    print("White's Sarrum has been captured in {0} moves.  Black wins!".format(round(MovesMade / 2)))

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if FileDifference != 0:
    checkRedumMoveIsLegal = False
  elif ColourOfPiece == "W":
    if RankDifference == -2:
      CheckRedumMoveIsLegal = True
      if StartRank != 7:
        CheckRedumMoveIsLegal = False
    elif StartRank == 7:
      CheckRedumMoveIsLegal = True
    elif FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif ColourOfPiece == "B":
    if RankDifference == 2:
      CheckRedumMoveIsLegal = True
      if StartRank != 2:
        CheckRedumMoveIsLegal = False
    if StartRank == 2:
      CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
    CheckNabuMoveIsLegal = True
  RankDifference = StartRank - FinishRank
  FileDifference = StartFile - FinishFile
  if RankDifference > 0 and FileDifference > 0:
    CheckNabuMoveIsLegal = True
    Count = 1
    while Count != RankDifference:
      if Board[StartRank - Count][StartFile - Count] != "  ":
        CheckNabuMoveIsLegal = False
      Count += 1
  if RankDifference > 0 and FileDifference < 0:
    CheckNabuMoveIsLegal = True
    Count = 1
    while Count != RankDifference:
      if Board[StartRank - Count][StartFile + Count] != "  ":
        CheckNabuMoveIsLegal = False
      Count += 1
  if RankDifference < 0 and FileDifference > 0:
    CheckNabuMoveIsLegal = True
    Count = -1
    while Count != RankDifference:
      if Board[StartRank - Count][StartFile + Count] != "  ":
        CheckNabuMoveIsLegal = False
      Count -= 1
  if RankDifference < 0 and FileDifference < 0:
    CheckNabuMoveIsLegal = True
    Count = -1
    while Count != RankDifference:
      if Board[StartRank - Count][StartFile-+ Count] != "  ":
        CheckNabuMoveIsLegal = False
      Count -= 1
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) :
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckKashshaptuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckKashaptuMoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece)
  if CheckKashaptuMoveIsLegal == False:
    CheckKashaptuMoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  if CheckKashaptuMoveIsLegal == False:
    CheckKashaptuMoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  if CheckKashaptuMoveIsLegal == False:
    CheckKashaptuMoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  if CheckKashaptuMoveIsLegal == False:
    CheckKashaptuMoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return CheckKashshaptuMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  else:
    try:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
        if not 0 < FinishRank < 9 or not 0 < FinishFile < 9:
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
        if not 0 < FinishRank < 9 or not 0 < FinishFile < 9:
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "K":
          MoveIsLegal = CheckKashshaptuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
    except IndexError:
      MoveIsLegal = False
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    InitialiseSampleBoard(Board)
  else:
    InitialiseNewBoard(Board)

def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          if Board[RankNo][FileNo] == "B":
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
          elif Board[RankNo][FileNo] == "W":
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          if Board[RankNo][FileNo] == "B":
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif Board[RankNo][FileNo] == "W":
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
          else:
            Board[RankNo][FileNo] = "  "

def InitialiseSampleBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"
                    
def GetMove(StartSquare, FinishSquare, WhoseTurn):
  quitNow = False
  finished = False
  while not finished:
    finished = True
    finished2 = False
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if StartSquare == -1:
        option_menu()
        option = option_choice()
        if option == "2":
          quitNow = True
          return StartSquare, FinishSquare, quitNow
        if option == "4":
          quitNow = True
          if WhoseTurn == "W":
            print("White Surrendered. Black Wins!\n")
          else:
            print("Black Surrendered. White Wins!\n")
          return StartSquare, FinishSquare, quitNow
        finished = False
        finished2 = True
      elif len(str(StartSquare)) != 2:
        print("Please provide both FILE and RANK for this move")
        finished = False
      else:
        while not finished2:
          finished2 = True
          FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
          if FinishSquare == -1:
            option_menu()
            option = option_choice()
            if option == "2":
              quitNow = True
              return StartSquare, FinishSquare, quitNow
            if option == "4":
              quitNow = True
              if WhoseTurn == "W":
                print("White Surrendered. Black Wins!\n")
              else:
                print("Black Surrendered. White Wins!\n")
              return StartSquare, FinishSquare, quitNow
            finished2 = False
          if len(str(FinishSquare)) != 2:
            print("Please provide both FILE and RANK for this move")
            finished2 = False
            finished = False
    except ValueError:
      print("Please provide an appropriate answer")
      finished = False
  return StartSquare, FinishSquare, quitNow

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  global Kashshaptu
  if Kashshaptu == "y":
    Initial = "K"
    Name = "Kashaptu"
  else:
    Initial = "M"
    Name = "Marzaz Pani"
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "W{0}".format(Initial)
    Board[StartRank][StartFile] = "  "
    print("White Redum Promoted To {0}".format(Name))
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "B{0}".format(Initial)
    Board[StartRank][StartFile] = "  "
    print("Black Redum Promoted To {0}".format(Name))
  else:
    try:
      colour1, piece1, = GetPieceName(Board,StartRank,StartFile)
      colour2, piece2, = GetPieceName(Board,FinishRank,FinishFile)
      print("{0} {1} Takes {2} {3}".format(colour1, piece1, colour2, piece2))
    except UnboundLocalError:
      colour1, piece1, = GetPieceName(Board,StartRank,StartFile)
      print("{0} {1} Moves to a blank space".format(colour1, piece1))
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    
def ConfirmMove(StartSquare, FinishSquare):
  print("Move from File {0}, Rank {1} to File {2}, Rank {3}? ".format(str(StartSquare)[0],str(StartSquare)[1],str(FinishSquare)[0],str(FinishSquare)[1]))
  confirmation = input("Confirm Move (Yes/No): ")
  return confirmation.lower()[0]

def GetPieceName(Board, Rank, File):
  PieceType = Board[Rank][File][1]
  PieceColour = Board[Rank][File][0]
  if PieceColour == "W":
    colour = "White"
  elif PieceColour == "B":
    colour = "Black"
  if PieceType == "R":
    piece = "Redum"
  elif PieceType == "S":
    piece = "Sarrum"
  elif PieceType == "M":
    piece = "MarzazPani"
  elif PieceType == "G":
    piece = "Gisgigir"
  elif PieceType == "N":
    piece = "Nabu"
  elif PieceType == "E":
    piece = "Etlu"
  elif PieceType == "K":
    piece = "Kashshaptu"
  return colour, piece

def option_menu():
  print("Options")
  print(" ")
  print("1. Save Game")
  print("2. Quit To Menu")
  print("3. Return To Game")
  print("4. Surrender")

def option_choice():
  choice = input("\nPlease select an option: ")
  if choice == "1":
    print("This should probably save the game")
    option = "1"
  if choice == "2":
    option = "2"
  if choice == "3":
    print("\nReturning To Game\n")
    option = "3"
  if choice == "4":
    print("\nSurrendering...\n")
    option = "4"
  return option

def AddHighScore(highScores,WhoseTurn,MovesMade):
  highScores.append(HighScores())
  highScores[len(highScores) - 1].Name = input("Please enter your name for the high score table: ")
  highScores[len(highScores) - 1].Colour = WhoseTurn
  highScores[len(highScores) - 1].Moves = MovesMade
  highScores[len(highScores) - 1].Date = datetime.now().strftime("%d/%m/%y")

def save_high_scores(scores):
  with open("HighScores.dat", mode = "wb") as HighScores_Files:
    pickle.dump(scores,HighScores_Files)

def load_high_scores():
  
def play_game(SampleGame, highScores):
  MovesMade = 0
  StartSquare = 0 
  FinishSquare = 0
  WhoseTurn = "W"
  GameOver = False
  if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
    SampleGame = chr(ord(SampleGame) - 32)
  InitialiseBoard(Board, SampleGame)
  while not(GameOver):
    DisplayBoard(Board)
    DisplayWhoseTurnItIs(WhoseTurn)
    MoveIsLegal = False
    skip = False
    while not(MoveIsLegal):
      StartSquare, FinishSquare, quitNow = GetMove(StartSquare, FinishSquare, WhoseTurn)
      if quitNow == True:
        return
      confirmation = ConfirmMove(StartSquare, FinishSquare)
      if confirmation == "y":
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if confirmation == "n":
        skip = True
      if not(MoveIsLegal) and not skip:
        print("That is not a legal move - please try again")
    GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
    MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
    if GameOver:
      DisplayWinner(WhoseTurn,MovesMade)
    if WhoseTurn == "W":
      WhoseTurn = "B"
      LastTurn = "W"
    else:
      WhoseTurn = "W"
      LastTurn = "B"
    MovesMade += 1
  AddName = input("Do you want to add your name to the highscore list? (Y/N): ").lower()[0]
  if AddName == "y":
    AddHighScore(highScores, LastTurn, MovesMade)
  PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
  if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
    PlayAgain = chr(ord(PlayAgain) - 32)

if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  PlayAgain = "Y"
  global Kashashptu
  Kashshaptu = "n"
  highScores = [None]
  while PlayAgain == "Y":
    display_menu()
    menuChoice = get_menu_selection()
    PlayAgain = make_selection(menuChoice,highScores)
  



