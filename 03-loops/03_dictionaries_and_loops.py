projects = {
    "Project A": {
        "Walls": 120,
        "Doors": 30,
        "Windows": 50
    },
    "Project B": {
        "Walls": 80,
        "Doors": 20,
        "Windows": 40
    },
    "Project C": {
        "Walls": 150,
        "Doors": 10,
        "Windows": 60
    }
}


# count all elements in all projects using nested loops


# for p in projects:
#     total = 0
#     for element in projects[p]:
#        total += projects[p][element]
#     print(f"{p} -> {total}")

total = {}

for p in projects:
    for element in projects[p]:
       if element in total:
           total[element] += projects[p][element]
       else:
           total[element] = projects[p][element]

# print(total)

# find category with the biggest amount of objects

max_amount = 0
max_materai = ""

for t in total:
    if total[t] > max_amount:
        max_amount = total[t]  
        max_materai = t

print(max_materai)
print(max_amount)