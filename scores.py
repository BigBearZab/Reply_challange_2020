from score_calc import score_calc
from parse import parse

from itertools import combinations

dev_meta, manager_meta, all_pairs, locations = parse("input/a_solar.txt")


dev_meta_labelled = {}
for i in range(len(dev_meta)):
    dev_meta_labelled[f"d{i}"] = dev_meta[i]

manager_meta_labelled = {}
for i in range(len(manager_meta)):
    manager_meta_labelled[f"m{i}"] = manager_meta[i]

total = dict(dev_meta_labelled, **manager_meta_labelled)

# calculate all combinations
scores = {}
for pair in combinations(total.keys(), 2):
    scores[pair[0] + "-" + pair[1]] = score_calc(total[pair[0]], total[pair[1]])

# calculate manager combinations
scores = {}
for pair in combinations(manager_meta_labelled.keys(), 2):
    scores[pair[0] + "-" + pair[1]] = score_calc(total[pair[0]], total[pair[1]])

# calculate developer combinations
scores = {}
for pair in combinations(dev_meta_labelled.keys(), 2):
    scores[pair[0] + "-" + pair[1]] = score_calc(total[pair[0]], total[pair[1]])
