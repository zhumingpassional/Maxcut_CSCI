

import copy
import time
from typing import List, Union
import numpy as np
import networkx as nx
from util import read_nxgraph
from util import obj_maxcut
from util import transfer_nxgraph_to_weightmatrix

# init_solution is useless
def greedy_maxcut(init_solution, num_steps: int, graph: nx.Graph) -> (int, Union[List[int], np.array], List[int]):
    print('greedy')
    start_time = time.time()
    num_nodes = int(graph.number_of_nodes())
    nodes = list(range(num_nodes))
    assert sum(init_solution) == 0
    if num_steps is None:
        num_steps = num_nodes
    curr_solution = copy.deepcopy(init_solution)
    curr_score: int = obj_maxcut(curr_solution, graph)
    init_score = curr_score
    scores = []
    for iteration in range(num_nodes):
        if iteration >= num_steps:
            break
        score = obj_maxcut(curr_solution, graph)
        print(f"iteration: {iteration}, score: {score}")
        traversal_scores = []
        traversal_solutions = []
        # calc the new solution when moving to a new node. Then store the scores and solutions.
        for node in nodes:
            new_solution = copy.deepcopy(curr_solution)
            # search a new solution and calc obj
            new_solution[node] = (new_solution[node] + 1) % 2
            new_score = obj_maxcut(new_solution, graph)
            traversal_scores.append(new_score)
            traversal_solutions.append(new_solution)
        best_score = max(traversal_scores)
        index = traversal_scores.index(best_score)
        best_solution = traversal_solutions[index]
        if best_score > curr_score:
            scores.append(best_score)
            curr_score = best_score
            curr_solution = best_solution
        else:
            break
    print("score, init_score of greedy", curr_score, init_score)
    print("scores: ", traversal_scores)
    print("solution: ", curr_solution)
    running_duration = time.time() - start_time
    print('running_duration: ', running_duration)
    return curr_score, curr_solution, scores

if __name__ == '__main__':
    # read data
    graph = read_nxgraph('./data/syn/syn_50_176.txt')
    weightmatrix = transfer_nxgraph_to_weightmatrix(graph)
    # run alg
    num_steps = 30
    alg_name = 'GR'

    # init_solution = None
    init_solution = [0] * graph.number_of_nodes()
    gr_score, gr_solution, gr_scores = greedy_maxcut(init_solution, num_steps, graph)










