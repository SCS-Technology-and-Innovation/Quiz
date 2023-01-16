# -*- coding: utf-8 -*-
from random import shuffle, randint, choice, sample, random
from math import log, ceil, floor, sqrt, factorial
from collections import defaultdict
from fractions import Fraction
import cgitb; cgitb.enable()
from datetime import datetime, timedelta, date
from copy import deepcopy
from hashlib import md5
import string

# 0 = Spanish
# 1 = English
# localization options kept in case we add French later
lan = 1 # default 

algs = {'FW': [1, 2, 3, 4],
        'FF': [5, 2, 6, 7],
        'Pr': [8, 9, 10, 11],
        'Kr': [8, 12, 10, 11],
        'DFS': [13, 14, 3, 16],
        'BFS': [17, 14, 3, 17], 
        'of': [18, 19, 20, 21],
        'os': [18, 22, 20, 21],
        'bb': [23, 24, 21, 26],
        'es': [27, 28, 29, 27],
        'er': [27, 30, 29, 27]
}

probs = {'knapsack': [1, 2, 3, 4],
         'editdist': [5, 6, 7, 8],
         'gcd': [5, 9, 28, 14], 
         'mincut': [5, 9, 11, 12],
         'maxflow': [5, 9, 13, 12],
         'matching': [5, 17, 15, 16],
         'mst': [5, 17, 7, 18], 
         'tsp': [19, 20, 7, 21],
         'clique': [19, 22, 23, 24],
         'idset': [19, 22, 23, 25], 
         'vertexcover': [19, 22, 26, 27],
         'edgecover': [5, 17, 26, 29],
         '2color': [5, 30, 10, 31],
         'kcolor': [19, 30, 10, 31]
}


algsIdx = {
    0: ['¿Qué se obtiene con el algoritmo',
        '¿Cuál es la complejidad asintótica de peor caso del algoritmo',
        '¿Qué se le da como entrada al algoritmo',
        '¿Qué produce como salida el algoritmo'],
    1: ['What is the the goal of',
        'What is the worst-case asymptotic complexity of',
        'What is the input for',
        'What is the output of']
}

algsOp = {
    0: {1: 'todas las distancias',
        2: '$\mathcal{O}(n^3)$',
        3: 'un grafo simple (ponderado)',
        4: 'una matriz de distancia',
        5: 'flujo máximo',
        6: 'un grafo ponderado y los vértices fuente y sumidero', 
        7: 'valor total de flujo y el flujo por arista',
        8: 'árbol de expansión mínima',
        9: '$\mathcal{O}(m + n \log n)$',
        10: 'un grafo necesariamente ponderado',
        11: 'el costo total y las aristas incluidas', 
        12: '$\mathcal{O}(m \log n)$',
        13: 'componente conexo de un vértice',
        14: '$\mathcal{O}(n + m)$',
        16: 'un recorrido de los vértices alcanzables', 
        17: 'los vértices alcanzables agrupados por su distancia',
        18: 'ordenar un arreglo',
        19: '$\mathcal{O}(n \log n)$',
        20: 'un arreglo en orden arbitrario', 
        21: 'un arreglo ordenado',
        22: '$\mathcal{O}(n^2)$',
        23: 'si un elemento está en un arreglo',
        24: '$\mathcal{O}(\log n)$', 
        26: 'verdad o falso',
        27: 'el mayor divisor común',
        28: '$\mathcal{O}(a + b)$',
        29: 'dos números enteros',
        30: '$\mathcal{O}(\log(a + b))$'},
    1: {1: 'all the distances',
        2: '$\mathcal{O}(n^3)$',
        3: 'a simple (weighted) graph',
        4: 'a distance matrix',
        5: 'maximum flow',
        6: 'a weighted graph with source and target vertices', 
        7: 'the total flow and the flow per edge',
        8: 'minimum spanning tree',
        9: '$\mathcal{O}(m + n \log n)$',
        10: 'a weighted graph',
        11: 'the total cost and the included edges', 
        12: '$\mathcal{O}(m \log n)$',
        13: 'the connected component of a vertex',
        14: '$\mathcal{O}(n + m)$',
        16: 'a traversal of researchable vertices', 
        17: 'the reachable vertices group by distance',
        18: 'sorting of an array',
        19: '$\mathcal{O}(n \log n)$',
        20: 'an array in abritrary order', 
        21: 'a sorted array',
        22: '$\mathcal{O}(n^2)$',
        23: 'whether an element is included in an array',
        24: '$\mathcal{O}(\log n)$', 
        26: 'true or false',
        27: 'the greatest common divisor',
        28: '$\mathcal{O}(a + b)$',
        29: 'two integers',
        30: '$\mathcal{O}(\log(a + b))$'}
}

algNames = {
    0: {
        'FW': 'Floyd-Warshall',
        'FF': 'Ford-Fulkerson',
        'of': 'ordenamiento por fusión',
        'os': 'ordenamiento por selección',
        'bb': 'búsqueda binaria',
        'es': 'Euclidiano por resta',
        'er': 'Euclidiano por residuo'
    },
    1: {
        'FW': 'Floyd-Warshall algorithm',
        'FF': 'Ford-Fulkerson algorithm',
        'Kr': 'Kruskal\'s algorithm',
        'BFS':'breadth-first search',
        'DFS':'depth-first search',
        'Pr': 'Prim\'s algorithm', 
        'of': 'merge sort algorithm',
        'os': 'selection sort algorithm',
        'bb': 'binary search',
        'es': 'Euclidian algorithm by subtraction',
        'er': 'Euclidian algorithm by residue'
    }
}

