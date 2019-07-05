import re
import os


def maketable(x, y):
    l = list()
    s = re.split('}(?:\n|, *\n) *', x)
    del s[-1]
    s.sort()
    c = re.match('^ *(.*?)/', x).group(1)  # get type
    for j in s:  # split up into each definition
        n = re.search('.*?/(.*?)/', j).group(1)  # get name
        if n == 'none' or n == '.unknown':
            continue  # skip if a blank placeholder
        ro = r'\texttt{' + n + r'} & \adjustbox{valign=m,margin=0.25cm}{\tikz{' \
                         r'\Mil' + y + r'[faction=none, ' + c + r'=' + n + r']}}' \
                         r' & \adjustbox{valign=m,margin=0.25cm}{\tikz{' \
                         r'\Mil' + y + r'[faction=friendly, ' + c + r'=' + n + r']}}' \
                         r' & \adjustbox{valign=m,margin=0.25cm}{\tikz{' \
                         r'\Mil' + y + r'[faction=hostile, ' + c + r'=' + n + r']}}' \
                         r' & \adjustbox{valign=m,margin=0.25cm}{\tikz{' \
                         r'\Mil' + y + r'[faction=neutral, ' + c + r'=' + n + r']}}' \
                         r' & \adjustbox{valign=m,margin=0.25cm}{\tikz{' \
                         r'\Mil' + y + r'[faction=unknown, ' + c + r'=' + n + r']}}' \
                         r'\\ \hline'
        l.append(ro)
    ta = '\\begin{tabularx}{\\linewidth}{|m{5cm}|c|c|c|c|c|}\n\\hline\n \\thead{Value} & ' \
         '\\thead{Glyph} & \multicolumn{4}{c|}{\\thead{Examples}} \\\\ ''\n\\hline\n' + '\n'.join(l) + '\n\\' \
         'caption{Table for \\texttt{' + c + '} values in the \\textbf{\\texttt{Mil' + y + '}} command.}' \
         '\n\\end{tabularx}'
    ofn = os.path.join(dr, y + '_' + c + '_table.tex')
    of = open(ofn, 'w')
    of.write(ta)
    of.close()


dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../milsymb.sty')
f = open(fn, 'r')
r = f.read()
f.close()
for i in ['Air', 'Missile', 'Land', 'Equipment', 'Installation', 'SeaSurface', 'SeaSubsurface', 'Space', 'Activity']:
    if i == 'Missile':
        t = re.search(
            r'\\NewDocumentCommand\\MilMissile{ o D\(\)\{0,0} d\(\) g}{'
            r'.*left/\.is choice,\n *?(.*?)^(?! *left)'
            r'.*right/\.is choice,\n *?(.*?)^(?! *right)',
            r, re.S | re.M)
        maketable(t.group(1), i)  # left
        maketable(t.group(2), i)  # right
    elif i == 'Equipment':
        t = re.search(
            r'\\NewDocumentCommand\\MilEquipment{ o D\(\)\{0,0} d\(\) g}{'
            r'.*main/\.is choice,\n *?(.*?)^(?! *main)'
            r'.*mobility/\.is choice,\n *?(.*?)^(?! *mobility)',
            r, re.S | re.M)  # extract all main, mobility
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # mobility
    elif i == 'Installation' or i == 'Activity':
        t = re.search(
            r'\\NewDocumentCommand\\Mil' + i + '{ o D\(\)\{0,0} d\(\) g}{.*?main/\.is choice,\n *(.*?)^(?! *main)'
            r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)',
            r, re.S | re.M)  # extract all main, upper
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # upper
    else:
        t = re.search(
            r'\\NewDocumentCommand\\Mil' + i + '{ o D\(\)\{0,0} d\(\) g}{.*?main/\.is choice,\n *(.*?)^(?! *main)'
            r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)'
            r'.*?lower/\.is choice,\n *(.*?)^(?! *lower)',
            r, re.S | re.M)  # extract all main, upper, lower
        maketable(t.group(1), i)  # main
        maketable(t.group(2), i)  # upper
        maketable(t.group(3), i)  # lower
