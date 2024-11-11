from c_benchmark import *
from fbm import *

path = "" # "file_path/benchmark_name ... NO EXTENSION"
m = Benchmark(path)
m.generate_benchmark()
# generate_benchmark function generates all the objects needed to describe a benchmark
# Cells, Nets, Rows, and metrics are all calculated in this method.
# Using a debugger you can see an analytical view of all objects and metrics inside m (Benchmark) instance

# Call the legalizer via the fbm python file
fbm_legalize(m)
