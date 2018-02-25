import re
import os

dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../milsymb.sty')
f = open(fn, 'r')
r = f.read()
f.close()

li = []

for i in ['Air', 'Missile', 'Land', 'Equipment', 'Installation', 'SeaSurface', 'SeaSubsurface', 'Space', 'Activity']:
    if i == 'Missile':
        t = re.search(
            r'\\NewDocumentCommand\\MilMissile{ o D\(\)\{0,0} d\(\) g}{'
            r'.*left/\.is choice,\n *?(.*?)^(?! *left)'
            r'.*right/\.is choice,\n *?(.*?)^(?! *right)',
            r, re.S | re.M)
        li.extend(re.split('}(?:\n|, *\n) *', t.group(1)))
        li.extend(re.split('}(?:\n|, *\n) *', t.group(2)))

    elif i == 'Equipment':
        t = re.search(
            r'\\NewDocumentCommand\\MilEquipment{ o D\(\)\{0,0} d\(\) g}{'
            r'.*main/\.is choice,\n *?(.*?)^(?! *main)'
            r'.*mobility/\.is choice,\n *?(.*?)^(?! *mobility)',
            r, re.S | re.M)  # extract all main, mobility
        li.extend(re.split('}(?:\n|, *\n) *', t.group(1)))
        li.extend(re.split('}(?:\n|, *\n) *', t.group(2)))

    elif i == 'Installation' or i == 'Activity':
        t = re.search(
            r'\\NewDocumentCommand\\Mil' + i + '{ o D\(\)\{0,0} d\(\) g}{.*?main/\.is choice,\n *(.*?)^(?! *main)'
            r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)',
            r, re.S | re.M)  # extract all main, upper
        li.extend(re.split('}(?:\n|, *\n) *', t.group(1)))
        li.extend(re.split('}(?:\n|, *\n) *', t.group(2)))

    else:
        t = re.search(
            r'\\NewDocumentCommand\\Mil' + i + '{ o D\(\)\{0,0} d\(\) g}{.*?main/\.is choice,\n *(.*?)^(?! *main)'
            r'.*?upper/\.is choice,\n *(.*?)^(?! *upper)'
            r'.*?lower/\.is choice,\n *(.*?)^(?! *lower)',
            r, re.S | re.M)  # extract all main, upper, lower
        li.extend(re.split('}(?:\n|, *\n) *', t.group(1)))
        li.extend(re.split('}(?:\n|, *\n) *', t.group(2)))
        li.extend(re.split('}(?:\n|, *\n) *', t.group(3)))

li = list(filter(None, li))

li = [re.search('Symb[CUL]=(.*?)(?:,|}|/\\\MilSymb@selectedfaction|$)', k).group(1) for k in li]

co = re.search('%% AIR SYMBOLS %%(.*)%% TEMPLATES %%', r, re.S | re.M).group(1)

co = re.findall('MilSymb (.*?/.*?/.*?)(?:/.*?)?/.pic', co)

li = set(li)

co = set(co)

d = co.difference(li)

d = list(filter(lambda i: not re.search('(multi|/debris/|/mine/)', i), list(d)))

d.sort()

pass
