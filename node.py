from enum import Enum

class NodeState(Enum):
    BLANK = 0
    WALL = 1
    START = 2
    TARGET = 3
    PATH = 4
    CLOSED = 5
    OPEN = 6

class Node:
    def __init__(self, row, col, parent):
        self.row = row
        self.col = col
        self.parent = parent
        self.g_score = float('inf')
    
    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def get_coords(self):
        return (self.row, self.col)
    
    def get_f_score(self, target):
        return self.g_score + self.get_distance_from_target(target)
    
    def get_distance_from_target(self, target):
        return (self.get_horizontal_distance(target) + self.get_vertical_distance(target))*1
    
    def get_horizontal_distance(self, node):
        return abs(self.row - node.row)
    
    def get_vertical_distance(self, node):
        return abs(self.col - node.col)
    
    def get_neighbors(self):
        neighbor_north = Node(self.row - 1, self.col, self)
        neighbor_south = Node(self.row + 1, self.col, self)

        neighbor_west = Node(self.row, self.col - 1, self)
        neighbor_east = Node(self.row, self.col + 1, self)

        neighbors = [neighbor_north, neighbor_east, neighbor_south, neighbor_west]
        
        return neighbors
    
    def is_blocked(self, map):
        if self.is_out_of_bounds(map):
            return True
        if self.is_wall(map):
            return True
        return False
    
    def is_out_of_bounds(self, map):
        return self.is_outside_lower_bound() or self.is_outside_upper_bound(map)
    
    def is_outside_lower_bound(self):
        return self.row < 0 or self.col < 0
    
    def is_outside_upper_bound(self, map):
        return self.row + 1 > map.height or self.col + 1 > map.width
    
    def is_wall(self, map):
        return map.matrix[self.row][self.col] == NodeState.WALL.value
    
    def is_in_list(self, list):
        for node in list:
            if self == node:
                return True
        return False
    
    def list_coords(node_list):
        return [node.get_coords() for node in node_list]