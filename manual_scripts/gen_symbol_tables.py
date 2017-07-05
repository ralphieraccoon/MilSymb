import re
import os


def maketable(x, y):
    l = list()
    for j in re.split('}, *\n *', x):  # split up into each definition
        n = re.search('.*?/(.*?)/', j).group(1)  # get name
        if re.search('symb[CUL]T=', j):  # detect if text based
            e = re.search('symb[CUL]T=(.*)$', j).group(1)  # get text
            if re.search('squashed', j):  # regular or squashed text
                ro = n.capitalize() + r' & \tikz{\pic{NATOSymb main/textsquashed={' + e + r'}} & ' + e + r' \\'
            else:
                ro = n.capitalize() + r' & \tikz{\pic{NATOSymb main/text={' + e + r'}}} & ' + e + r' \\'
        else:
            p = re.search('symb[CUL]=(.*)(?:,|$)', j).group(1)  # get shape path
            ro = n.capitalize() + r' & \tikz{\pic{NATOSymb ' + p + r'}} & ' + p + r' \\'
        l.append(ro)
    return l

dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../nato2.tex')
f = open(fn, 'r')
r = f.read()
f.close()
m = list()
for i in ['Air', 'Missile', 'Land']:
    if i != 'Missile':
        t = re.search(
            r'\\newcommand{\\NATO' + i + '\}\[\d\]\[\]{.*?main/.is choice,\n *(.*?)},\n *'
                                         'upper/.is choice,\n *(.*?)},\n *'
                                         'lower/.is choice,\n *(.*?)},\n *^(?:(?!lower).)*$',
            r, re.S | re.M)  # extract all main, upper, lower
        m.append(maketable(t.group(1), i))  # main
        m.append(maketable(t.group(2), i))  # upper
        m.append(maketable(t.group(3), i))  # lower
    else:
        t = re.search(
            r'\\newcommand{\\NATOMissile\}\[\d\]\[\]{.*?left/.is choice,\n *(.*?)},\n *'
            r'right/.is choice,\n *(.*?)},\n *^(?:(?!right).)*$',
            r, re.S | re.M)
        m.append(maketable(t.group(1)))  # left
        m.append(maketable(t.group(2)))  # right
