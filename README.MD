# Mancala
This project implements an AI player for the game Mancala. The goal was to design, implement, and evaluate a program capable of playing Mancala competitively against both random agents and human players.

Our solution is based on the Minimax algorithm with alpha-beta pruning, supported by a custom evaluation function to guide decisions under time constraints.

## Game Rules
- Each player has 6 pits, each starting with 4 stones, and a store to the right.
- A turn consists of choosing a pit, sowing its stones counterclockwise into subsequent pits and the player’s store.
- If the last stone lands in the player’s store, they get an extra turn.
- If the last stone lands in one of the player’s own empty pits, they capture stones from the opposite pit.
- The game ends when one player’s pits are empty. Remaining stones go into the opponent’s store.
- The winner is the player with the most stones in their store.

## AI Implementation
### Algorithm
- Minimax search with alpha-beta pruning to reduce the number of explored states.
- Time-limited search (1 second per move).

### Evaluation Function (Heuristic)
Our heuristic prioritizes:
1. Extra turns (highest weight, ×4).
2. Capturing opponent stones.
3. Sowing into the store.
4. Difference in stone count between player and opponent.

## Results & Observations
- Careful heuristic design significantly improved search depth and win rate.
- Alpha-beta pruning reduced runtime enough to allow meaningful strategic play.
- Extra turns proved to be the most decisive factor in gameplay.