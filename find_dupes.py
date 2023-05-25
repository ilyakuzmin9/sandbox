# a = [1,2,3,2,1,5,6,5,5,5]
#
# import collections
# print([item for item, count in collections.Counter(a).items() if count > 1])
#
# seen = set()
# uniq = []
# for x in a:
#     if x not in seen:
#         uniq.append(x)
#         seen.add(x)
#
# seen = set()
# uniq = [x for x in a if x not in seen and not seen.add(x)]
#
# seen = set()
# dupes = []
#
# for x in a:
#     if x in seen:
#         dupes.append(x)
#     else:
#         seen.add(x)
#
# seen = set()
# dupes = [x for x in a if x in seen or seen.add(x)]
#
# a = [[1], [2], [3], [1], [5], [3]]
#
# no_dupes = [x for n, x in enumerate(a) if x not in a[:n]]
# print no_dupes # [[1], [2], [3], [5]]
#
# dupes = [x for n, x in enumerate(a) if x in a[:n]]
# print dupes # [[1], [3]]

# a = [1,2,3,2,1,5,6,5,5,5]
a = ['a', 'b', 'b', 'c', 'a', 'c', 'c']

set_elem = set()
duples = []

for elem in a:
    if elem in set_elem:
        duples.append(elem)
    else:
        set_elem.add(elem)
print(set_elem)
print(duples)
