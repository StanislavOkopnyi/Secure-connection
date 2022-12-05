import os.path
from functions import progon
try:
    os.remove("OUTPUT.txt")
except FileNotFoundError:
    pass

with open("INPUT.txt", "r") as file:
    _input_ = file.read()

_input_ = _input_.split("\n")

num_of_cities, num_of_pairs = _input_[0].split()
data_centers_list = _input_[1].split()
connections = [i.split() for i in _input_[2:]]

progon(num_of_pairs, data_centers_list, connections)
