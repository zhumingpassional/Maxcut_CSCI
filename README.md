## Run algorithms

Commands:
```
python greedy.py           #Local Search
python random_walk.py
python simulated_annealing.py
```

## Datasets

Take g14.txt (an undirected graph with 800 nodes and 4694 edges) as an example:

800 4694 # #nodes is 800, and #edges is 4694.

1 7 1 # node 1 connects with node 7, weight = 1

1 10 1 # node 1 connects node 10,  weight = 1

1 12 1 # node 1 connects node 12, weight = 1


## Results 

Results will be written to a file xxx.txt in the folder "result". The first column is nodes, and the second column is label. 

1 2  # node 1 in set 2

2 1  # node 2 in set 1

3 2  # node 3 in set 2

4 1  # node 4 in set 1

5 2  # node 5 in set 2


## Performance
In the following experiments, we used GPU during training by default. The best-known results are labed in bold.

The results are stored in the folder "result". Take __Gset__ as an example.

[Gset](https://web.stanford.edu/~yyye/yyye/Gset/) was created by Stanford University. 

| graph | #nodes| #edges | BLS | DSDP    | KHLWG   | RUN-CSP| PI-GNN| Gurobi (0.5 h)  | Gurobi (1 h)  |Gap           | Ours | Improvement | 
|--- |------|----  |---        |-----    |-----    |--------|-------|------           | ---           | ---           | ----| ----|
|G14 | 800  | 4694 | __3064__  |         | 2922    | 3061   | 2943  |3034             |3042           | 3.61\%        | __3064__ | +0\%|
|G15 | 800  | 4661 | __3050__  | 2938    |__3050__ | 2928   | 2990  | 3016            | 3033          |3.33\%         | __3050__ | +0\% | 
|G22 | 2000 | 19990|__13359__  | 12960   |__13359__| 13028  | 13181 |13062            |13129          | 28.94\%       | __13359__ |  +0\% | 
|G49 | 3000 | 6000 | __6000__  | __6000__|__6000__ |__6000__| 5918  |__6000__         |__6000__       |0              | __6000__|  +0\% | 
|G50 | 3000 | 6000 | __5880__  | __5880__|__5880__ |__5880__| 5820  |__5880__         |__5880__       |0              | __5880__|  +0\% | 
|G55 | 5000 | 12468| 10294     | 9960    | 10236   | 10116  | 10138 | 10103           | 10103         | 11.92\%       |__10298__ |  +0.04\% | 
|G70 | 10000| 9999 |9541       | 9456    | 9458    | -      | 9421  | 9489            | 9490          |2.26\%         |__9583__ | +0.44\% | 

L2A's results are represented as strings. How to transfer the strings into binary results? 

Take data/syn/powerlaw_100_ID0.txt as an example, the result is "4SuqhIaQimYjyk_sX" by L2A, which can be transferred to a binary vector by calling the function str_to_bool in EncoderBase64 in evaluator.py. 



