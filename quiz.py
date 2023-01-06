# /content/<course path>/images is where any potential images should come from 
# save output as CSV UTF-8 encoded

def sep(target):
    print(',,,,\n,,,,', file = target)

counter = 1

prefix = 'ElisaDemo'

def qid():
    global counter
    counter += 1
    return f'{prefix}_{counter}'

from random import shuffle, randint, choice, sample, random
from math import log, ceil, floor, sqrt, factorial
from collections import defaultdict
from fractions import Fraction
import string
import sys

from btree import Tree, Node

# short answer question example: logarithms of arbitrary bases and rounding
def logarithm(target, pts = 1, level = 1, rows = 1, cols = 3):
    title = 'Logarithm'
    n = randint(100, 999)
    b = randint(2, 8)
    o = choice(['ceil', 'floor'])    
    corr = log(n, b)
    if o == 'ceil':
        corr = ceil(corr)
    else:
        corr = floor(corr)
    question = 'What is the integer value of \\( \\l{:s} \log_{:d} {:d}\\r{:s} \\)?'.format(o, b, n, o)
    hint = '"Think of which power of the base is the closest to the number. Remember to use the correct rounding rule to deal with any potential decimal places. Type only the digits of your answer as your response with no additional information."'
    feedback = '"Being able to estimate logarithms in arbitrary bases, especially without recurring to a calculator, is an important skill for a programmer."'
    print('NewQuestion,SA,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    print(f'InputBox,{rows},{cols},,', file = target)
    print(f'Answer,{pts},{corr},,', file = target) # there could be more alternatives with partial credit
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from boolean import boolean
        
# true/false example: evaluating a boolean expression
def booleval(target, pts = 1, level = 1):
    bop = {'X': '\\oplus', 'A': '\\wedge', 'O': '\\vee', 'I': '\\rightarrow', 'E': '\\leftrightarrow', 'N': '\\neg'}
    cand = bop.keys() -  {'0', '1', 'N'}
    bor = sample(list(cand), 3)
    expr = 'a {:s} b {:s} c {:s} d'.format(bor[0], bor[1], bor[2])
    shuffle(bor)
    sp = ' '.join(bor) 
    q = expr
    lp = sp[::-1] # reverse
    prec = lp
    for op in bop: # prepare as LaTeX
        q = q.replace(op, bop[op]) 
        lp = lp.replace(op, bop[op])
    a = 1 * (random() < 0.5)
    b = 1 * (random() < 0.5)
    c = 1 * (random() < 0.5)
    d = 1 * (random() < 0.5)
    val = f'\\(a = {a}, b = {b}, c = {c}, d = {d}\\)'
    title = 'Boolean logic'
    question = f'"What is the value of \\( {q} \\)'
    question += f' with precedence (from highest to lowest) \\( {lp} \\)'
    question += f' and the assignment {val}?"'
    hint = '"Assign the truth values into the variables in the expression. Then, starting from the highest-precedence operator, compute its value. Use the value of each operator evaluation as an input in the follow-up evaluations until you each the final result."'
    feedback = '"Remember that should there be any negations (a unary operator), they would have the highest precedence. The only way to alter that would be by placing parenthesis around subexpressions to indicate that they should be evaluatedbefore taking the negation."'
    expr = expr.replace('a', str(a))
    expr = expr.replace('b', str(b))
    expr = expr.replace('c', str(c))
    expr = expr.replace('d', str(d))
    result = boolean(expr, prec)    
    print('NewQuestion,TF,,,', file = target)
    print(f'ID,{qid},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    if result: # evaluated to true
        print('TRUE,100,Your result is correct,,', file = target)
        print('FALSE,0,Your result is incorrect,,', file = target)
    else:
        print('TRUE,0,Your result is incorrect,,', file = target)
        print('FALSE,100,Your result is correct,,', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from dm import digit

# matching sample question: integer bases
def integers(target):
    used = set()
    # small base to decimal
    b = randint(2, 9)
    n = None
    while n is None:
        n = ''.join([ digit(randint(0, b - 1)) for x in range(3) ]) # four digits
        if len(n.replace('0', '')) == 0:
            n = None    
    used.add(n)
    sb = '\\( {:s}_{:d} \\)'.format(n, b)
    v = int(n, b)
    sbc = f'\\( {v} \\)'
    # large base to decimal
    b = randint(11, 22)    
    while n is None or n in used:
        n = ''.join([ digit(randint(0, b - 1)) for x in range(2) ]) # three digits
        if len(n.replace('0', '')) == 0:
            n = None
    used.add(n)
    lb = '\\( {:s}_{{{:d}}}\\)'.format(n, b)
    v = int(n, b)
    lbc = f'\\( {v} \\)'
    # binary to octal
    while n in used:
        binary = '1{:s}'.format(''.join([str(randint(0, 1)) for x in range(5)]))
        n = int(binary, 2)
    used.add(n)
    boctal = f'\\( {oct(n)[2:]}_{{8}} \\)'
    sbo = '\\( {:s}_2 \\)'.format(binary)
    # octal to hexadecimal
    while n is None or n in used:
        n = ''.join([str(randint(0, 7)) for i in range(3)]).lstrip('0') # three digits
        if len(n.replace('0', '')) == 0:
            n = None        
    used.add(n)
    hos = f'\\( {n}_8 \\)'
    v = hex(int(n, 8))[2:]
    hhs = f'\\( {v}_{{16}} \\)'
    print('NewQuestion,M,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    title = 'Integer bases'
    question = 'Match integer representations that correspond to the same numerical value.'
    hint = 'One way to work this out would be converting all the values into the same base. Two and ten are often convenient options.'
    feedback = 'Try to avoid memorizing conversion tricks. It is more fruitful to develop a conceptual understanding of the meaning of digits and their positions within a number.'
    pts = 4 # four pairs for now
    level = 2
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused    
    print('Scoring,EquallyWeighted,,,', file = target) # unsure what the other options would be
    print(f'Choice,1,{sb},,', file = target)
    print(f'Choice,2,{lb},,', file = target)
    print(f'Choice,3,{sbo},,', file = target)
    print(f'Choice,4,{hos},,', file = target)
    print(f'Match,1,{sbc},,', file = target)
    print(f'Match,2,{lbc},,', file = target)
    print(f'Match,3,{boctal},,', file = target)
    print(f'Match,4,{hhs},,', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

# multiple choice example question: modulo
def modulo(target, pts = 1, level = 1): 
    a = randint(20, 50)
    b = randint(7, 15)
    corr = a % b
    options = { corr } 
    while len(options) < 5:
        options.add(randint(0, b))
    options.remove(corr)
    options = list(options)
    shuffle(options)
    title = 'Modulo'
    question = f'What is the value of \\( {a} \pmod {{{b}}} \\)?'
    hint = '"Recall that the modulo operator refers to the residue of an integer division. In programming, the percent sign is often used to signify this operation."'
    feedback = '"Much of cryptography is based on modular arithmetic, but it is also handy for programmers in general."'
    print('NewQuestion,MC,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused       
    print(f'Option,100,\\({corr}\\),,Nice work', file = target)
    for other in options:
        # partial credit could also be given by indicating a value > 0 but < 100        
        print(f'Option,0,\\({other}\\),,Just remove all multiples of the divisor while the result remains non-negative.',
              file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from btree import Tree
    
# multiselect sample question: build a binary tree and pick the leaves
def leaves(target, count = 3, level = 2):
    T = None
    leaves = None
    internal = None
    while True:
        T = Tree()
        keys = sample([i for i in range(1, 100)], randint(12, 18))
        for key in keys:
            T.insert(key)
        T.update()
        leaves = T.leaves()
        internal = set(keys) - leaves
        if min(len(leaves), len(internal)) >= count:
            break
    leaves = list(leaves)
    internal = list(internal)
    title = 'Binary trees'
    question = '"Build a binary tree by inserting the key sequence [ ' + \
        ', '.join([ str(k) for k in keys ]) + \
        ' ] and identify which of the following keys are leaves after all keys have been inserted."'
    hint = '"The first key becomes the root. Then, recursively, smaller values go into the left branch and larger values into the right. Any node that has neither a left nor a right branch underneath it is a leaf."'
    feedback = '"When you are systematic and disciplined about always starting at the root and following the rules, this is an easy task."'
    pts = count * 2    
    print('NewQuestion,MS,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused           
    print('Scoring,RightAnswers,,,', file = target) # unsure what the other options are like
    options = sample(leaves, count) + sample(internal, count)
    shuffle(options)
    for option in options:
        pick = 1 * (option in leaves) # 1 is yes, 0 is no
        fb = 'This is a leaf node' if pick == 1 else 'This is an internal node'
        print(f'Option,{pick},{option},,{fb}', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

# ordering sample question: sort the vertices by their degree in decreasing order

def vertexdegree(target, count = 3, level = 3):
    V = None
    E = None
    deg = None
    A = None
    distinct = None
    while True:
        n = randint(7, 10)
        V = [string.ascii_lowercase[i] for i in range(0, n)]
        m = n + randint(3, 6)
        E = set()
        A = defaultdict(set)
        while len(E) < m:
            e = sample(V, 2)
            u = min(e)
            v = max(e)
            A[u].add(v)
            A[v].add(u)
            E.add((u, v))
        deg = { v: len(A[v]) for v in V }
        distinct = set(deg.values())
        if len(distinct) >= count:
            break # enough distinct degrees
    distinct = list(distinct)
    distinct = sample(distinct, count) # cut down
    distinct = sorted(distinct)[::-1] # sort decr
    chosen = []
    for d in distinct:
        for v in V:
            if v in chosen:
                continue
            if deg[v] == d:
                chosen.append(v)
                break
    assert len(chosen) == count
    title = 'Vertex degrees'
    question = '"In the graph \\(G = (V, E)\\) where $$V = \\{' + \
        ', '.join([v for v in sorted(list(V))]) + '\\}$$ and $$E = \\{' + \
        ', '.join(['({:s}, {:s})'.format(u, v) for (u, v) in E ]) + \
        ' \\},$$ sort the following vertices in the descending order of their degree."'
    hint = 'The degree of a vertex is the number of neighbors it has.'
    feedback = '"Drawing the graph can be helpful, but technically one could just go down the edge list and count."'
    print('NewQuestion,O,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    pts = count 
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Scoring,RightMinusWrong,,,', file = target) # unsure what the other options are like    
    print('Image,,,,', file = target) # unused           
    for v in chosen:
        l = ', '.join([ u for u in A[v] ])
        nl = '\\(\\{' + l + '\\}\\)'
        fb = f'"The neighborhood of \\({v}\\) is {nl}."'
        print(f'Item,\\({v}\\),NOT HTML,{fb},', file = target) # apparently there is an option HTML as well
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)


kinds = [
    logarithm, # 1
    booleval, # 2 
    integers, # 3
    modulo, # 4
    leaves, # 5
    vertexdegree # 6
]
    
def generate(count):
    category = 1
    for generator in kinds:
        with open(f'question{category}.csv', 'w', encoding='utf-8') as target:
            for i in range(count):
                generator(target)
                sep(target)
        category += 1

if __name__ == '__main__':
    generate(10) # just a demo (you can do hundreds if you'd like)
