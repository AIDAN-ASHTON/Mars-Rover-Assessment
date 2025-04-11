class Matrix:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    def is_valid_position(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height
    
class Rover:
    def __init__(self, x, y, direction, matrix, rover_id):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        self.matrix = matrix
        self.instructions = []
        self.rover_id = rover_id  # Unique identifier for collision reporting

    def move(self, occupied_positions):
        new_x, new_y = self.x, self.y

        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1

        # Check plateau boundaries
        if not self.matrix.is_valid_position(new_x, new_y):
            raise ValueError(f'Rover {self.rover_id}: Invalid move - out of plateau bounds')
        
        # Check for collisions
        if (new_x, new_y) in occupied_positions:
            other_rover = occupied_positions[(new_x, new_y)]
            raise ValueError(f'Rover {self.rover_id}: Collision detected with Rover {other_rover} at position ({new_x}, {new_y})')
        
        self.x, self.y = new_x, new_y
        
    def rotate(self, direction):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        if direction == 'L':
            new_index = (current_index - 1) % 4
        elif direction == 'R':
            new_index = (current_index + 1) % 4
        self.direction = directions[new_index]

class Solution:
    def __init__(self, matrix, rovers):
        self.matrix = matrix
        self.rovers = rovers

    def run(self):
        # Track occupied positions (position: rover_id)
        occupied_positions = {}
        
        # Initialize occupied positions with starting positions
        for rover in self.rovers:
            pos = (rover.x, rover.y)
            if pos in occupied_positions:
                raise ValueError(f'Initial collision detected between Rover {rover.rover_id} and Rover {occupied_positions[pos]} at {pos}')
            occupied_positions[pos] = rover.rover_id
        
        for rover in self.rovers:
            # Remove rover's current position before moving
            occupied_positions.pop((rover.x, rover.y), None)
            
            for instruction in rover.instructions:
                if instruction == 'L' or instruction == 'R':
                    rover.rotate(instruction)
                elif instruction == 'M':
                    try:
                        rover.move(occupied_positions)
                        # Update occupied positions after successful move
                        occupied_positions[(rover.x, rover.y)] = rover.rover_id
                    except ValueError as e:
                        print(f"Error: {e}")
                        break  # Stop processing further instructions for this rover
                else:
                    raise ValueError('Invalid instruction')

    def get_final_positions(self):
        return [(rover.x, rover.y, rover.direction) for rover in self.rovers]
    
def check_positive_integer(value):
    try:
        val = int(value)
        if val > 0:
            return val
        raise ValueError("Value must be greater than 0")
    except ValueError:
        raise ValueError("Please enter a positive integer")

def check_at_least_zero(value):
    try:
        val = int(value)
        if val >= 0:
            return val
        raise ValueError("Value must be at least 0")
    except ValueError:
        raise ValueError("Please enter a non-negative integer")

def check_direction(value):
    value = value.upper()
    if value in ['N', 'E', 'S', 'W']:
        return value
    raise ValueError("Please enter a valid direction (N, E, S or W)")

def check_instructions(value):
    value = value.upper()
    if all(c in ['L', 'R', 'M'] for c in value):
        return list(value)
    raise ValueError("Instructions can only contain L, R, or M")

def get_input(prompt, validation_func, allow_empty=False):
    while True:
        try:
            value = input(prompt).strip()
            if allow_empty and not value:
                return None
            return validation_func(value)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    try:
        # Get plateau dimensions
        height = get_input("Please enter a height for the plateau: ", check_positive_integer)
        width = get_input("Please enter a width for the plateau: ", check_positive_integer)
        matrix = Matrix(height, width)

        rovers = []
        num_rovers = get_input("How many rovers are there? ", check_at_least_zero)

        if num_rovers == 0:
            print("No rovers to move")
            exit()

        for rover_id in range(1, num_rovers + 1):
            print(f"\nRover {rover_id}:")
            x = get_input("Please enter the x coordinate for the rover: ", check_at_least_zero)
            y = get_input("Please enter the y coordinate for the rover: ", check_at_least_zero)
            direction = get_input("Please enter the direction for the rover (N, E, S, W): ", check_direction)
            
            # Get all instructions at once
            instructions = get_input("Please enter the instructions as a continuous string (e.g., 'LMLMLMLMM'): ", check_instructions)
            
            rover = Rover(x, y, direction, matrix, rover_id)
            rover.instructions = instructions
            rovers.append(rover)
        
        solution = Solution(matrix, rovers)
        solution.run()
        print("\nFinal positions of the rovers:")
        for i, pos in enumerate(solution.get_final_positions(), 1):
            print(f"Rover {i}: {pos}")
            
