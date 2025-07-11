# CODER-assignment2

## Setup 

### Required Packages
This project requires the following Python packages:
- `colorama` 
- `random` 
- `math` 

Both random and math are inbuilt to python, colorama must be installed.
If coloarama is not installed the game will not run
Please run: `pip install colorama`
 

### About the project 
This connect 4 game allows you to pick a player agent and an opponent agent
Each of the following is an agent:
- Player - the basic playable character
- Randobot - picks a random move, does not know how to win
- Monte Carlo Agent - A much more complex agent that will play the game well

You can play the project by running:
`python connect_four.py`

### Monte Carlo Agent
The monte carlo agent uses a monte carlo tree search to find which moves to explore, and which to ignore.
While it does this it makes sure that winning moves are explored much more, while unexplored moves gain at least
some exploration.
The formula for deciding which node to explore is as follows:

$\frac{w}{n} + c \sqrt{\frac{\ln N}{n}}$

This is the Upper Confidence Bound for Trees (UCBT) formula, commonly used in other Monte Carlo tree search algorithms
To change the difficulty of the AI we just change how many iterations the agent gets when exploring.

The steps of the agent are as follows:
#### Selection
Find a node that is unexplored, using the UCBT formula it finds a node, then travels through that nodes best child and continues until a unexplored option is found

#### Expansion
We choose a random valid move to make from this nodes board, then return the node

#### Rollout
With this node we simulate a game, and return who the winner was ('X' 'O' or draw)

#### Back propagation
We then update all nodes visits by +1 and its win if it is the corresponding peice. Ie. a board that played a 'O' move gains a point if 'O' won the rollout
Drawn boards also add 0.5 to the score, so the agent also accounts for that option

Note: Because of how backpropagation works we account for the best move for X and O regardless if its the agents piece. We do this because we also expect the other player to make their best move. 



There are many methods to improve this agent:
- making it so that each rollout is not a randomly played game and the agent uses logic (ie connecting 4 from 3, playing towards the center etc)
however I felt it was sufficient for this project

## Legal

### Colorama 
- BSD licence (Open-source)
- found here: https://pypi.org/project/colorama/
- This means that Colorama is free and open source, as long as credits are kept for the original author

### Random + Math
T-hese are inbuilt python libaries, so they are under the availble for commercial and private use
