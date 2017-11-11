
"""
s = [-5, -23, 5, 0, 23, -6, 23, 67]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)

print nl
"""


# wrapper for the above code

def subsort(list):
    nl = []
    for i in range(len(list)):
        a = min(s)
        nl.append(a)
        s.remove(a)
    return nl

