# Create grid to be transformed.
GRID = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

def print_grid(grid = [] ):
    for i in grid:
            print(i)

#rows = len(grid)
#columns = len(grid[0])
print_grid(GRID)
'''new_grid = []
for i in range(rows):
	new_grid[i] += i
	for j in range(columns):
		new_grid[i][j] += i
		new_grid[j][i] = grid[i][j]
for k in new_grid:
	print(new_grid[k])'''
