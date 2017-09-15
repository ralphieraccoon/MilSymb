import re
import os


def maketable(x, y):
    l = list()
    s = re.split('}(?:\n|, *\n) *', x)
    del s[-1]
    c = re.match('^ *(.*?)/', x).group(1)  # get type
    for j in s:  # split up into each definition
        n = re.search('.*?/(.*?)/', j).group(1)  # get name
        if n == 'none':
            continue  # skip if a blank placeholder
        ro = n.title() + r' & \trimbox{0.25cm, 0.25cm, 0.25cm, 0.25cm}' \
                         r'{\tikz[baseline=-0.5ex, scale=2, transform shape]{\NATO' + y + \
                         r'[faction=none, ' + c + r'=' + n + r']{(0,0)}}} \\ \hline'
        l.append(ro)
    ta = '\\begin{longtable}{|c|m{2cm}|c|}\n\\hline\n\\bfseries{Name} & \\bfseries{Symbol} & \\bfseries{' \
         'Examples} \\\\ ''\n\\hline\n' + '\n'.join(l) + '\n\\end{longtable}'
    ofn = os.path.join(dr, y + '_' + c + '_table.tex')
    of = open(ofn, 'w')
    of.write(ta)
    of.close()


dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../milsymb.sty')
f = open(fn, 'r')
r = f.read()
f.close()
for i in ['Air', 'Missile', 'Land']:
    if i != 'Missile':
        t = re.search(
            r'\\newcommand{\\NATO' + i + '\}\[\d\]\[\]{.*?main/\.is choice,\n *(.*?)^(?! *main)'
                                         r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)'
                                         r'.*?lower/\.is choice,\n *(.*?)^(?! *lower)',
            r, re.S | re.M)  # extract all main, upper, lower
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # upper
        maketable(t.group(3), i)  # lower
    else:
        t = re.search(
            r'\\newcommand{\\NATOMissile\}\[\d\]\[\]{'
            r'.*left/\.is choice,\n *?(.*?)^(?! *left)'
            r'.*right/\.is choice,\n *?(.*?)^(?! *right)',
            r, re.S | re.M)
        maketable(t.group(1), i)  # left
        maketable(t.group(2), i)  # right
