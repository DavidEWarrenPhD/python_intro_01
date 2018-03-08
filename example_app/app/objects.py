import collections

INF = float('inf')

triad_attrs = 'item1 item2 item3'.split()
Triad = collections.namedtuple('Triad', triad_attrs)
Set = collections.namedtuple('Set', 'name num triadsABC'.split())
Group = collections.namedtuple('Group', 'name num sets')
