import math
import decimal


def right_shift(formatted):
    return formatted+ '1'

def plus(formatted):
    print(len(formatted))
    incre= len(formatted)*'0'
    print(incre)
    incre= '0.'+ incre[2:]
    print(incre)
    incre= incre[:-1]+ '1'
    
    formatted_target= decimal.Decimal(formatted)
    increment= decimal.Decimal(incre)
    
    sum= formatted_target+ increment
    return_sum= format(sum,'.'+str(len(formatted)-2)+'f')
    print(return_sum)
    
    return return_sum
    

decimal.getcontext().prec= 32
pi= decimal.Decimal('3.141592653589793238462643383279')
root_two= decimal.Decimal('1.414213562373095048801688724209')


f= (pi-3)/8
q= 1/(pi-2*root_two)

f= decimal.Decimal(format(f, '.8f'))
q= decimal.Decimal(format(q, '.9f'))

i= 3+ f*8
a= i- 2*root_two
o= (3-(2*root_two+f*8))
v= (3-2*root_two-o)*2
b= 1/a
h_i= 1/q+ 2*root_two
g= ((root_two*b/2)*(root_two*b-b))/2
d= ((root_two*q/2)*(root_two*q-q))/2

print(a,i,o,v,b,h_i,g,d)