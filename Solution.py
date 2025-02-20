#class to represent the plateau for the rovers to traverse
class Matrix:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    #function checks if given coordinates are on the plateau
    def is_valid_position(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height
    
#class to represent the rovers
class Rover:
    def __init__(self, x, y, direction, matrix):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        self.matrix = matrix
        self.instructions = []

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

    def check_positive_integer(value):
        try:
            val = int(value)
            if val > 0:
                return val
            else:
                print("Please enter an integer greater than 0")
                exit()
        except ValueError:
            print("Please enter a positive integer")
            exit()

    def check_at_least_zero(value):
        try:
            val = int(value)
            if val >= 0:
                return val
            else:
                print("Value must be at least 0")
                exit()
        except ValueError:
            print("Please enter a non-negative integer or zero")
            exit()

    def check_direction(value):
        if value.upper() in ['N', 'E', 'S', 'W']:
            return value.upper()
        else:
            print("Please enter a valid direction (N, E, S or W)")
            exit()

    def check_instruction(value):
        if value.upper() in ['L', 'R', 'M']:
            return value.upper()
        else:
            print("Please enter a valid instruction (L, R or M)")

    height = input("Please enter a height for the plateau: ")
    check_positive_integer(height)
    width = input("Please enter a width for the plateau: ")
    check_positive_integer(width)
    matrix = Matrix(height, width)

    rovers = []

    num_rovers = check_at_least_zero(input("How many rovers are there? "))

    if num_rovers == 0:
        print("No rovers to move")
        exit()

    for rover in range(num_rovers):
        x = check_at_least_zero(input("Please enter the x coordinate for the rover: "))
        y = check_at_least_zero(input("Please enter the y coordinate for the rover: "))
        direction = input("Please enter the direction for the rover, one of either N, E, S or W: ").upper()
        check_direction(direction)
        new_rover = Rover(x, y, direction, matrix)
        num_instructions = check_at_least_zero(input("How many instructions are there for the rover? "))
        for _ in range(num_instructions):
            instruction = input(("Please enter the instruction (one of either L, R or M): ").upper())
            check_instruction(instruction)
            new_rover.instructions.append(instruction)
        rovers.append(new_rover)
    
    solution = Solution(matrix, rovers)
    solution.run()
    print(solution.get_final_positions())