import copy
import sys
from heapq import heapify, heappush, heappop


class Node():
    def __init__(self, data, move, depth, parent):
        self.data = data
        self.index_zero = self.data.index(0)
        self.heuristic = 999
        self.move = move
        self.depth = depth
        self.parent = parent
        self.moves = []
        self.possible_moves()
        self.heurstic_calc()

    def possible_moves(self):
        if self.index_zero in [0, 1, 3, 4, 6, 7]:
            self.moves.append('RIGHT')
        if self.index_zero in [1, 2, 4, 5, 7, 8]:
            self.moves.append('LEFT')
        if self.index_zero in [3, 4, 5, 6, 7, 8]:
            self.moves.append('UP')
        if self.index_zero in [0, 1, 2, 3, 4, 5]:
            self.moves.append('DOWN')

    def heurstic_calc(self):  #number of misplaced tiles
        count = 0
        for i, j in zip(self.data, final_state):
            if (i != j):
                count += 1
        self.heuristic = count

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def swap(L, pos1, pos2):
    L[pos1], L[pos2] = L[pos2], L[pos1]
    return L


def RIGHT(L):
    temp = copy.copy(L.data)
    index_zero = L.index_zero
    new_data = swap(temp, index_zero, index_zero + 1)
    return Node(new_data, "MOVE RIGHT", L.depth + 1, L.data)


def LEFT(L):
    temp = copy.copy(L.data)
    index_zero = L.index_zero
    new_data = swap(temp, index_zero, index_zero - 1)
    return Node(new_data, "MOVE LEFT", L.depth + 1, L.data)


def UP(L):
    temp = copy.copy(L.data)
    index_zero = L.index_zero
    new_data = swap(temp, index_zero, index_zero - 3)
    return Node(new_data, "MOVE UP", L.depth + 1, L.data)


def DOWN(L):
    temp = copy.copy(L.data)
    index_zero = L.index_zero
    new_data = swap(temp, index_zero, index_zero + 3)
    return Node(new_data, "MOVE DOWN", L.depth + 1, L.data)


def print_results(initial_state, track, explored):
    print("INITIAL STATE")
    print(" ")
    print(initial_state[0], " ", initial_state[1], " ", initial_state[2])
    print(initial_state[3], " ", initial_state[4], " ", initial_state[5])
    print(initial_state[6], " ", initial_state[7], " ", initial_state[8])
    for i in track:
        print(" ")
        print(i.move)
        print(i.data[0], " ", i.data[1], " ", i.data[2])
        print(i.data[3], " ", i.data[4], " ", i.data[5])
        print(i.data[6], " ", i.data[7], " ", i.data[8])
    print("\nTotal Nodes Explored : ", explored, " Total Moves Required",
          len(track))


def backtrack(first, initial_state, visited):
    track = []
    while (first.data != initial_state):
        track.insert(0, first)
        for i in visited:
            if (i.data == track[0].parent):
                first = i
    return track


def run():
    try:
        first = Node(initial_state, "INITIAL STATE", 0, [0])
        visited = []
        frontier = []
        explored = 0
        heapify(frontier)
        while (first.data != final_state):
            first_node = first
            visited.append(first)
            if 'RIGHT' in first_node.moves:
                node = RIGHT(first_node)
                if node.data not in [k.data for k in visited]:
                    heappush(frontier, node)
                    explored += 1
            if 'UP' in first_node.moves:
                node = UP(first_node)
                if node.data not in [k.data for k in visited]:
                    heappush(frontier, node)
                    explored += 1
            if 'DOWN' in first_node.moves:
                node = DOWN(first_node)
                if node.data not in [k.data for k in visited]:
                    heappush(frontier, node)
                    explored += 1
            if 'LEFT' in first_node.moves:
                node = LEFT(first_node)
                if node.data not in [k.data for k in visited]:
                    heappush(frontier, node)
                    explored += 1
            first = heappop(frontier)
        visited.reverse()
        print_results(initial_state, backtrack(first, initial_state, visited),
                    explored)
    except:
        print('got stuck somewhere')
        exit(0)

if __name__ == "__main__":
    initial_state = list(sys.argv[1].split(','))
    initial_state = [int(x) for x in initial_state]
    final_state = list(sys.argv[2].split(','))
    final_state = [int(x) for x in final_state]
    run()
