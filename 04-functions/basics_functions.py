# def multiply(a, b):
#     return a * b

# print(multiply(3, 5))
#-------------------------------------------------

# def bigger(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(bigger(10, 7))
# --------------------------------------------------

# materials = {
#     "Concrete": 300,
#     "Steel": 75,
#     "Wood": 75,
#     "Asphalt": 450
# }

# def total_materials(materials):
#     total = 0
#     for m in materials:
#         total += materials[m]
#     return total

# print(total_materials(materials))
# ----------------------------------------------------

# materials = {
#     "Concrete": 300,
#     "Steel": 75,
#     "Wood": 75,
#     "Asphalt": 450
# }

# def max_material(materials):
#     max_value = 0
#     max_name = ""
#     for m in materials:
#         if materials[m] > max_value:
#             max_value = materials[m]
#             max_name = m
#     return max_name, max_value

# print(max_material(materials))
# ----------------------------------------------------

# projects = {
#     "Project A": {"Walls": 120, "Doors": 30},
#     "Project B": {"Walls": 80, "Doors": 20},
#     "Project C": {"Walls": 150, "Doors": 40}
# }

# def total_walls(projects):
#     total = 0
#     for p in projects:
#         for m in projects[p]:
#             if m == "Walls":
#                 total += projects[p][m]
#     return total

# print(total_walls(projects))
# --------------------------------------------------

# projects = {
#     "Project A": {"Walls": 120, "Doors": 30},
#     "Project B": {"Walls": 80, "Doors": 20},
#     "Project C": {"Walls": 150, "Doors": 40}
# }

# def total_walls(projects,category):
#     total = 0
#     for p in projects:
#         for m in projects[p]:
#             if m == category:
#                 total += projects[p][m]
#     return total

# print(total_walls(projects, "Walls"))
# print(total_walls(projects, "Doors"))
# --------------------------------------------------------

projects = {
    "Project A": {"Walls": 120, "Doors": 30},
    "Project B": {"Walls": 80, "Doors": 20},
    "Project C": {"Walls": 150, "Doors": 40}
}

def project_totals(projects):
    total = {}
    for p in projects:
        value = 0
        for m in projects[p]:
            value += projects[p][m]
        total[p] = value
    return total

print(project_totals(projects))
