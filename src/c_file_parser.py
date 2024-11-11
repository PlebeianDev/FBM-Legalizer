class FParser:
    """
    The file-parser class is made in such way that can support all bookshelf format benchmarks.
    FParser class can be used either in combination with the other classes in order to have a complete
    object-oriented version of a benchmark, or can be used separately as a class or not (you'll need to make minor
    changes to use it as a standalone version)
    """

    def __init__(self, path: str):
        self.path = path  # File path/name WITHOUT extension

    def read_cells(self):
        """
        Reads all the files necessary to init cell class.
        :return: {'cell1_name': [left-x, low-y, width, height, move-type],...}
        Note that non-terminals move-type is None
        """

        cells = {}
        data = []

        with open(self.path + '.pl') as p:
            for num, line in enumerate(p):
                if not(num == 0 or '#' in line or line == '\n'):
                    data = line.split()
                    cells[data[0]] = [float(data[1]), float(data[2])]  # cell_name: [left-x, low-y]
        data.clear()

        with open(self.path + '.nodes') as n:
            for num, line in enumerate(n):
                if num == 0 or '#' in line or line == '\n' or 'NumNodes' in line or 'NumTerminals' in line:
                    continue
                elif 'terminal' in line or 'terminal_NI' in line:
                    data = line.split()
                    cells[data[0]].append(float(data[1]))
                    cells[data[0]].append(float(data[2]))
                    cells[data[0]].append(data[3])  # Move-type
                else:
                    data = line.split()
                    cells[data[0]].append(float(data[1]))
                    cells[data[0]].append(float(data[2]))
                    cells[data[0]].append(None)  # None = Non-terminal
        return cells

    def read_nets(self):
        """
        Reads all the files necessary to init net class.
        :return: {'net_name': [cell1, cell2,...]}
        """

        net_counter = -1
        nets = {}
        nets_index = {}

        with open(self.path + '.nets') as n:
            for num, line in enumerate(n):
                if not(num == 0 or '#' in line or line == '\n' or 'NumNets' in line or 'NumPins' in line):
                    data = line.split()
                    if 'NetDegree' in line:
                        net_counter += 1
                        nets['n' + str(net_counter)] = []
                        nets_index[net_counter] = 'n' + str(net_counter)
                    else:
                        nets['n' + str(net_counter)].append(data[0])
        return nets, nets_index

    def read_rows(self):
        """
        Reads all the necessary files to init row class
        :return: {line_num: [coordinate, height, sitespacing, SubrowOrigin, NumSites], ...}
        """

        rows = {}
        data = []
        row_count = -1

        with open(self.path + '.scl') as s:
            for _, line in enumerate(s):
                if 'CoreRow' in line:
                    row_count += 1
                if 'Coordinate' in line:
                    data = line.split()
                    rows[row_count] = [float(data[2])]  # Coordinate
                if 'Height' in line:
                    data = line.split()
                    rows[row_count].append(float(data[2]))  # Height
                if 'Sitespacing' in line:
                    data = line.split()
                    rows[row_count].append(float(data[2]))  # Sitespacing
                if 'SubrowOrigin' in line:
                    data = line.split()
                    rows[row_count].append(float(data[2]))  # SubrowOrigin
                    rows[row_count].append(float(data[5]))  # NumSites
        return rows
