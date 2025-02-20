#class to represent the plateau for the rovers to traverse
class Matrix:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    #function checks if given coordinates are on the plateau
    def is_valid_position(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height
    
#class to represent the rovers
class Rover:
    def __init__(self, x, y, direction, matrix):
        self.x = x
        self.y = y
        self.direction = direction
        self.matrix = matrix

    #function to move the rover
    def move(self):
        new_x = self.x
        new_y = self.y

        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1

        #check if the new position is valid
        if self.matrix.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            raise ValueError('Invalid move')
        
    #function to rotate the rover
    def rotate(self, direction):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        if direction == 'L':
            new_index = (current_index - 1) % 4
        elif direction == 'R':
            new_index = (current_index + 1) % 4
        self.direction = directions[new_index]

#class to provide the solution
class Solution:
    def __init__(self, matrix, rovers):
        self.matrix = matrix
        self.rovers = rovers

    def run(self):
        for rover in self.rovers:
            for instruction in rover.instructions:
                if instruction == 'L' or instruction == 'R':
                    rover.rotate(instruction)
                elif instruction == 'M':
                    rover.move()
                else:
                    raise ValueError('Invalid instruction')

    def get_final_positions(self):
        return [(rover.x, rover.y, rover.direction) for rover in self.rovers]
    
if __name__ == "__main__":
    matrix = Matrix(5, 5)

    rovers = [Rover(1, 2, 'N', matrix), Rover(3, 3, 'E', matrix)]
    
    rovers[0].instructions = ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']
    rovers[1].instructions = ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M']
    solution = Solution(matrix, rovers)
    solution.run()
    print(solution.get_final_positions())