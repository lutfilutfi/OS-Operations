with open('nounlist.txt') as f:
    lines = [line.rstrip() for line in f]
for f in lines:
    # print(type(f))
    print(f)