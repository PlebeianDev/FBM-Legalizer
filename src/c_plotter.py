from matplotlib import pyplot as plt
from matplotlib import patches
from c_benchmark import *


class Plotter:
    """
    Contains methods for a variety of plots in order to visualize results, parts of a design etc.
    NOTE! This class will be updated and extended depending on the needs and implementations of my research
    """
    def __init__(self):
        pass

    @staticmethod
    def plot_design(benchmark: Benchmark):
        """
        Plots full intance of a design
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal', adjustable='datalim')
        for p in benchmark.pins.values():
            ax.add_patch(patches.Rectangle((float(p.left_x), float(p.low_y)), 1.0, 1.0, fill=True))
            ax.plot()

        for cell in benchmark.cells.values():
            ax.add_patch(patches.Rectangle((float(cell.left_x), float(cell.low_y)), cell.width, cell.height, fill=True,color='black'))
            ax.plot()

        for row in benchmark.rows:
            ax.add_patch(patches.Rectangle((float(row.subroworigin), float(row.corerow)), row.right_x - row.subroworigin, row.height, fill=None, color="black"))
            ax.plot()
        ax.add_patch(patches.Rectangle((benchmark.left_x, benchmark.low_y), benchmark.width, benchmark.height, fill=False))
        ax.plot()
        plt.show()
        