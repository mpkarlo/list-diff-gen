from uuid import uuid4
from random import sample, randint

test_set_a = {uuid4() for _ in range(1_000_000)}
test_set_b = {uuid4() for _ in range(1_000_000)}

test_set_a.update(sample(tuple(test_set_b), randint(1_000, 100_000)))
test_set_b.update(sample(tuple(test_set_a), randint(1_000, 100_000)))

with open('set_a.txt', 'w') as file_obj:
    file_obj.write('\n'.join([str(i) for i in test_set_a]))

with open('set_b.txt', 'w') as file_obj:
    file_obj.write('\n'.join([str(i) for i in test_set_b]))
