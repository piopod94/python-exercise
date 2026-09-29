# Exe.2 sum values for each element

# data = [
# ("Concrete", 100),
# ("Steel", 50),
# ("Concrete", 200),
# ("Steel", 25),
# ("Wood", 75)
# ]

# result = {}

# for item in data:
#     if item[0] in result:
#         result[item[0]] += item[1]
#     else:
#         result[item[0]] = item[1]

# print(result)


#Exe.3 Create empty dictionary:
# add elements to dictionary
# Wall -> 125
# Door -> 32
# Window -> 48
# 1. Give the number of the doors
# 2. Increase number of walls by 10
# 3. Print whole dictionary

# elements = {}

# elements["Wall"] = 125
# elements["Door"] = 32
# elements["Window"] = 48

# print(elements["Door"])

# elements["Wall"] += 10

# print(elements)

# create dictionary with list from given elements list

# elements = [
#     ("Level 1", "Wall A"),
#     ("Level 1", "Wall B"),
#     ("Level 2", "Wall C"),
#     ("Level 1", "Door A"),
# ]

# levels = {}

# for lvl in elements:
#     if lvl[0] in levels:
#         levels[lvl[0]].append(lvl[1])
#     else:
#         levels[lvl[0]] = [] 
#         levels[lvl[0]].append(lvl[1])
# print(levels)


# # found material with the biggest sum

# materials = {
#     "Concrete": 300,
#     "Steel": 75,
#     "Wood": 75,
#     "Asphalt": 450
# }

# max_value = 0
# max_material = ""

# for x in materials:
#     if materials[x] > max_value:
#         max_value = materials[x]
#         max_material = x

# print(f"The bigest ammount is {max_value} and the material is {max_material}")

# Sum all materials

# materials = {
#     "Concrete": 300,
#     "Steel": 75,
#     "Wood": 75,
#     "Asphalt": 450
# }

# q = 0

# for m in materials:
#     q += materials[m]  

# print(q)

# Give materials that quantity is grater then 100

materials = {
    "Concrete": 300,
    "Steel": 75,
    "Wood": 75,
    "Asphalt": 450
}



for m in materials:
    if materials[m] > 100:
        print(m)

