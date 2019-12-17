# If the Elves all proceed with their own plans, none of them will have enough fabric. 
# How many square inches of fabric are within two or more claims?

# Huiswerk: What is the ID of the only claim that doesn't overlap?

grid = []

for y in range(1000):
    row = []
    for x in range(1000):
        row.append(0)
    grid.append(row)


claimfile = open('input.txt', 'r')
# claimfile = open('test.txt', 'r')
# #2 @ 413,723: 16x28
# #ID @ xoffset, yoffset: w x h
for claim in claimfile:
    claim_id, _ , offset, wh = claim.split()
    claim_id = int(claim_id[1:])
    offset = offset[:-1].split(',')
    offsetx = offset[0]
    offsety = offset[1]
    offsetx, offsety = int(offsetx), int(offsety)
    w, h = wh.split('x')
    w, h = int(w), int(h)

    # offsetpoint = (offsety, offsetx)
    # grid[offsety][offsetx] += 1
    for y in range(offsety, offsety + h):
        for x in range(offsetx, offsetx + w):
            if grid[y][x] == 0:
                grid[y][x] = claim_id
            else:
                grid[y][x] = 'X'
        

result = 0
for row in grid:
    for square in row:
        if square == 'X':
            result += 1
    
print(result)
claimfile.close()