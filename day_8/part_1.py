class Forest:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.ROW_LENGTH = len(grid)
        self.COLUMN_LENGTH = len(grid[0])
    
    def visible(self, row, column) -> bool:
        # If they're at the edge of the forest.
        if (
            row == 0 or
            row == self.ROW_LENGTH - 1 or
            column == 0 or
            column == self.COLUMN_LENGTH - 1
        ):
            return True

        else:
            value = self.grid[row][column]

            def shorter(x: int) -> bool:
                return value > x

            visible_left = True
            visible_right = True
            visible_top = True
            visible_bottom = True

            # Left.
            for column_check in range(column):
                if not shorter(self.grid[row][column_check]):
                    visible_left = False
                    break

            # Right.
            for column_check in range(column + 1, self.COLUMN_LENGTH):
                if not shorter(self.grid[row][column_check]):
                    visible_right = False
                    break
            
            # Top.
            for row_to_check in range(row):
                if not shorter(self.grid[row_to_check][column]):
                    visible_top = False
                    break

            # Bottom.
            for row_to_check in range(row + 1, self.ROW_LENGTH):
                if not shorter(self.grid[row_to_check][column]):
                    visible_bottom = False
                    break

            return visible_left or visible_right or visible_top or visible_bottom

grid = []

try:
    while True:
        line = input()

        if line:
            line = list(line)
            grid.append(line)

except KeyboardInterrupt:
    forest = Forest(grid)

    count = 0
    for row in range(forest.ROW_LENGTH):
        for column in range(forest.COLUMN_LENGTH):
            if forest.visible(row, column):
                count += 1
    
    print(count)
