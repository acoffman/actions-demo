import csv
import matplotlib.pyplot as plt

xVals = []
yVals = []

with open('data.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        xVals.append(int(row['x']))
        yVals.append(int(row['y']))

plt.scatter(xVals, yVals)
plt.xlabel('Month')
plt.ylabel('Count')
plt.savefig('site/plot.png')
