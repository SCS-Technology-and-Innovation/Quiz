
# https://www.tutorialspoint.com/data_structures_algorithms/expression_parsing_using_statck.htm
def postfix(expr, prec):
    expr = expr.replace(' ', '') # no spaces
    resultado = []
    pila = []
    for pedazo in expr:
        if pedazo not in prec: # no es operador
            resultado.append(pedazo)
        else:
            if pedazo == '(': # abre subexpresion
                pila.append(pedazo)
            else:
                if pedazo == ')': # cierra subexpresion
                    while True:
                        siguiente = pila.pop(-1)
                        if siguiente == '(':
                            break
                        else:
                            resultado.append(siguiente)
                        if len(pila) == 0:
                            print('Hay una parentesis que no se cierra, no es posible evaluar.')
                            return None
                else:
                    if len(pila) == 0 or prec.index(pedazo) > prec.index(pila[-1]):
                        pila.append(pedazo)
                    else:
                        while len(pila) > 0 and prec.index(pedazo) <= prec.index(pila[-1]): 
                            resultado.append(pila.pop(-1))
                        pila.append(pedazo)
    return resultado + pila[::-1]

def valor(a, b, op):
    if op in 'AOXIE': # operador booleano binario
        assert(a in '01' and b in '01') # acepta solamente bits
        if op == 'A': # and
            if a == '1' and b == '1': # ambos unos para que sea verdadero
                return '1'
            else:
                return '0'
        elif op == 'X': # xor
            if a != b: # con que sean diferentes
                return '1'
            else:
                return '0'
        elif op == 'E': # equivalencia
            if a == b: # con que sean iguales
                return '1'
            else:
                return '0'
        elif op == 'O': # or
            if a == '1' or b == '1': # con que hay por lo menos un uno
                return '1'
            else:
                return '0'
        else: # nada mas queda la implicacion como opcion
            assert op == 'I'
            if a == '0' or b == '1': # o no a o b
                return '1'
            else:
                return '0'
    elif op in '+-*/%': # aritmetica regular (de enteros en este caso)
        va = None
        vb = None
        try:
            va = int(a)
            vb = int(b)
        except:
            print('Se permite solamente enteros; no se puede evaluar de otra forma.')
            quit()
        if op == '+':
            return str(va + vb)
        elif op == '-':
            return str(va - vb)
        elif op == '*':
            return str(va * vb)
        if op in '/%':
            if vb == 0:
                print('No se puede realizar divisiones entre cero.')
                quit()
        if op == '/':
            return str(va // vb)
        if op == '%':
            return str(va % vb)
    else:
        print('Unexpected operator', op)

def boolean(expr, prec='EIXOA'): # toma como entrada la expresion en forma postfix
    prec = prec.replace(' ', '') # no spaces
    prec = '()' + prec + 'N' # add defaults
    pfe = postfix(expr, prec)
    pila = []
    while len(pfe) > 0:
        if pfe[0] not in prec: # no es un operador
            pila.append(pfe.pop(0))
        else: # es un operador
            operador = pfe.pop(0)
            if operador == 'N': # unario
                v = pila.pop(-1)
                assert v in '01' # solamente para bits
                if v == '1': # voltear el valor
                    pila.append('0')
                else:
                    pila.append('1')                
            else: # los demas son binarios
                ladoDer = pila.pop(-1)
                ladoIzq = pila.pop(-1)
                v = valor(ladoIzq, ladoDer, operador)
                pila.append(v)
    return pila[0]
