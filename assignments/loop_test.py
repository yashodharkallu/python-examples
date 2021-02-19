partitionNum = 104
batch_size = 4
pool_size = int(partitionNum / batch_size)
odds = partitionNum % batch_size
part_num = 0
for n in range (1, pool_size+1):
    for x in range (1, batch_size+1):
        part_num = (n-1) * batch_size + x
        print('>>', part_num)
for y in range(part_num+1, part_num+odds+1):
    print('<<', y)
