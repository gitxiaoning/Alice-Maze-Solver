import sys

def read_data():

    # Usage of the solver
    if len(sys.argv) != 2:
        print("Usage: python3 Alice.py <inputfilename>")
        sys.exit()

    # Here is how you open a file whose name is given as the first argument
    f = open(sys.argv[1])

    # readline returns the next line from the file reader as a string
    # including the linefeed

    # Read the first line: the size of maze
    maze_size = int(f.readline())

    # Read the second line: the initial position
    initial_position = f.readline().split(',')
    initial_x = int(initial_position[0])
    initial_y = int(initial_position[1])

    # I found the string functions .split() and .strip() helpful when
    # I was converting from my input text file representing a maze to the
    # data structure representing a maze in my code

    # Read the third line: the goal position
    goal_position = f.readline().split(',')
    final_x = int(goal_position[0])
    final_y = int(goal_position[1])

    # Read the rest of file: all arrows' direction and colour saved in maze_grid(A maze_size*maze_size 2d array)
    maze_grid = [[] for i in range(maze_size)]

    j = 0
    while (line := f.readline()) != "":
        line = line.split(',')
        i = 0
        while i < maze_size * 2:
            maze_grid[j].append([line[i], str(int(line[i + 1]))])
            i += 2

        j += 1

    return maze_size, initial_x, initial_y, maze_grid, final_x, final_y


def code2direction(num: str) -> (int, int):
    # Convert direction code into (x,y)
    code_direction = [0, (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    return code_direction[int(num)]


def make_a_move(curr: (int, int), direction: (int, int), step_size: int) -> (int, int):
    # Move to a given direction
    # Returns the moved position
    return curr[0] + direction[0] * step_size, curr[1] + direction[1] * step_size


def alice_depth_first_search(
        previous_x: int,
        previous_y: int,
        maze_size: int,
        curr_x: int,
        curr_y: int,
        maze_grid: list,
        step_size: int,
        step_count: int
) -> None:
    # Walk through all possible ways to find the smallest
    # Use the depth_first_search technique

    # Base case (1): Out of boundary:
    if curr_x >= maze_size or curr_y >= maze_size or curr_x < 0 or curr_y < 0:
        return

    # Base case (2): Landed on the blank block
    if maze_grid[curr_x][curr_y][0] == 'N':
        return

    # Base case (3): Find the goal:
    if maze_grid[curr_x][curr_y][0] == 'G':
        # Change it only if the new step count is smaller than the original one
        # Despite the step_size this time, only save the smaller step_count

        # If the goal is firstly found:
        if len(maze_grid[curr_x][curr_y][3]) == 0:
            (maze_grid[curr_x][curr_y][2])[0] = step_count
            (maze_grid[curr_x][curr_y][3]).append((previous_x, previous_y))
            (maze_grid[curr_x][curr_y][4]).append(step_size)
        # If not
        else:
            # Change only if the new step count is smaller
            print(maze_grid)
            if (maze_grid[curr_x][curr_y][2])[0] > step_count:
                (maze_grid[curr_x][curr_y][2])[0] = step_count
                # And updates the previous node
                (maze_grid[curr_x][curr_y][3])[0] = (previous_x, previous_y)
                (maze_grid[curr_x][curr_y][4])[0] = step_size
        return

    # There are two cases here:
    # a) If this_block is visited, but this time we have the different step_size. Than we visit this block again.
    # b) If this_block is visited, and this time we have the same step_size.
    #       -If this_step_count is smaller than the one stored in the list. Than we DO visit this block again and
    #        replace the old numbers and count.
    #
    #       -If this_step_count is larger than the one stored in the list. Than we DO NOT visit this block again.
    if step_size not in maze_grid[curr_x][curr_y][4]:
        # If step_count only contains "inf" -> replace the infinity with the new step countt
        if (maze_grid[curr_x][curr_y][2])[-1] == float('inf'):
            (maze_grid[curr_x][curr_y][2])[-1] = step_count
        else:
            maze_grid[curr_x][curr_y][2].append(step_count)

        maze_grid[curr_x][curr_y][4].append(step_size)
        maze_grid[curr_x][curr_y][3].append((previous_x, previous_y))
    else:
        # Retrieve the index of step_count(corresponding to step_size)
        step_count_index = (maze_grid[curr_x][curr_y][4]).index(step_size)

        if step_count >= (maze_grid[curr_x][curr_y][2])[step_count_index]:
            # Base case (4)
            return
        else:
            (maze_grid[curr_x][curr_y][2])[step_count_index] = step_count
            (maze_grid[curr_x][curr_y][3])[step_count_index] = (previous_x, previous_y)

    # Base case (5)
    if step_size == 0:
        return

    # Inductive steps
    curr_colour = maze_grid[curr_x][curr_y][0]
    curr_all_directions = maze_grid[curr_x][curr_y][1]
    if curr_colour == 'Y':
        step_size -= 1
    elif curr_colour == 'R':
        step_size += 1

    for code in curr_all_directions:
        direction = code2direction(code)
        new_location = make_a_move((curr_x, curr_y), direction, step_size)
        # print(new_location, step_size)

        alice_depth_first_search(curr_x,
                                 curr_y,
                                 maze_size,
                                 new_location[0],
                                 new_location[1],
                                 maze_grid,
                                 step_size,
                                 step_count + 1)


def find_shortest_path(maze_size, curr_x, curr_y, maze_grid, final_x, final_y):
    alice_depth_first_search(curr_x, curr_y, maze_size, curr_x, curr_y, maze_grid, 1, 0)

    if maze_grid[final_x][final_y][2][0] == float('inf'):
        return None
    else:

        path_list = [(goal_x, goal_y)]
        pre_x = ((maze_grid[final_x][final_y][3])[0])[0]
        pre_y = ((maze_grid[final_x][final_y][3])[0])[1]

        pre_size = (maze_grid[final_x][final_y][4])[0]

        # Assign curr_block to previous block;
        # Where the block comes to the goal
        pre_block = maze_grid[pre_x][pre_y]

        while curr_x != pre_x or curr_y != pre_y:

            path_list.append((pre_x, pre_y))
            # We only add the corresponding step_size steps.
            # We find the corresponding steps

            # Calculate the correct size for curr block
            if pre_block[0] == 'Y':
                pre_size += 1
            elif pre_block[0] == 'R':
                pre_size -= 1

            correspond_index = (pre_block[4]).index(pre_size)

            pre_coordinate = (pre_block[3])[correspond_index]
            pre_x = pre_coordinate[0]
            pre_y = pre_coordinate[1]

            pre_block = maze_grid[pre_x][pre_y]

        path_list.append((curr_x, curr_y))

        path_list.reverse()
        return path_list, maze_grid[final_x][final_y][2]


if __name__ == "__main__":
    # Load data
    data = read_data()

    # Retrieve all data
    size = data[0]
    start_x = data[1]
    start_y = data[2]
    grid = data[3]
    goal_x = data[4]
    goal_y = data[5]

    # Initialize
    for i in range(size):
        for j in range(size):
            grid[i][j].append([float('inf')])
            grid[i][j].append([])
            grid[i][j].append([])

    solution = find_shortest_path(size, start_x, start_y, grid, goal_x, goal_y)

    if solution is None:
        print("No solution")
    else:
        for i in range(len(solution[0])):
            if i != len(solution[0]) -1:
                print(solution[0][i], end="->")
            else:
                print(solution[0][i])

        print(solution[1][0])