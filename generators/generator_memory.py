# pip3 install memory_profiler
import memory_profiler as mem_profile
import random
import time

names = ['Rajesh', 'Sunit', 'Ruchi', 'Priyanka', 'Lathesh', 'Rahul']
stacks = ['Spark', 'Hadoop', 'Flink', 'AWS', 'GCP', 'Azure']
print('Memory (Before): {} MB'.format(mem_profile.memory_usage()[0]))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'stacks': random.choice(stacks)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'stacks': random.choice(stacks)
        }
        yield person


t1 = time.process_time()

# people = people_list(10000)
people = people_generator(10000)
# people = list(people_generator(1000000))

for person in people:
    print(person)

t2 = time.process_time()

print('Memory (After): {} MB'.format(mem_profile.memory_usage()[0]))
print('Took {} seconds'.format(t2 - t1))