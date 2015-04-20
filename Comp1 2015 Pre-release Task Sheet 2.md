##Question 11
1. display_menu() - This function will display the options on the menu
    get_menu_selection() - Get the user input from the menu choice
    Make_selection(menuChoice) - Loads the correct option that the user entered
    play_game() - Starts a new game

##Question 12
1. GetMove(StartSquare, FinishSquare)

##Question 14
1. Refactoring is the process of rewriting or restructuring code so that it is more maintainable, or more efficient while still having the same perceived behaviour. 

##Question 15
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

##Task 20

When passing by value the value of the variable that's called is copied to the functions parameter while when passing by reference a reference that directs the program to the correct memory location is passed as the parameter.

 
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
|display_menu()|None|
|get_menu_selection()|None|
|make_selection(menuChoice)|Value|
|play_game()|None|
|option_menu()|None|
|option_choice()|None|
|InitialiseNewBoard(Board)|Reference|
|InitialiseSampleBoard()|Reference|

> Written with [StackEdit](https://stackedit.io/).