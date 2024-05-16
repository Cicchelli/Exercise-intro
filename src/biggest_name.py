from typing import List


def find_biggest_name(names: List[str]) -> str:
    biggesst_name = names
    for name in names:
        if len(name) > len(biggesst_name):
            biggesst_name = name
    return biggesst_name
