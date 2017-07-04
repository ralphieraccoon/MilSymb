import re

#f = open('nato2.tex', 'r')
f = open(r'C:\Users\UoM\Documents\NATOSymb\nato2.tex', 'r')
r = f.read()
f.close()
m = re.search('%% AIR SYMBOLS %%(.*)%% TEMPLATES %%', r, re.S) #find section containing symbol names.
l = re.findall('NATOSymb (.*)/.pic', m.group(0)) #output a list of all symbol names.
d = list()
for i in l: #convert list to dictionary for grouping
  t = re.split('/', i)
  try:
    c = {'fullstring' : i, 'type': t[0], 'position': t[1], 'name': t[2], 'faction': t[3]} 
  except IndexError:
        try:
          c = {'fullstring' : i, 'type': t[0], 'position': t[1], 'name': t[2]}
        except IndexError:
          c = {'fullstring' : i, 'type': t[0], 'name': t[1]}
  d.append(c)
s = set([ i['type'] for i in d ])
h = ['main', 'upper', 'lower']
k = list()
for i in s: #create table strings
    if i != 'multi'
        if i == 'supply'

        else
            for j in h:
                e = [j['name'] + '& \tikz{\pic{' + j['fullstring'] + '};}\\' for j in d if d['type'] == i and d['position'] == j]
