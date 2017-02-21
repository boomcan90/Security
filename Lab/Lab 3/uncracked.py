wf = open("uncracked.txt", 'w')

with open("hashes.txt", 'r') as f:
    for line in f:
        a = line.split(" ")
        if len(a) < 2:
            wf.write(a[0])

