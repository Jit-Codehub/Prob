import math
def circular_permutation(n):
    v=[]
    a=v.append
    a('<p>(n−1)!=?</p>')
    a('<p>(n−1)! = ({}−1)!</p>'.format(n))
    a('<p>= {}!</p>'.format(n-1))
    ans=math.factorial(n-1)
    a('<p>= {}</p>'.format(ans))
    return ''.join(v),ans