probIdx = {
    0: ['¿Cuál es la complejidad computacional del problema de',
        '¿Qué busca determinar el problema de',
        '¿Cuál es la función objetivo del problema de',
        '¿Qué restricciones tiene el problema de'],
    1: ['What is the computational complexity of the',
        'What is the goal of the',
        'What is the objective function of the',
        'What are the restrictions of the']
}

probOp = {
    0: {1: 'pseudopolinomial',
        2: 'cuál combinación de objetos incluir',
        3: 'maximizar valor total',
        4: 'no superar el peso permitido',
        5: 'polinomial',
        6: 'cómo cambiar una cadena a otra',
        7: 'minimizar costo total',
        8: 'no tiene',
        9: 'cuánto vale (cómo número)',
        10: 'no es un problema de optimización',
        11: 'minimizar capacidad total',
        12: 'separar el fuente del sumidero, respetar capacidades',          
        13: 'maximizar flujo total',
        14: 'que ambas divisiones sean exactas',
        15: 'maximizar cobertura',
        16: 'no repetir vértices',
        17: 'cúales aristas incluir',
        18: 'expandir sin crear ciclos',
        19: 'NP-completo',
        20: 'en qué orden visitar',
        21: 'visitar cada vértice exactamente una vez',
        22: 'cuáles vértices incluir',
        23: 'maximizar cardinalidad',
        24: 'que todos los incluidos sean vecinos entre ellos',
        25: 'que ningunos de los incluidos sean vecinos entre ellos',
        26: 'minimizar cardinalidad', 
        27: 'que cada arista sea cubierto por lo menos una vez',
        28: 'que sea el divisor más grande',
        29: 'que cada vértice sea cubierto por lo menos una vez',
        30: 'asignar colores a los vértices',
        31: 'que ningunos vecinos compartan color',
        32: 'desconocido',
        33: 'PSPACE-completo'},
    1: {1: 'pseudopolynomial',
        2: 'the selection of objects to include',
        3: 'maximize total value',
        4: 'not to exceed the weight limit',
        5: 'polynomial',
        6: 'how to transform a string into another',
        7: 'minimize total cost',
        8: 'none',
        9: 'its numeric value',
        10: 'it is not an optimization problem',
        11: 'minimize total capacity',
        12: 'separate the source from the target, respecting the capacities',          
        13: 'maximize total flow',
        14: 'that both divisions be exact',
        15: 'maximize the coverage',
        16: 'not to repeat vertices',
        17: 'which edges to include',
        18: 'expand without introducing cycles',
        19: 'NP-complete',
        20: 'in which order to make the visits',
        21: 'visit each vertex exactly once',
        22: 'which vertices to include',
        23: 'maximize cardinality',
        24: 'that all included vertices be neighbors',
        25: 'that none of the included vertices be neighbors',
        26: 'minimize the cardinality', 
        27: 'that each edge be covered at least once',
        28: 'that the divisor be the largest possible',
        29: 'that each vertex be covered at least once',
        30: 'to assign a color to each vertex',
        31: 'that no pair of neighbors share a color',
        32: 'unknown',
        33: 'PSPACE-complete'}
}
         
probNames = {
    0: {'editdist': 'distancia de edición',
        'gcd': 'mayor divisor común',
        'mincut': 'corte mínimo',
        'maxflow': 'flujo máximo',
        'matching': 'acoplamiento máximo',
        'mst': 'árbol de expansión mínima',
        'tsp': 'problema del viajante',
        'clique': 'camarilla máxima', 
        'idset': 'conjunto independiente máximo',
        'vertexcover': 'cubierta mínima con vértices',
        'edgecover': 'cubierta mínima con aristas',
        '2color': '2-coloreo',
        'kcolor': '$k$-coloreo'},
    1: {'editdist': 'edit distance problem',
        'gcd': 'greatest common divisor problem',
        'mincut': 'minimum cut problem',
        'maxflow': 'maximum flow problem',
        'matching': 'matching problem',
        'mst': 'minimum spanning tree',
        'tsp': 'travelling salesman problem',
        'clique': 'clique problem', 
        'idset': 'independent set problem',
        'vertexcover': 'vertex cover problem',
        'edgecover': 'edge cover problem',
        '2color': '2-coloring problem',
        'kcolor': '$k$-coloring problem'}
}

def mc_problem(level = 1):
    pr = sample(list(probs.keys()), 1)[0]
    pi = randint(0, len(probIdx[lan]) - 1)
    available = { v[pi] for v in probs.values() }
    if pi == 0:
        available |= { 32, 33 }
    count = 2 * level + 1
    options = sample(list(available), count)
    corr = probs[pr][pi]        
    if corr not in options:
        options.remove(sample(options, 1)[0])
        options.append(corr)
    question = '{:s} {:s}?'.format(probIdx[lan][pi],
                                   probNames[lan].get(pr, pr))
    options = [ (probOp[lan][o], o == corr) for o in options ]
    return (question, options)

def mc_algorithm(level = 1):
    al = sample(list(algs.keys()), 1)[0] 
    ai = randint(0, len(algsIdx[lan]) - 1)
    count = 2 * level + 1
    options = sample([ v[ai] for v in algs.values() ], count)
    corr = algs[al][ai]        
    if corr not in options:
        options.remove(sample(list(options), 1)[0])
        options.append(corr)
    shuffle(options)
    question = '{:s} {:s}?'.format(algsIdx[lan][ai],
                                   algNames[lan].get(al, al))
    options = [ (algsOp[lan][o], o == corr) for o in options ]
    return (question, options)

if __name__ == '__main__':
    print(mc_problem())
    print(mc_algorithm())
