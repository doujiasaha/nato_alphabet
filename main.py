rangelist = [x*2 for x in range(1,5)]

print(rangelist)

names = ["Caroline", "Thomas", "Peter", "Alex", "Brad", "Hao"]

new_names = [x.upper() for x in names if len(x) > 5]

print(new_names)