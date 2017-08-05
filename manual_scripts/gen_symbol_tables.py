import re
import os


def maketable(x, y):
    l = list()
    s = re.split('}(?:\n|, *\n) *', x)
    del s[-1]
    for j in s:  # split up into each definition
        n = re.search('.*?/(.*?)/', j).group(1)  # get name
        if n == 'none':
            continue  # skip if a blank placeholder
        if re.search('symb[CUL]T=', j):  # detect if text based
            e = re.search('symb[CUL]T=(.*)$', j).group(1)  # get text
            if re.search('squashed', j):  # regular or squashed text
                ro = n.title() + r' & \tikz{\pic{NATOSymb main/textsquashed={' + e + r'}} & ' + e + ' \\\\ \n\\hline'
            else:
                ro = n.title() + r' & \tikz{\pic{NATOSymb main/text={' + e + r'}}} & ' + e + ' \\\\ \n\\hline'
        else:
            p = re.search('symb[CUL]=(.*)(?:,|$)', j).group(1)  # get shape path
            ro = n.title() + r' & \tikz{\pic{NATOSymb ' + p + r'}} & ' + p + ' \\\\ \n\\hline'
        l.append(ro)
    ta = '\\begin{tabular}{|c|c|c|}\n\\hline\n\\bfseries{Name} & \\bfseries{Symbol} & \\bfseries{Examples} \\\\ ' \
         '\n\\hline\n' + '\n'.join(l) + '\n\\end{tabular}'
    ofn = os.path.join(dr, y + '_' + re.match('^(.*?)/', x).group(1) + '_table.tex')
    of = open(ofn, 'w')
    of.write(ta)
    of.close()


dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../nato2.tex')
f = open(fn, 'r')
r = f.read()
f.close()
for i in ['Air', 'Missile', 'Land']:
    if i != 'Missile':
        t = re.search(
            r'\\newcommand{\\NATO' + i + '\}\[\d\]\[\]{.*?main/\.is choice,\n *(.*?)^(?! *main)'
                                         r'.*upper/\.is choice,\n *(.*?)^(?! *upper)'
                                         r'.*lower/\.is choice,\n *(.*?)^(?! *lower)',
            r, re.S | re.M)  # extract all main, upper, lower
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # upper
        maketable(t.group(3), i)  # lower
    else:
        t = re.search(
            r'\\newcommand{\\NATOMissile\}\[\d\]\[\]{'
            r'.*left/\.is choice,\n *(.*?)^(?! *left)'
            r'.*right/\.is choice,\n *(.*?)^(?! *right)',
            r, re.S | re.M)
        maketable(t.group(1), i)  # left
        maketable(t.group(2), i)  # right
