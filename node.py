class Node:
        def __init__(self, pos: tuple = (-1, -1)) -> None:
            self.pos = pos
            self.visited = False

            self.neighbors = {
                'up': None,
                'down': None,
                'left': None,
                'right': None
            }

            self.connections = {
                'up': False,
                'down': False,
                'left': False,
                'right': False
            }
        
        def __str__(self) -> str:
            out = f"{self.pos}: up="

            if(self.neighbors['up'] != None):
                out += str(self.neighbors['up'].pos) + "\tdown="
            else:
                out += "None\tdown="

            if(self.neighbors['down'] != None):
                out += str(self.neighbors['down'].pos) + "\tleft="
            else:
                out += "None\tleft="

            if(self.neighbors['left'] != None):
                out += str(self.neighbors['left'].pos) + "\tright="
            else:
                out += "None\tright="

            if(self.neighbors['right'] != None):
                out += str(self.neighbors['right'].pos)
            else:
                out += "None"
            
            return out

        def set_connection(self, direction: str, status: bool = True) -> None:
            self.connections[direction] = status

            if(self.neighbors[direction] is not None):
                self.neighbors[direction].connections[self.direction_opposite(direction)] = status

        def set_connections(self, directions: dict) -> None:
            self.set_connection("up", directions["up"])
            self.set_connection("down", directions["down"])
            self.set_connection("left", directions["left"])
            self.set_connection("right", directions["right"])  
        
        def connection_count(self) -> int:
            out = 0

            if(self.connections['up']):
                out += 1
            
            if(self.connections['down']):
                out += 1

            if(self.connections['left']):
                out += 1

            if(self.connections['right']):
                out += 1

            return out

        def direction_opposite(self, direction: str) -> str:
            if(direction == "up"):
                return "down"
            elif(direction == "left"):
                return "right"
            elif(direction == "right"):
                return "left"
            elif(direction == "down"):
                return "up"
            
            raise Exception(f"{direction}: invalid direction")