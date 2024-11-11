from c_cell import Cell
import sys


class Net:
    """
    Defines a net object according to bookshelf format
    """

    counter = -1

    def __init__(self):
        Net.counter += 1

        self.name = None
        self.cells = []  # list of cells-in-net names
        self.net_degree = 0
        self.area = 0.0
        self.left_x = 0.0
        self.low_y = 0.0
        self.right_x = 0.0
        self.high_y = 0.0
        self.hpwl = 0.0

        self.id = Net.counter

    def calculate_net_area(self):
        return abs((self.high_y - self.low_y) * (self.right_x - self.left_x))

    def make_cells_list(self, cells_from_file: set):
        self.cells = cells_from_file

    def calculate_net_corners(self, cells: dict):
        low_y = sys.float_info.max
        left_x = sys.float_info.max
        high_y = sys.float_info.min
        right_x = sys.float_info.min

        for cell_name in self.cells:
            if cells[cell_name].low_y <= low_y:
                low_y = cells[cell_name].low_y
            if cells[cell_name].left_x <= left_x:
                left_x = cells[cell_name].left_x
            if cells[cell_name].high_y >= high_y:
                high_y = cells[cell_name].high_y
            if cells[cell_name].right_x >= right_x:
                right_x = cells[cell_name].right_x

        self.left_x = left_x
        self.low_y = low_y
        self.high_y = high_y
        self.right_x = right_x

    def calculate_hpwl(self):
        h = self.high_y - self.low_y
        w = self.right_x - self.left_x
        self.hpwl = h + w
    
    def check_if_cell_in_net(self, cell: Cell):
        if cell.name in self.cells:
            return True
        return False

    def generate_net(self, nets_dict: dict, cells_list: list, nets_index: dict):
        """
        Custom net constructor compatible to info given by file-parsing
        :param nets_dict:
        :param cells_list:
        :param nets_index:
        :return:
        """

        self.name = nets_index[self.id]
        tmp = nets_dict[self.name]
        self.make_cells_list(tmp)
