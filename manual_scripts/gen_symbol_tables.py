import re
import os

dr = os.path.dirname(__file__)
fn = os.path.join(dr, '../nato2.tex')
f = open(fn, 'r')
r = f.read()
f.close()
m = list()
for i in ['Air','Missile','Land']:
  if i != 'Missile':
    t = re.search(r'\\newcommand\{\\NATO' + i + '\}\[\d\]\[\]\{.*?main\/.is choice,(.*?)upper\/.is choice,(.*?)lower\/.is choice,(.*?)^(?:(?!lower).)*$', r, re.S | re.M)
    for j in re.split('},', t.group(1)):
      pass
  else:
    t = re.search(r'\\newcommand\{\\NATOMissile\}\[\d\]\[\]\{.*?left\/.is choice,(.*?)right\/.is choice,(.*?)^(?:(?!right).)*$', r, re.S | re.M)

		
def maketable(x):
  return  '''\begin{tabular}{ |c|c|c| } 
\hline
\bfseries{Function} & \bferies{Icon} & \bfseries{Example} \\ 
\hline'''
  + ''.join[ k['name'].capitalize() + '''& \tikz{\pic{''' + k['icon'] + '''}} & \tikz{''' +  + '''\\''' for k in x] + '''\hline
\end{tabular}'''
