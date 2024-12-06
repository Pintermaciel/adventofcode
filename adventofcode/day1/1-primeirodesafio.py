from collections import Counter

arquivo = '/home/pintermaciel/code/adventofcode/adventofcode/day1/input.txt'

list1 = []
list2 = []

with open(arquivo, "r") as file:
    data = [
        line.split() for line in file if line.strip()
        ] 

list1 = [int(pair[0]) for pair in data]
list2 = [int(pair[1]) for pair in data]

list1.sort()
list2.sort()

distances = [abs(list1[i] - list2[i]) for i in range(len(list1))]

total_distance = sum(distances)


print("Soma das distâncias:", total_distance)


contalista2 = Counter(list2) 

similaridade = sum(num * contalista2[num] for num in list1)

print("Similaridade:", similaridade)