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
    print(f'Answer,100,{corr},,', file = target) # there could be more alternatives with partial credit
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from boolean import boolean
from sys import argv # debugging

# true/false example: evaluating a boolean expression

def booleval(target, pts = 1, level = 1):
    bop = {'X': '\\oplus', 'A': '\\wedge', 'O': '\\vee', 'I': '\\rightarrow', 'E': '\\leftrightarrow', 'N': '\\neg'}
    cand = bop.keys() -  {'0', '1', 'N'}
    bor = sample(list(cand), 3)
    expr = 'a {:s} b {:s} c {:s} d'.format(bor[0], bor[1], bor[2])
    shuffle(bor)
    precedence = ''.join(bor)
    a = 1 * (random() < 0.5)
    b = 1 * (random() < 0.5)
    c = 1 * (random() < 0.5)
    d = 1 * (random() < 0.5)
    assigned = expr.replace('a', str(a))
    assigned = assigned.replace('b', str(b))
    assigned = assigned.replace('c', str(c))
    assigned = assigned.replace('d', str(d))
    result = boolean(assigned, precedence) 
    prec = [ op for op in precedence ][::-1] # invert
    if 'debug' in argv:
        p = ''.join(prec)
        print(f'{p} for {assigned} gives {result}')
    precedence = ' '.join(prec)
    for op in bop: # prepare as LaTeX
        expr = expr.replace(op, bop[op]) 
        precedence = precedence.replace(op, bop[op])
    val = f'\\(a = {a}, b = {b}, c = {c}, d = {d}\\)'
    title = 'Boolean logic'
    question = f'"What is the value of \\( {expr} \\)'
    question += f' with precedence (from highest to lowest) \\( {precedence} \\)'
    question += f' and the assignment {val}?"'
    hint = '"Assign the truth values into the variables in the expression. Then, starting from the highest-precedence operator, compute its value. Use the value of each operator evaluation as an input in the follow-up evaluations until you each the final result."'
    feedback = '"Stick to the precedence, work iteratively. Remember that should there be any negations (a unary operator), they would have the highest precedence. The only way to alter that would be by placing parenthesis around subexpressions to indicate that they should be evaluated before taking the negation."'
    print('NewQuestion,TF,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    if result == '1': # evaluated to true
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
    k = randint(3, 5)
    while n is None:
        n = ''.join([ digit(randint(0, b - 1)) for x in range(k) ]) 
        if len(n.replace('0', '')) == 0:
            n = None    
    used.add(n)
    sb = '\\( {:s}_{{{:d}}} \\)'.format(n, b)
    v = int(n, b)
    sbc = f'\\( {v}_{{10}} \\)'
    # large base to decimal
    b = randint(11, 22)
    k = randint(2, 4)
    while n is None or n in used:
        n = ''.join([ digit(randint(0, b - 1)) for x in range(k) ]) 
        if len(n.replace('0', '')) == 0:
            n = None
    used.add(n)
    lb = '\\( {:s}_{{{:d}}}\\)'.format(n, b)
    v = int(n, b)
    lbc = f'\\( {v}_{{10}} \\)'
    # binary to octal
    k = randint(3, 6)
    while n in used:
        binary = '1{:s}'.format(''.join([str(randint(0, 1)) for x in range(k)]))
        n = int(binary, 2)
    used.add(n)
    boctal = f'\\( {oct(n)[2:]}_{{8}} \\)'
    sbo = '\\( {:s}_{{2}} \\)'.format(binary)
    # octal to hexadecimal
    while n is None or n in used:
        # three digits
        n = ''.join([str(randint(0, 7)) for i in range(3)]).lstrip('0') 
        if len(n.replace('0', '')) == 0:
            n = None        
    used.add(int(n, 8))
    hos = f'\\( {n}_{{8}} \\)'
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
    pairs = [ ( sb, sbc ),
              ( lb, lbc ),
              ( sbo, boctal ) ,
              (hos, hhs ) ]
    shuffle(pairs)
    l = 1
    for x, y in pairs:
        if random() < 0.5:
            x, y = y, x
        print(f'Choice,{l},{x},,', file = target)
        print(f'Match,{l},{y},,', file = target)
        l += 1
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
    options = list(options)
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
    shuffle(options)
    for o in options:
        if o == corr:
            print(f'Option,100,\\({o}\\),,Nice work.', file = target)
        else:
            # partial credit could also be given by indicating a value > 0 but < 100        
            print(f'Option,0,\\({o}\\),,Just remove all multiples of the divisor while the result remains non-negative.',
              file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from btree import Tree
    
# multiselect sample question: build a binary tree and pick the leaves
def leaves(target, count = 3, level = 2):
    T = Tree()
    low = 2 * count + 2
    high = low + 4
    amount = randint(low, high)
    keys = sample( [ i for i in range(1, 100) ], amount)
    for key in keys:
        T.insert(key)
    T.update()
    leaves = T.leaves()
    internal = set(keys) - leaves
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
    total = 2 * count
    first = None
    second = None
    while True:
        first = randint(1, total - 1)
        second = total - first        
        if first <= len(leaves) and second <= len(internal):
            break
    options = sample(leaves, first) + sample(internal, second)
    shuffle(options)
    for option in options:
        pick = 1 * (option in leaves) # 1 is yes, 0 is no
        fb = f'{option} is a leaf node. ' if pick == 1 else f'{option} is an internal node. '
        print(f'Option,{pick},{option},,{fb}', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

# ordering sample question: sort the vertices by their degree in decreasing order

def vertexdegree(target, count = 4, level = 3):
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
    feedback = '"Drawing the graph can be helpful, but technically one could just go down the edge list and count. Remember to scroll all the way to the right to see all of the edges."'
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
        l = ' '.join([ u for u in A[v] ])
        fb = f'"The neighborhood of {v} consist of {l}. "'
        print(f'Item,\\({v}\\),NOT HTML,{fb},', file = target) # apparently there is an option HTML as well
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)


# regression, for now as a multiple choice question
def noise(width):
    r = random() * width
    if random() < 0.5:
        r *= -1
    return r

from casestudy import select
from math import fabs
url = "https://scs-technology-and-innovation.github.io/casestudy/demo/select.html"
def regression(target, pts = 1, level = 1): 
    n = level * 10 # number of data points
    prec = 1 + level # precision in decimal places
    fs = f'{{:.{prec}f}}' # format string    
    (a, b), s = select(n, prec)
    corr = f'"Slope {a}, intercept {b}"'
    inverted = f'"Slope {b}, intercept {a}"'
    options = { corr, inverted }
    opt = 3 * level * 2
    na = float(a)
    nb = float(b)
    width = (fabs(na) + fabs(nb)) / 2
    while len(options) < opt:
        fas = fs.format(na + noise(width))
        fbs = fs.format(nb + noise(width))
        fake = f'"Slope {fas}, intercept {fbs}"'
        invfake = f'"Slope {fbs}, intercept {fas}"'
        options.add(fake)
        options.add(invfake)
    options = list(options)
    title = 'Linear regression'
    question = f'"Fit a linear model into <a href=\'{url}?s={s}&n={n}\' target=\'_blank\'>casestudy{s}.csv</a>. Select the correct slope-intercept pair."'
    hint = '"Use LinearRegression from scikit-learn. The data file is automatically downloaded whenclicking the link in the question. Check your download folder if you cannot find it."'
    feedback = '"The slope is listed as the first (and only) coefficient of the fitted model."'
    print('NewQuestion,MC,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},HTML,,', file = target) 
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    shuffle(options)
    for o in options:
        if o == corr:
            print(f'Option,100,{o},,Nicely done.', file = target)
        else:
            # partial credit could also be given by indicating a value > 0 but < 100        
            print(f'Option,0,{o},,"Think carefully which value is which. Careful with the rounding, too."',
              file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

    
from algs import mc_problem, mc_algorithm
    
def compprob(target, level = 2, pts = 1):
    (question, options) = mc_problem(level)
    title = 'Computational optimization problems'
    hint = '"Think of the problem definition to identify its objective function and any potential restrictions. Remember that the computational complexity of a problem is not dependent of a specific algorithm but instead characterizes the difficulty inherent in the task."'
    feedback = '"These are not questions that are easy to memorize, but once you understand the problem formulation, it becomes easier to reconstruct the specific details."'
    print('NewQuestion,MC,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    shuffle(options)
    for (to, corr) in options:
        if corr:
            print(f'Option,100,"{to}",,Nice work.', file = target)
        else:
            # partial credit could also be given by indicating a value > 0 but < 100        
            print(f'Option,0,"{to}",,"The CLRS textbook is great study resource for this topic."',
              file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

def compalg(target, level = 2, pts = 1):
    (question, options) = mc_problem(level)
    title = 'Algorithms'
    hint = '"Each algorithm solves a specific problem. The inputs and outputs depend on the characteristics of that problem. For the complexity, pay special attention to any loops or recursive calls in the pseucocode."' 
    feedback = '"These are not questions that are easy to memorize, but once you understand the essence of the algorithm, the pseudocode starts to make sense shortly thereafter."'
    print('NewQuestion,MC,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Pts,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    shuffle(options)
    for (to, corr) in options:
        if corr:
            print(f'Option,100,"{to}",,Nice work.', file = target)
        else:
            # partial credit could also be given by indicating a value > 0 but < 100        
            print(f'Option,0,"{to}",,"The CLRS textbook is great study resource for this topic."',
              file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

kinds = [
    logarithm, # 1
    booleval, # 2 
    integers, # 3
    modulo, # 4
    leaves, # 5
    vertexdegree, # 6
    regression, # 7 (would ideally be a FIB question, but there seems to be no template yet
    compprob, # 8 a multiple-choice question about computational problems
    compalg # 9 a multiple-choice question about algorithms
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
