s='aabbba'
print(''.join([j for i,j in enumerate(s) if j not in s[:i]]))
