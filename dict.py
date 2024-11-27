dict1={2:"orange",4:"apple",1:"banana",3:"grapes"}
print(f"dictionary1: {dict1.items()}")
l=list(dict1.items())
l.sort()
print('ascending order is:',l)
l.sort(reverse=True)
print('descending order is:',l)
l.sort()
dict3=dict(l)
dict2={5:"plum",6:"cherry"}
dict3.update(dict2)
print(dict3)
