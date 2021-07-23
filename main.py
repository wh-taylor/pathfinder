from map import Map
from node import Node
from plotmap import PlotMap

map = Map([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 1],
])

map2 = Map([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [2, 0, 1, 0, 1],
])

map3 = Map([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,2,0,0,0,1,0,0,0,1,3,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
])

path = map3.get_path()
print(f'Node: {path.node}')
print(f'Open: {Node.list_coords(path.open)}')
print(f'Closed: {Node.list_coords(path.closed)}')
print(f'Checks: {path.checks}')
print(f'List: {Node.list_coords(path.list)}')

pltmap = PlotMap(map3)
pltmap.plot()