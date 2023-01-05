# /content/<course path>/images is where any potential images should come from 
# save output as CSV UTF-8 encoded

def sep(target):
    print(',,,,\n,,,,', file = target)

counter = 1
    
def qid(prefix = ''):
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

        b = choice([i for i in range(3, 8)] + [9])
        n = ''.join([str(randint(0, b - 1)) for x in range(4)])
        corr = int(n, b)
        options = { corr }
        while len(options) < 5:
            options.add(randint(0, 2 * corr + 10))
        options = list(options)       

        # 9 gcd
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuánto vale $\\text{{gcd}}({:d}, {:d})?$'.format(x, y), options, (x, y)))
        else:
            questions.append(('What is the value of $\\text{{gcd}}({:d}, {:d})?$'.format(x, y), options, (x, y)))


            

        iop = ['|', '&', '^']
        shuffle(iop)
        dire = ['<<', '>>']
        shuffle(dire)
        a = randint(20, 40)
        b = randint(10, 19)
        c = randint(1, 3)
        d = randint(30, 50)
        e = randint(20, 40)
        f = randint(1, 3)
        bc = b << c if dire[0] == '<<' else b >> c
        ef = e << f if dire[1] == '<<' else e >> f
        left = a & bc if '&' in iop[0] else a | bc if '|' in iop[0] else a ^ bc
        right = d & ef if '&' in iop[2] else d | ef if '|' in iop[2] else d ^ ef
        corr = left & right if '&' in iop[1] else left | right if '|' in iop[1] else left ^ right
        options = set()
        while len(options) < 4:
            cand = randint(0, 2 * (corr + 10))
            if cand != corr:
                options.add(cand)
        options.add(corr)
        options = list(options)
        expr = '({:d} {:s} ({:d} {:s} {:d})) {:s} ({:d} {:s} ({:d} {:s} {:d}))'.format(a, iop[0], b, dire[0], c, iop[1], d, iop[2], e, dire[1], f)
        # 12 binary arithmetic
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuánto vale {:s}?'.format(expr), options, (a, b, c, d, e, f, dire, iop)))
        else:
            questions.append(('What is the value of {:s}?'.format(expr), options, (a, b, c, d, e, f, dire, iop)))
        A = {randint(1, 99) for p in range(6, 15)}
        A = list(A)
        sA = '\\{{ {:s} \}}'.format(', '.join([str(a) for a in A]))
        options = { len(A), min(A), max(A), choice(A), randint(1, len(A) - 1)}
        while len(options) < 5:
            options.add(randint(0, 10))
        options = list(options)
        # 13 cardinality                       
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuál es la cardinalidad de $A = {:s}$?'.format(sA), options, A))
        else:
            questions.append(('What is the cardinality of $A = {:s}$?'.format(sA), options, A))
        pstart = randint(1, 7)
        plen = 12
        abre = ['(', '[']
        cierre = [')', ']']
        shuffle(abre)
        shuffle(cierre)
        hasta = pstart + plen
        desde = pstart
        if abre[0] == '(':
            desde += 1
        if cierre[0] == ')':
            hasta -= 1
        incluidos = []
        for x in range(desde, hasta + 1):
            if primo(x):
                incluidos.append(x)
        options = set()
        while len(options) < 4:
            cand = randint(0, 3 * hasta)
            if cand not in incluidos: # not a correct option
                options.add(cand)
        options.add(choice(incluidos))
        options = list(options)
        incl = '$\\{{ x \\mid x \\text{{ es primo }} \wedge x \\in {:s}{:d}, {:d} {:s}\\}}$'.format(abre[0], pstart, pstart + plen, cierre[0])
        # 14 prime numbers
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuál de los siguientes números pertenece a {:s}?'.format(incl), options, (abre[0], pstart, pstart + plen, cierre[0])))
        else:
            questions.append(('Which of the following numbers belongs to {:s}?'.format(incl), options, (abre[0], pstart, pstart + plen, cierre[0])))
        fstart = randint(0, 5)
        flen = randint(3, 5)
        extras = randint(2, 4)
        hasta = fstart + flen
        desde = fstart
        if abre[1] == '(':
            desde += 1
        if cierre[1] == ')':
            hasta -= 1
        f = fibo(hasta + extras)
        incluidos = f[desde:(hasta + 1)]
        options = set()
        while len(options) < 4:
            cand = randint(0, 2 * hasta)
            if cand not in incluidos:
                options.add(cand)
        options.add(choice(incluidos))
        options = list(options)
        incl = '$\\{{ F_i \\mid i \\in {:s}{:d}, {:d}{:s}\\}}$'.format(abre[1], fstart, fstart + flen, cierre[1])
        # 15 Fibonacci numbers
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuál de los siguientes números pertenece a {:s}'.format(incl), options, (abre[1], fstart, fstart + flen, cierre[1])))
        else:
            questions.append(('Which of the following numbers belongs to {:s}'.format(incl), options, (abre[1], fstart, fstart + flen, cierre[1])))
        A = set([string.ascii_lowercase[randint(2, 18)] for p in range(3, 6)])
        sA = '\\{{ {:s} \}}'.format(', '.join(A))
        B = set([string.ascii_lowercase[randint(0, 20)] for p in range(5, 9)])
        sB = '\\{{ {:s} \}}'.format(', '.join(B))
        op = randint(0, 3)
        if op == 0:
            C = A | B
        elif op == 1:
            C = A & B
        elif op == 2:
            C = A - B
        elif op == 3:
            C = B - A
        if random() < 0.2 and len(C) > 1:
            C.remove(sample(C, 1)[0])
        elif random() < 0.2:
            C.add(string.ascii_lowercase[randint(2, 18)])
        sC = '\\{{ {:s} \}}'.format(', '.join(C))
        sA.replace('\\{  \\}', '\\emptyset')
        sB.replace('\\{  \\}', '\\emptyset')
        sC.replace('\\{  \\}', '\\emptyset')
        options = ['$C = A \cup B$', '$C = A \cap B$', '$C = A \setminus B$', '$C = B \setminus A$']
        if lan == 0:
            options.append('ninguna')
        else:
            options.append('none')
        # 16 set operations
        shuffle(options)
        if lan == 0:
            questions.append(('Teniendo $A = {:s}$, $B = {:s}$ y $C = {:s}$, ¿cuál de las siguientes es la descripción más precisa de su relación?'.format(sA, sB, sC), options, (A, B, C)))
        else:
            questions.append(('With $A = {:s}$, $B = {:s}$ and $C = {:s}$, which of the following is the most precise description of their relationship?'.format(sA, sB, sC), options, (A, B, C)))  
        superset = sample(string.ascii_lowercase, randint(5, 8))
        k = len(superset)
        A, B = superset, sample(superset, k - randint(0, k // 2))
        if random() < 0.5:
            A, B = B, A
        sA = '\\{{ {:s} \}}'.format(', '.join(A))
        sB = '\\{{ {:s} \}}'.format(', '.join(B))
        sA.replace('\\{  \\}', '\\emptyset')
        sB.replace('\\{  \\}', '\\emptyset')
        sC.replace('\\{  \\}', '\\emptyset')        
        options = ['$A \subset B$', '$A \supset B$', '$A \subseteq B$', '$A \supseteq B$']
        if lan == 0:
            options.append('ninguna')
        else:
            options.append('none')
        # 17 subsets and supersets
        shuffle(options)
        if lan == 0:
            questions.append(('Teniendo $A = {:s}$ y $B = {:s}$, ¿cuál de las siguientes es la descripción más precisa de su relación?'.format(sA, sB), options, (A, B)))
        else:
            questions.append(('With $A = {:s}$ and $B = {:s}$, which of the following is the most precise description of their relationship?'.format(sA, sB), options, (A, B)))
        A = sample([c for c in string.ascii_lowercase], randint(4, 7))
        sA = '\\{{ {:s} \}}'.format(', '.join(A))
        corr = factorial(len(A))
        options = set()
        while len(options) < 5:
            options.add(randint(2, 7 * corr))
        if corr not in options:
            options.remove(sample(options, 1)[0])
            options.add(corr)
        options = list(options)
        shuffle(options)
        # 18 factorial
        if lan == 0:
            questions.append(('¿Cuánto vale $|{:s}|!$?'.format(sA), options, A))
        else:
            questions.append(('What is the value of $|{:s}|!$?'.format(sA), options, A))
        A = set([string.ascii_lowercase[randint(0, 20)] for p in range(4, 8)])
        sA = '\\{{ {:s} \}}'.format(', '.join(A))
        ck = len(A)
        corr = 2**ck
        options = set()
        while len(options) < 5:
            if random() < 0.5:
                options.add(2**randint(0, ck + 2))
            else:
                options.add(randint(0, 2 * corr))                
        options = sample(options, 5)        
        if corr not in options:
            options.remove(sample(options, 1)[0])
            options.append(corr)        
        # 19 conjunto potencia 
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuánto vale $|2^{{ {:s} }}|?$'.format(sA), options, A))
        else:
            questions.append(('What is the value of $|2^{{ {:s} }}|?$'.format(sA), options, A))
        n = randint(10, 15)
        k = randint(2 , n - 2)        
        options = {binom(n, h) for h in range(k - 2, k + 2)}
        while len(options) < 5:
            options.add(randint(0, 2**n))
        options = sample(options, 5)
        corr = binom(n, k)
        if corr not in options:
            options.remove(sample(options, 1)[0])
            options.append(corr)
        # 20 binomioal coefficient
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuánto vale $\\binom{{ {:d} }}{{ {:d} }}?$'.format(n, k), options, (n, k)))
        else:
            questions.append(('What is the value of $\\binom{{ {:d} }}{{ {:d} }}?$'.format(n, k), options, (n, k)))
    if 'ord' in kind:
        n = randint(5, 8)
        V = set([string.ascii_lowercase[i] for i in range(0, n)])
        m = n + randint(2, 5)
        E = dict()
        A = defaultdict(set)
        while len(E) < m:
            e = sample(V, 2)
            u = min(e)
            v = max(e)
            A[u].add(v)
            A[v].add(u)
            w = randint(1, 9)
            E[(u, v)] = w
        possibles = [str(n + i) for i in range(-3, 3)]
        possibles += [str(m + i) for i in range(-3, 3)]
        possibles = set(possibles)
        options = sample(possibles, 5)
        if str(n) not in options:
            options.remove(sample(options, 1)[0])
            options.append(str(n))
        # 1: order
        shuffle(options)
        if lan == 0:
            questions.append(('¿Cuál es el orden del grafo $G = (V, E)$ donde $V = \{' +
                              ', '.join([v for v in sorted(list(V))]) + '\}$ y $E = \{' +
                              ', '.join(['({:s}, {:s}): {:d}'.format(e[0], e[1], w) for (e, w) in E.items()]) + ' \}$', options, V))
        else:
            questions.append(('What is the order of the graph $G = (V, E)$ where $V = \{' +
                              ', '.join([v for v in sorted(list(V))]) + '\}$ and $E = \{' +
                              ', '.join(['({:s}, {:s}): {:d}'.format(e[0], e[1], w) for (e, w) in E.items()]) + ' \}$', options, V))        
        deg = {v: len(A[v]) for v in V}
        options = set([i for i in range(0, max(deg.values()) + 2)] + [str(Fraction(m + randint(0, m), n + randint(-n, n) // 2)) for i in range(4)])
        options = sample(list(options), 5)
        v = sample(V, 1)[0]

# short answer question example: logarithms of arbitrary bases and rounding
def logarithm(target, points = 1, level = 1, rows = 1, cols = 3):
    title = 'Logarithm'
    n = randint(100, 999)
    b = randint(2, 8)
    o = choice(['ceil', 'floor'])    
    corr = log(n, b)
    if o == 'ceil':
        corr = ceil(corr)
    else:
        corr = floor(corr)
    question = 'What is the value of $\\l{:s}\\log_{:d} {:d}\\r{:s}$?'.format(o, b, n, o)
    hint = '''Think of which power of the base is the closest to the number.
Remember to use the correct rounding rule to deal with any potential decimal places. Type only the digits of your answer as your response with no additional information'''
    feedback = '''Being able to estimate logarithms in arbitrary bases,
especially without recurring to a calculator,
is an important skill for a programmer.'''
    print('NewQuestion,SA,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Points,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused
    print(f'InputBox,{rows},{cols},,', file = target)
    print(f'Answer,{pts},{corr},,,') # there could be more alternatives with partial credit
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

from boolean import boolean
        
# true/false example: evaluating a boolean expression
def booleval(target, points = 1, level = 1):
    bop = {'X': '\\oplus', 'A': '\\wedge', 'O': '\\vee', 'I': '\\rightarrow', 'E': '\\leftrightarrow', 'N': '\\neg'}
    cand = bop.keys() -  {'0', '1', 'N'}
    bor = sample(cand, 3)
    negs = ['N' if random() < 0.5 else '' for i in range(3)]
    expr = 'a {:s} b {:s} c {:s} d'.format(bor[0], bor[1], bor[2])
    shuffle(bor)
    sp = ' '.join(bor) 
    q = expr
    lp = sp[::-1] # reverse
    prec = lp
    for op in bop: # prepare as LaTeX
        q = q.replace(op, bop[op]) 
        lp = lp.replace(op, bop[op])
    a = 'top' if random() < 0.5 else 'bot'
    b = 'top' if random() < 0.5 else 'bot'
    c = 'top' if random() < 0.5 else 'bot'
    d = 'top' if random() < 0.5 else 'bot'
    val = '$a = \{:s}, b = \{:s}, c = \{:s}, d = \{:s}$'.format(a, b, c, d)
    result = boolean(expr, prec)
    title = 'Boolean logic'
    question = 'With precedence, from highest to lowest, $ {:s} $, and the assignment {:s}, what is the value of ${:s}$?'.format(lp, val, expr)
    hint = '''Assign the truth values into the variables in the expression.
    Then, starting from the highest-precedence operator, compute its value.
    Use the value of each operator evaluation as an input in the follow-up evaluations until you each the final result.'''
    feedback = '''Remember that if there were any negations (a unary operator), they would have the highest precedence.
    The only way to alter that would be by placing parenthesis around subexpressions to indicate that they should be evaluated
    before taking the negation.'''
    print('NewQuestion,TF,,,', file = target)
    print(f'ID,{qid},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Points,{pts},,,', file = target)
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

# matching
def integers(target):
    used = set()
    # small base to decimal
    n = ''.join([digit(randint(0, b - 1)) for x in range(3)]) # three digits
    used.add(n)
    b = randint(2, 9)
    sb = '${:s}_{:d}$?'.format(n, b)
    sbc = '$' + int(n, b) + '$'
    # large base to decimal
    while n in used:
        n = ''.join([digit(randint(0, b - 1)) for x in range(3)]) # three digits
    used.add(n)
    b = randint(11, 22)
    lb = '${:s}_{:d}$?'.format(n, b)
    lbc = '$' + int(n, b) + '$'
    # binary to octal
    while n in used:
        binary = '1{:s}'.format(''.join([str(randint(0, 1)) for x in range(5)]))
        n = int(b, 2)
    used.add(n)
    boctal = oct(n)[2:] 
    sbo = '${:s}_2$?'.format(binary)
    # octal to hexadecimal
    while n in used:
        n = ''.join([str(randint(0, 7)) for i in range(3)]).lstrip('0')
    used.add(n)
    hos = '${:s}_8$?'.format(n)
    hhs = '${:s}_16$?'.format(hex(int(n, 8))[2:])
    print('NewQuestion,M,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    title = 'Integer bases'
    question = 'Match integer representations that correspond to the same numerical value.'
    hint = '''One way to work this out would be converting all the values into the same base.
    Two and ten are often convenient options.'''
    feedback = '''Try to avoid memorizing conversion tricks.
    It is more fruitful to develop a conceptual understanding of the meaning of digits and their positions within a number'''
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Points,{pts},,,', file = target)
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


def modulo(target): # multiple choice example question: modulo
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
    question = 'What is the value of ${:d} \\bmod {:d}$?'.format(a, b)
    hint =
    '''Recall that the modulo operator refers to the residue of an integer division.
    In programming, the percent sign is often used to signify this operation.'''
    feedback = 'Much of cryptography is based on modular arithmetic, but it is also handy for programmers in general.'
    print('NewQuestion,MC,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Points,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused       
    print(f'Option,100,{corr},,Nice work', file = target)
    for other in options:
        # partial credit could also be given by indicating a value > 0 but < 100        
        print(f'Option,0,${other}$,,Just remove all multiples of the divisor while the result remains non-negative.', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)


from btree import Tree, 
    
# multiselect: pick the leaves
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
    title = 'Binary trees'
    question = 'Let $A$ be the binary tree that results from inserting the key sequence $' +
    ','.join([ str(k) for k in keys ]) +
    '$. Identify which of the following keys become leaves of the resulting tree after all keys have been inserted.'
    hint = '''The first kety becomes the root.
    Then, recursively, smaller values go into the left branch and larger values into the right.
    Any node that has neither a left nor a right branch underneath it is a leaf.'''
    feedback = 'When you are systematic and disciplined about always starting at the root and following the rules, this is an easy task.'
    print('NewQuestion,MS,,,', file = target)
    print(f'ID,{qid()},,,', file = target)
    print(f'Title,{title},,,', file = target)
    print(f'QuestionText,{question},,,', file = target)
    print(f'Points,{pts},,,', file = target)
    print(f'Difficulty,{level},,,', file = target)
    print('Image,,,,', file = target) # unused           
    print('Scoring,RightAnswers,,,', file = target) # unsure what the other options are like
    points = count * 2
    options = sample(leaves, count) + sample(internal, count)
    shuffle(options)
    for option in options:
        pick = 1 * (option in leaves) # 1 is yes, 0 is no
        fb = 'This is a leaf node' if pick == 1 else 'This is an internal node'
        print(f'Option,{pick},{option},,{fb}', file = target)
    print(f'Hint,{hint},,,', file = target)
    print(f'Feedback,{feedback},,,', file = target)

# PENDING
    
'''# ordering: vertex degree
NewQuestion,O,,,
ID,CHEM110-240,,,
Title,This is an ordering question,,,
QuestionText,This is the question text for O1,,,
Points,2,,,
Difficulty,2,,,
Scoring,RightMinusWrong,,,
Image,images/O1.jpg,,,
Item,This is the text for item 1,NOT HTML,This is feedback for option 1,
Item,This is the text for item 2,HTML,This is feedback for option 2,
Hint,This is the hint text,,,
Feedback,This is the feedback text,,,

# written response
NewQuestion,WR,,,
ID,CHEM110-234,,,
Title,This is a written response question,,,
QuestionText,This is the question text for WR1,,,
Points,1,,,
Difficulty,7,,,
Image,images/LA1.jpg,,,
InitialText,This is the initial text,,,
AnswerKey,This is the answer key text,,,
Hint,This is the hint text,,,
Feedback,This is the feedback text,,,
'''
