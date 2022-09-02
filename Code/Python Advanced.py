import numpy as np
from openpyxl import Workbook as wkb
from datetime import datetime as dt
import csv
import time

x23 = [[0]*4 for i in range(5)]

for i in range(5):
    for j in range(4):
        if j%4==0:
            x23[i][j]=(np.random.randint(1,10))
        if j%4==1:
            x23[i][j]=(np.random.randint(4,80))
        if j%4==2:
            x23[i][j]=(np.random.uniform(pow(10,-2),pow(10,-1)))
        if j%4==3:
            x23[i][j]=(np.random.uniform(pow(10,-7),pow(10,-5)))

print(x23)
           
for k in range(5):
        wb = wkb()
        ws = wb.active
        ws.append([1, 2, 3, 4, 5])
        ws.append(x23[k-1]+[np.random.randint(1,6)])
        wb.save('work'+str(k)+'.xlsx')
        with open('time'+str(k)+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time','cost'])
            writer.writerow(([dt.now().strftime('%Y%m%d%H%M%S')+'\t',np.random.random()])) 
            time.sleep(1)
