from problem import *

class NQueen(Problem):

    def __init__(self, n):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        pass

    def tuple_to_list(self, state):
        new_state = []
        for i in range(self.n):
            new_state.append([x for x in state[i][:]])
        return new_state

    def list_to_tuple(self, state):
        new_state = []
        for i in range(self.n):
            new_state.append(tuple([x for x in state[i][:]]))
        return tuple(new_state)


if __name__ == '__main__':
    pass