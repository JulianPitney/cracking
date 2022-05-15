def incinerate_farmland(coords, mat):

    # unpack coords and burn tile
    x = coords[0]
    y = coords[1]
    mat[x][y] = 0

    # coords for all adjacent tiles with bounds protection.
    # If coords are out of bounds they'll just be reset to the starting
    # tile's coords and not trigger their corresponding if-statement
    # below since the starting tile has already been burned.
    #
    # Note: Assumes input mat is 2D and a rectangle. If it's not this code will fail.
    left = (max(0, x - 1), y)
    right = (min(len(mat) - 1, x + 1), y)
    top = (x, min(len(mat[x]) - 1, y + 1))
    bottom = (x, max(0, y - 1))

    # check if adjacent tiles are farmland. If they are, recursively set them on fire.
    adjacent_coords = [left, right, top, bottom]
    for coord in adjacent_coords:
        if mat[coord[0]][coord[1]]:
            # torch everything as we go.
            mat[coord[0]][coord[1]] = 0
            incinerate_farmland(coord, mat)


def count_fields(farm):

    num_fields = 0

    for x in range(0, len(farm)):
        for y in range(0, len(farm[x])):

            if farm[x][y]:
                num_fields += 1
                incinerate_farmland((x, y), farm)

    return num_fields


unlucky_farm = [[1, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 0, 1]]
print(count_fields(unlucky_farm))
print(unlucky_farm)