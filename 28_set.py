# set

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# union two sets
dinner_table = utensils.union(dishes)

# difference
print(utensils.difference(dishes))

# intersection
print(utensils.intersection(dishes))

utensils.add("napkin")
utensils.remove("spoon")
utensils.clear()
utensils.update(dishes)


for x in utensils:
    print(x)
