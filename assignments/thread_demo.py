tot_cnt = 110

batch_size = 50
pool_size = int(tot_cnt / batch_size)
odds = tot_cnt % batch_size
part_num = 0
for x in range(1, pool_size + 1):
    for y in range(1, batch_size + 1):
        part_num = (x-1) * batch_size + y
        print(part_num)

print('>>>>.', part_num)
print('>>>>.', odds)
for z in range((part_num + 1), (part_num + odds + 1)):
    print(z)

