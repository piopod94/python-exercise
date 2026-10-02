# projects = {
#     "Project A": {
#         "Walls": 120,
#         "Doors": 30,
#         "Windows": 50
#     },
#     "Project B": {
#         "Walls": 80,
#         "Doors": 20,
#         "Windows": 40
#     },
#     "Project C": {
#         "Walls": 150,
#         "Doors": 10,
#         "Windows": 60
#     }
# }


# count all elements in all projects using nested loops


# for p in projects:
#     total = 0
#     for element in projects[p]:
#        total += projects[p][element]
#     print(f"{p} -> {total}")

# total = {}

# for p in projects:
#     for element in projects[p]:
#        if element in total:
#            total[element] += projects[p][element]
#        else:
#            total[element] = projects[p][element]

# # print(total)

# # find category with the biggest amount of objects

# max_amount = 0
# max_materai = ""

# for t in total:
#     if total[t] > max_amount:
#         max_amount = total[t]  
#         max_materai = t

# print(max_materai)
# print(max_amount)

# found the project which has the biggest number of elements and return the name of it

# max_amount = 0
# max_name = ""

# for p in projects:
#     total = 0
#     for element in projects[p]:
#         total += projects[p][element]
#     if total > max_amount:
#         max_amount = total
#         max_name = p

# print(max_name)
# print(max_amount)

# Find project with the bigest amount of walls
# biggest ammount of doors
# bigest amount of elements
# present the data in a raport

projects = {
    "Project A": {
        "Walls": 120,
        "Doors": 30,
        "Windows": 50
    },
    "Project B": {
        "Walls": 80,
        "Doors": 60,
        "Windows": 40
    },
    "Project C": {
        "Walls": 150,
        "Doors": 10,
        "Windows": 60
    },
    "Project D": {
        "Walls": 90,
        "Doors": 100,
        "Windows": 20
    }
}

max_amountw = 0
max_projectw = ""

for p in projects:
    if projects[p]["Walls"] > max_amountw:
        max_amountw = projects[p]["Walls"]
        max_projectw = p

max_amountd = 0
max_projectd = ""

for p in projects:
    if projects[p]["Doors"] > max_amountd:
        max_amountd = projects[p]["Doors"]
        max_projectd = p

max_project = ""
max_amount = 0

for p in projects:
    total = 0
    for elements in projects[p]:
        total += projects[p][elements]
    if total > max_amount:
        max_amount = total
        max_project = p


print(f"Largest wall project: {max_projectw}")
print(f"Largest door project: {max_projectd}")
print(f"Largest total project: {max_project}")