import csv
from collections import Counter

def mean(vals) :
    
    total_val = 0
    lent = len(vals)
    mean = 0

    for i in vals:
        total_val += i

    mean = total_val/lent
    return mean

def median(vals) :

    lent = len(vals)
    sorted_val = vals.sort()

    if lent % 2 == 0:
        mid1 = lent//2
        mid2 = mid1+1
        val1 = vals[mid1]
        val2 = vals[mid2]
        median = mean([val1, val2])

        return median

    else:

        mid = lent /2
        median = vals[mid]
        return median

def mode(vals):
    floored_vals = []

    for v in vals:
        f_v = v//1
        floored_vals.append(f_v)

    freq = Counter(floored_vals)
    mode = freq.most_common(1)[0][0]
    return mode


with open("data.csv", newline="") as raw_data:
    data = csv.reader(raw_data)
    file_data = list(data)
    

file_data.pop(0)
total_weight = 0
total_entries = len(file_data)
sorted_data = []

for i in file_data:
    total_weight += float( i[2] )
    sorted_data.append( float( i[2] ) )

sorted_data.sort()
weight_mean = mean(sorted_data)
weight_median = median(sorted_data)
weight_mode = mode(sorted_data)

print(f"Mean of Weight = {weight_mean}")
print(f"Median of Weight = {weight_median}")
print(f"Mode of Weight = {weight_mode}")