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
        ro = n.title() + r' & \tikz[baseline=-0.5ex]{' \
                         r'\NATO' + y + r'[faction=none, ' + c + r'=' + n + r']}' \
                         r' & \tikz[baseline=-0.5ex]{' \
                         r'\NATO' + y + r'[faction=friendly, ' + c + r'=' + n + r']}' \
                         r' & \tikz[baseline=-0.5ex]{' \
                         r'\NATO' + y + r'[faction=hostile, ' + c + r'=' + n + r']}' \
                         r' & \tikz[baseline=-0.5ex]{' \
                         r'\NATO' + y + r'[faction=neutral, ' + c + r'=' + n + r']}' \
                         r' & \tikz[baseline=-0.5ex]{' \
                         r'\NATO' + y + r'[faction=unknown, ' + c + r'=' + n + r']}' \
                         r'&\\[1.25cm] \hline'
        l.append(ro)
    ta = '\\begin{tabularx}{\\linewidth}{|n|s|s|s|s|s|@{}m{0pt}@{}}\n\\hline\n \\thead{Name} & ' \
         '\\thead{Symbol} & \multicolumn{4}{c|}' \
         '{\\thead{Examples}} \\\\ ''\n\\hline\n' + '\n'.join(l) + '\n\\end{tabularx}'
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
            r'\\NewDocumentCommand\\NATO' + i + '{ o D\(\)\{0,0} d\(\) g}{.*?main/\.is choice,\n *(.*?)^(?! *main)'
                                                r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)'
                                                r'.*?lower/\.is choice,\n *(.*?)^(?! *lower)',
            r, re.S | re.M)  # extract all main, upper, lower
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # upper
        maketable(t.group(3), i)  # lower
    else:
        t = re.search(
            r'\\NewDocumentCommand\\NATOMissile{ o D\(\)\{0,0} d\(\) g}{'
            r'.*left/\.is choice,\n *?(.*?)^(?! *left)'
            r'.*right/\.is choice,\n *?(.*?)^(?! *right)',
            r, re.S | re.M)
        maketable(t.group(1), i)  # left
        maketable(t.group(2), i)  # right
