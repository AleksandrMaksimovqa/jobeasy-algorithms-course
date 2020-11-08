names = [
    'Aliza Hulme',
    'Isaiah Mcgill',
    'Keiran Partridge',
    'Michele Wilcox',
    'Jordon Rocha',
    'Shakir Calhoun',
    'Lexi Bob',
    'Nimrah Regan',
    'Scarlet Roberts',
    'Emily-Jane Mejia'
]
jobs = [
    'Speech therapist',
    'Animal breeder',
    'Miner',
    'IT consultant',
    'Butler',
    'Radio presenter',
    'Architect',
    'Police officer',
]


def create_dictionary(keys, values):
    while len(values) < len(keys):
        values.append(None)
    return dict(zip(keys, values))


print(create_dictionary(names, jobs))