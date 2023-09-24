# object-oriented-design

### Modified Connect Four Game Rules

#### Objective
The goal is to be the first to connect four of one's own discs, either horizontally, vertically, or diagonally, but with a twist in how the "connection" is defined.

#### Board Setup
The game is played on a grid that has "7" rows and "6" columns, making a total of 42 slots. You can change the number of rows or columns. 

#### Game Play

1. **Starting the Game**: Players decide who goes first, often by coin toss.
2. **Taking Turns**: Players take turns dropping one of their colored discs from the top into any of the seven column slots.
3. **Falling Discs**: Discs must fall to the lowest available slot within the chosen column.
4. **Connection Criteria**: Unlike traditional Connect Four, a disc is considered "connected" to another disc with the same color if it is placed adjacent to it in either the right, left, top, or bottom direction. Diagonal connections do not count in this modified version.
5. **Winning**: The first player to get ${Winning Length} of their discs "connected" wins the game.

#### Additional Rules and Constraints

1. **Full Column**: Players cannot add a disc to a full column.
2. **Draw**: If all slots are filled and no one has connected four discs, the game is a draw. (**Not implemented yet**)
3. **Winning Length**: Before the game starts, players agree on the length of the sequence required to win, and this value is stored in the variable winning_length.
