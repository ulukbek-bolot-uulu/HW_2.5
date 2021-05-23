example = {
    'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15 / 2, False],
    'fire': ['hot', 46, ['cha', 'ching'], 81.13],
    'earth': ['solid', 100, (13, 31, 1), 90.01, {'b': 'c'}]
}
elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']


def func(dct, lst):
    for i in lst:
        try:
            sum = 0
            for j in dct[i]:
                try:
                    sum += j
                except TypeError:
                    continue
            print(f"{i}------------{sum}")
        except KeyError:
            print(f"Key {i}--------------does not exist")


func(example, elements)
