arquivo = '/home/pintermaciel/code/adventofcode/adventofcode/day1/input.txt'

lista1 = []
lista2 = []

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

print("Lista 1 ordenada:", list1)
print("Lista 2 ordenada:", list2)
print("Distâncias:", distances)
print("Soma das distâncias:", total_distance)
