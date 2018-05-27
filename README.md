# search
Generic search algorithm implementations. Includes Breadth First Search, Depth First Search and A*

Sample Usage:

```python
import problem
import search

# Define the problem
adjacency_matrix = [
  [0, 1, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0]]

start = 4
end = 0
spp = problem.ShortestPathProblem(adjacency_matrix, start, end)

# Choose a search algorithm
a = search.BestFirstSearch()

# Get the solution
s = a.solve(spp)
```
