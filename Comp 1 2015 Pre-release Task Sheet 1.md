
##Question 2

1. An error message is displayed
2. The piece is moved to a non existent space not on the board and the game continues as normal
3. The piece is moved to a non existent space not on the board and the game continues as normal
4. An error message is displayed
5. All of the moves involving pieces being moved to squares with a 0 coordinate carry on as normal but if a coordinate contains a 9 then an error occurs
6. CheckMoveIsLegal()

##Question 3

1. GetMove(StartSquare, FinishSquare)

##Question 5

1. The program returns the StartRank and the StartFile or the FinishRank and FinishFIle. These Values are then used to determine the piece based on what piece is listed in that position in the parameter Board.

3. MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)

##Question 6
1. def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):

##Question 7
1. def DisplayBoard(Board)

##Question 8
1.
|Role|Description|
|-----|--------------|
|Fixed Value|A variable that has a hard coded value that should not be changed|
|Stepper|A variable often used as a counter that is incremented or decremented usually to keep track of repetitions in while loops|
|Most Recent Holder|The most recent value interacted with by the program|
|Most Wanted Holder|A variable holding the most appropriate value attained thus far for the task|
|Gatherer|A variable containing the accumulative value of another set of variables|
|Transformation|A variable which has its value determined based on the values of other variables|
|Follower|A variable which has its value copied from another variable|
|Temporary|A variable which has a value that is only stored for a small amount of time|

2.
|Role|Example|
|-----|--------------|
|Fixed Value|BOARDDIMENSION|
|Stepper|Count|
|Most Recent Holder|StartSquare|
|Most Wanted Holder|No Example|
|Gatherer|No Example|
|Transformation|StartRank|
|Follower|Board[FinishRank][FinishFile]|
|Temporary|No Example|

##Question 3
1. When passing by value the value of the variable that's called is copied to the functions parameter while when passing by reference a reference that directs the program to the correct memory location is passed as the parameter.

2. 
|Function| Mechanism|
|--------|----------|
|CreateBoard()|No Parameters|
|DisplayWhoseTurnItIs(WhoseTurn)|Value|
|GetTypeOfGame()|No Parameters|
|DisplayWinner(WhoseTurn)|Value|
|CheckIfGameWillBeWon(Board, FinishRank, FinishFile)|Reference, Value, Value|
|DisplayBoard(Board)|Reference|
|Check(insert piece name here)MoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)|Reference, Value, Value, Value, Value|
|CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)|Reference, Value, Value, Value, Value, Value|
|InitialiseBoard(Board, SampleGame)|Reference, Value|
|MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)|Reference, Value, Value, Value, Value, Value|
|ConfirmMove(StartSquare, FinishSquare)|Value, Value|
|GetPieceName(Board, Rank, File)| Reference, Value, Value|

> Written with [StackEdit](https://stackedit.io/).