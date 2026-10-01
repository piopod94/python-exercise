# Exc 6 give back keys and values

materials = {
    "Concrete": 300,
    "Steel": 75,
    "Wood": 75,
    "Asphalt": 450
}

for m in materials:
    # print(f"{m} -> {materials[m]}")
    print(materials[m])

# # give material and min value

# import math

# min_val = math.inf
# min_material = ""

# for m in materials:
#     if materials[m] < min_val:
#         min_val = materials[m]
#         min_material = m
# print(min_material)
# print(min_val)

# Exc 7 dict with 2 levels
# give back the number of walls in project A
# give back the number of walls in both projects

# projects = {
#     "Project A": {
#         "Walls": 120,
#         "Doors": 30
#     },
#     "Project B": {
#         "Walls": 80,
#         "Doors": 20
#     }
# }

# # print(projects["Project A"]["Walls"])

# counter = 0
# for p in projects:
#     counter += projects[p]["Walls"]

# print(counter)

#Exc 8 Find pProject with the biggest ammount of walls

# projects = {
#     "Project A": {
#         "Walls": 120,
#         "Doors": 30
#     },
#     "Project B": {
#         "Walls": 80,
#         "Doors": 20
#     },
#     "Project C": {
#         "Walls": 150,
#         "Doors": 10
#     }
# }

# p_name = ""
# w_value = 0

# for p in projects:
#     if projects[p]["Walls"] > w_value:
#         w_value = projects[p]["Walls"]
#         p_name = p
# print(p_name)
# print(w_value)

#Summ all the elements (walls and dors) for all projects

# value = 0

# for p in projects:
#     x = projects[p]["Walls"] + projects[p]["Doors"]
#     value += x
# print(value)

# # Sum Walls and Dors for each project.
# projects = {
#     "Project A": {
#         "Walls": 120,
#         "Doors": 30
#     },
#     "Project B": {
#         "Walls": 80,
#         "Doors": 20
#     },
#     "Project C": {
#         "Walls": 150,
#         "Doors": 10
#     }
# }

# totals = {}

# for p in projects:
#     totals[p] = projects[p]["Walls"] + projects[p]["Doors"]

# print(totals)

# for t in totals:
#     if totals[t] >= 150:
#         print(f"{t} -> Large")
#     else:
#         print(f"{t} -> Small")
