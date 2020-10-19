"""
Tracy has a file that contains a list of actors and the movies in which they acted.
She wants to know the top 3 ranked actors from her list whom have acted/appeared in the most movies.

Question:
Write code in Java/Scala/Python to display the top 3 ranked actors appearing in the most movies based on the count of movies
in which they have acted. If there are less than 3 actors in her list, display all of them.
Consider all scenarios - such as, if two actors have acted in the same number of movies, they will have the same rank.

Input Explanation
The first line of input is always an integer denoting how many lines to read after the first line.
In our sample test case, we have 7 in the first line and 7 lines after the first line, each having an actor name and movie name.
In each data line, the actor name and movie name are separated by a ','(comma).

Input
8
Leonardo DiCaprio,The Revenant
Christian Bale,Vice
Morgan Freeman,Shawshank Redemption
Leonardo DiCaprio,The Great Gatsby
Christian Bale,American Psycho
Morgan Freeman,The Dark Knight
Christian Bale,The Dark Knight
Samuel L. Jackson,Pulp Fiction

Output Explanation
Print the top actor names to standard output in alphabetical order.
You should not have counts in the output, only actor names
Output
Christian Bale
Leonardo DiCaprio
Morgan Freeman
"""
import sys

num = int(sys.stdin.readline())
print(num)

inputs = {}
for n in range(num):
    inp = sys.stdin.readline().split(",")
    inputs[inp[0]] = inputs.get(inp[0], 0) + 1

values = sorted(list(set(inputs.values())), key=lambda v: -v)
pos_rng = values[-1] if len(values) <= 3 else values[2]
print(pos_rng)
output = {k: v for k, v in inputs.items() if v >= pos_rng}

result = [k for k, v in sorted(output.items(), key=lambda item: item[0])]
for res in result:
    print(res)

"""
Input:
12
A1,M1
A2,M1
A3,M1
A4,M1
A5,M2
A6,M2
A7,M3
A8,M3
A9,M3
A10,M3
A11,M3
A12,M4

Output:
A1
A10
A11
A12
A2
A3
A4
A5
A6
A7
A8
A9
"""