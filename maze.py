from random import seed, shuffle
from node import Node
import logging as log
import sys

sys.setrecursionlimit(10000)

class Maze:
    def __init__(self, size: int, maze_seed: int = None) -> None:
        if(size > 70):
            size = 70

        self.size = size
        self.maze = [[Node((i,j)) for i in range(size)] for j in range(size)] # set maze as 2d list of nodes with their positions marked
        seed(maze_seed)

        # initialize each node's neighbors
        for i in range(0, size):
            for j in range(0, size):
                up_node = self.maze[i][j - 1] if j > 0 else None
                down_node = self.maze[i][j + 1] if j < size - 1 else None
                left_node = self.maze[i - 1][j] if i > 0 else None
                right_node = self.maze[i + 1][j] if i < size - 1 else None
                
                self.maze[i][j].neighbors = {"up": up_node, "down": down_node, "left": left_node, "right": right_node}

        self.bfs_generate(self.maze[0][0]) # generate from top-left corner

    def __str__(self) -> str:
        out = ""

        for j in range(self.size):
            layer1 = ""
            layer2 = ""
            layer3 = ""

            for i in range(self.size):
                print(self.maze[i][j])
                lateral_length = self.size // 2 * 2 if (self.size // 2 * 2 > 3) else 2
                vertical_length = self.size // 3 if (self.size // 3 > 1) else 1

                if(not self.maze[i][j].connections['up']):
                    layer1 += "0" + "-" * (lateral_length) + "0"
                else:
                    layer1 += "0" + " " * (lateral_length) + "0"

                if(not self.maze[i][j].connections['left']):
                    layer2 += "|"
                else:
                    layer2 += " "
                
                layer2 += " " * lateral_length

                if(not self.maze[i][j].connections['right']):
                    layer2 += "|"
                else:
                    layer2 += " "

                if(not self.maze[i][j].connections['down']):
                    layer3 += "0" + "-" * lateral_length + "0"
                else:
                    layer3 += "0" + " " * lateral_length + "0"
                
            out += layer1 + "\n" + (layer2 + "\n") * vertical_length + layer3 + "\n"

        return out
    
    def bfs_generate(self, node: Node) -> None:
        neighbors = node.neighbors
        directions = ["up", "down", "left", "right"]

        shuffle(directions)
        node.visited = True

        for k in directions:
            if(neighbors[k] is None or neighbors[k].visited):
                continue

            node.set_connection(k)
            self.bfs_generate(node.neighbors[k])