from c_benchmark import Benchmark
from c_cell import Cell
from c_row import Row


def fbm_legalize(b: Benchmark):
    """
    Algorithm's final step
    5. Run:
        for i=1 to C do
            if Celli and Celli+1 are overlapping then
                Celli+1 is moved to right
            end if
        end for
        for i=1 to C do
            if Celli is not in a valid position then
                Move the Celli to a valid position to left
                while Celli−1 not be in a valid position do
                    Move the Celli−1 untill to a valid position to left
                end while
            end if
        end for
    """
    # Remove pins from cells
    cells = {key: value for key, value in b.cells.items() if key not in b.pins}

    # 1. Place all cells in the nearest rows according to their positions y
    ypos = []
    for row in b.rows:
        ypos.append(row.corerow)
    for cell in cells.values():
        cell.low_y = min(ypos, key=lambda x: abs(x - cell.low_y))
    del ypos

    # 2. Sort cells according to width and y-position. Priorities in text
    cells = sorted(cells.values(), key=lambda c: (c.width, c.low_y))

    # 3. Check if cells fit in the same row and move them according to text
    for row in b.rows:
        row.find_cells(cells)
        if row == b.rows[-1]:
            # Other rules, push down cells to other avail rows
            break
        total_cell_width = sum(c.width for c in row.cells)
        if total_cell_width > row.right_x:
            # Move cells to row above, if last row, go below. Not shown in paper
            cells_to_move = select_cells_to_move(row.cells, row.right_x, total_cell_width)
            move_cells_up(cells_to_move, row, cells)
            row.cells = [x for x in row.cells if x not in cells_to_move] #Remove cells from list
    # Check last row and move cells to other below that have space
    row = b.rows[-1]
    total_cell_width = sum(c.width for c in row.cells)
    if total_cell_width > row.right_x:
        cells_to_move = select_cells_to_move(row.cells, row.right_x, total_cell_width)
        # Move below to avail rows
        for row2 in b.rows[-2::-1]:
            if not cells_to_move:
                break
            row2_cells_width = sum(c.width for c in row2.cells)
            cells_to_move2 = select_cells_last_row(cells_to_move, row2.right_x, row2_cells_width)
            for c in cells_to_move2:
                c.low_y = row2.corerow
                row2.cells.append(c)
                row.cells.remove(c) # Remove cells from list
                cells_to_move.remove(c)

    # 4. Sort cells according to x and y-positions
    for row in b.rows:
        row.cells = sorted(row.cells, key=lambda c: c.left_x)

    # 5 Algorithm execution
    # Move to the right, may create overflows
    for row in b.rows:
        for i in range(len(row.cells)-1):
            c = row.cells[i]
            cn = row.cells[i+1]
            if check_cells_overlap(c, cn):
                cn.left_x = c.right_x
                cn.right_x = cn.width + cn.left_x
    # Eliminate overflows
    for row in b.rows:
        flag = False
        for i in range(len(row.cells)-1,-1,-1):
            c = row.cells[i]
            if c.right_x > row.right_x:
                # Bring overflowing cell exactly to the right side of the die area
                c.right_x -= c.right_x - row.right_x
                c.left_x = c.right_x - c.width
                flag = True
        if flag:
            # Reverse row ironing instead of the proposed algorithm scheme
            for i in range(len(row.cells) - 1, 0, -1):
                c = row.cells[i]
                cn = row.cells[i-1]
                if check_cells_overlap_reverse(c, cn):
                    cn.right_x = c.left_x
                    cn.left_x = cn.right_x - cn.width

def select_cells_to_move(cells: [Cell], row_width: float, total_cell_width: float):
    target_width = total_cell_width - row_width
    tmp_width  = 0.0
    cells_to_move = []
    # Cells already in ascending order by width
    for cell in cells:
        if tmp_width >= target_width:
            break
        cells_to_move.append(cell)
        tmp_width += cell.width
    return cells_to_move

def move_cells_up(cells: [Cell], row: Row, cells_og: [Cell]):
    newy = row.corerow + row.height
    for cell in cells:
        row.cells[row.cells.index(cell)].low_y = newy
        cells_og[cells_og.index(cell)] = row.cells[row.cells.index(cell)]

def select_cells_last_row(cells: [Cell], row_width: float, curr_total_cell_width: float):
    max_width = row_width - curr_total_cell_width
    move_cells = []
    for cell in cells:
        if max_width - cell.width <= 0:
            break
        move_cells.append(cell)
        max_width -= cell.width
    return move_cells

def check_cells_overlap(c1: Cell, c2: Cell):
    if c2.left_x < c1.right_x:
        return True
    return False

def check_cells_overlap_reverse(c1: Cell, c2: Cell):
    if c2.right_x > c1.left_x:
        return True
    return False
