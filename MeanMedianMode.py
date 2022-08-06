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
    data = Counter(vals)
    mode_data_for_range = {
        "50-60": 0,
        "60-70": 0,
        "70-80": 0
    }
    for height, occurence in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"] += occurence
        elif 60 < float(height) < 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 < float(height) < 80:
            mode_data_for_range["70-80"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
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
