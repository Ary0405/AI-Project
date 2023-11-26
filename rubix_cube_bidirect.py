from collections import deque
from rubix_cube_display import display_cube
from rubix_cube_move import apply_move

def bidirectional_search(scrambledCube, solved_state, possibleMoves, n, pattern_db, heuristic):
   # Convert lists to tuples to make them hashable
   scrambledCube = tuple(tuple(row) for row in map(tuple, scrambledCube))
   solved_state = tuple(tuple(row) for row in map(tuple, solved_state))

   # Initialize the forward and backward frontiers
   forward_frontier = deque([(scrambledCube, [])]) # Store the moves along with the state
   backward_frontier = deque([(solved_state, [])]) # Store the moves along with the state

   # Initialize the forward and backward explored sets
   forward_explored = {scrambledCube: []} # Store the moves along with the state
   backward_explored = {solved_state: []} # Store the moves along with the state

   while forward_frontier and backward_frontier:
       # Expand the forward frontier
       cube_state, moves_so_far = forward_frontier.popleft()
       for move in possibleMoves:
           neighbor = apply_move([list(row) for row in cube_state], move)
           neighbor = tuple(tuple(row) for row in neighbor)
           if neighbor in backward_explored:
               return moves_so_far + [move] + backward_explored[neighbor][::-1] # Combine the moves
           if neighbor not in forward_explored:
               forward_frontier.append((neighbor, moves_so_far + [move])) # Store the moves along with the state
               forward_explored[neighbor] = moves_so_far + [move] # Store the moves along with the state

       # Expand the backward frontier
       cube_state, moves_so_far = backward_frontier.popleft()
       for move in possibleMoves:
           neighbor = apply_move([list(row) for row in cube_state], move)
           neighbor = tuple(tuple(row) for row in neighbor)
           if neighbor in forward_explored:
               return forward_explored[neighbor] + [move] + moves_so_far[::-1] # Combine the moves
           if neighbor not in backward_explored:
               backward_frontier.append((neighbor, moves_so_far + [move])) # Store the moves along with the state
               backward_explored[neighbor] = moves_so_far + [move] # Store the moves along with the state

   # If no solution was found, return None
   return None
