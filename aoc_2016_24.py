from functools import partial
from itertools import pairwise, permutations

import mrm.ansi_term as ansi
from mrm.point import adj_ortho, grid_as_dict
from mrm.dijkstra import dijkstra, Dictlike

with open('data/aoc-2016-24.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def preprocess():
    nodes = grid_as_dict(dat, valid=lambda c: c in '.0123456789')
    pts = [k for k, v in sorted(nodes.items(), key = lambda x: x[1]) if v != '.']

    sp_w = {}
    sp_p = {}
    for i, p in enumerate(pts):
        w, p = dijkstra(Dictlike(partial(adj_ortho, constrain_pos=nodes)), start_point=p)
        for j, q in enumerate(pts):
            sp_w[(i, j)] = w[q]
            sp_p[(i, j)] = p[q]

    return pts, sp_w, sp_p, nodes

def viz(grid, nodes, paths, min_path):
    path_pts = []
    for a, b in pairwise(min_path):
        path_pts += paths[(a, b)]
    for y in range(len(dat)):
        for x in range(len(dat[0])):
            pt = (x, y)
            if pt in nodes:
                print(ansi.red(str(nodes.index(pt))), end='')
            elif pt in path_pts:
                print(ansi.green('*'), end='')
            elif pt in grid:
                print(' ', end='')
            else:
                print(ansi.cyan('#'), end='')
        print()

def part1(output = True):
    nodes, weights, paths, grid = preprocess()
    n_pts = len(nodes)

    min_dist = sum(weights.values())
    min_path = None
    for arr in permutations(range(1, n_pts), n_pts - 1):
        tot = 0
        for a, b in pairwise([0] + list(arr)):
            tot += weights[(a, b)]
        if tot < min_dist:
            min_dist = tot
            min_path = arr

    if output:
        ansi.clear_screen()
        lmp = [0] + list(min_path)
        print('Optimal path:', lmp)
        viz(grid, nodes, paths, lmp)

    return min_dist

def part2(output = True):
    nodes, weights, paths, grid = preprocess()
    n_pts = len(nodes)

    min_dist = sum(weights.values())
    min_path = None
    for arr in permutations(range(1, n_pts), n_pts - 1):
        tot = 0
        for a, b in pairwise([0] + list(arr) + [0]):
            tot += weights[(a, b)]
        if tot < min_dist:
            min_dist = tot
            min_path = arr

    if output:
        ansi.clear_screen()
        lmp = [0] + list(min_path) + [0]
        print('Optimal path:', lmp)
        viz(grid, nodes, paths, lmp)

    return min_dist

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
