
from matplotlib import pyplot as plt
from matplotlib import style
from collections import defaultdict, Counter
import time
import numpy as np

import csv

file = "Crime Stats.csv"

f = ''

style.use('ggplot')


crimes = defaultdict(list)

with open(file, newline='') as csvfile:
    r = csv.DictReader(csvfile)

    i = 2000
    for row in r:
        x = row['OCCURRED ON']
        if not x: x = row['OCCURRED TO']
        crimes[row['UCR CRIME CATEGORY']].append(x)
        # i -= 1
        if not i: break


for crime in crimes:
    times = Counter()
    for entry in crimes[crime]:
        hour = time.strptime(entry.split()[-1], '%H:%M').tm_hour
        times[str(hour)] += 1

    x = sorted(int(t) for t in times)
    y = [times[str(t)] for t in x]
    plt.plot(x, y, linewidth=5, label=crime)
    # plt.scatter(x, y)


plt.title('Linear fit')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend(loc='upper right', prop={'size': 10})

plt.show()
