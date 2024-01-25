def count_neighbours(grid, row, column):
    """counts the alive number of neighbours for a cell"""
    neighbours = 0
    for i in range(-1,2):#check rows above, same and below.
        for j in range(-1,2):#check columns right, same and left.
            if (i == 0 and j == 0) or not (0 <= row + i < len(grid)) or not (0<= column + j < len(grid[0])):
                continue
            neighbours += grid[row + i][column + j]

    return neighbours

def update_grid(grid):
    grid_c = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and count_neighbours(grid, i, j) < 2:
                grid_c[i][j] = 0
            elif grid[i][j] == 1 and (count_neighbours(grid, i, j) == 2 or count_neighbours(grid, i, j) == 3):
                grid_c[i][j] = 1
            elif grid[i][j] == 1 and count_neighbours(grid, i, j) > 3:
                grid_c[i][j] = 0
            elif grid[i][j] == 0 and count_neighbours(grid, i, j) == 3:
                grid_c[i][j] = 1

    return grid_c

def print_grid(grid):
    for row in grid:
        row_string = ""
        for cell in row:
            if cell == 1:
                row_string += "+"
            else:
                row_string += "."    
        
        print(row_string)


def game_of_life(initial_grid, iterations):
    grid = initial_grid
    for n in range(iterations):
        print_grid(grid)
        print("\n\n Next Generation \n\n")
        grid = update_grid(grid)

#Testing the code
def main():
    initial_grid = [[0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,1,0,0,0]]

    game_of_life(initial_grid, 5)

if __name__ == "__main__":
    main()