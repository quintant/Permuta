from permuta import Perm
from permuta.permutils.groups import dihedral_group


def test_dihedral_group():
    first_11 = {
        0: set(),
        1: set(),
        2: set(),
        3: {
            Perm((1, 0, 2)),
            Perm((2, 0, 1)),
            Perm((0, 1, 2)),
            Perm((2, 1, 0)),
            Perm((1, 2, 0)),
            Perm((0, 2, 1)),
        },
        4: {
            Perm((3, 2, 1, 0)),
            Perm((0, 3, 2, 1)),
            Perm((3, 0, 1, 2)),
            Perm((2, 1, 0, 3)),
            Perm((2, 3, 0, 1)),
            Perm((1, 2, 3, 0)),
            Perm((1, 0, 3, 2)),
            Perm((0, 1, 2, 3)),
        },
        5: {
            Perm((0, 1, 2, 3, 4)),
            Perm((3, 2, 1, 0, 4)),
            Perm((4, 0, 1, 2, 3)),
            Perm((0, 4, 3, 2, 1)),
            Perm((4, 3, 2, 1, 0)),
            Perm((1, 0, 4, 3, 2)),
            Perm((3, 4, 0, 1, 2)),
            Perm((2, 3, 4, 0, 1)),
            Perm((1, 2, 3, 4, 0)),
            Perm((2, 1, 0, 4, 3)),
        },
        6: {
            Perm((3, 4, 5, 0, 1, 2)),
            Perm((4, 3, 2, 1, 0, 5)),
            Perm((2, 1, 0, 5, 4, 3)),
            Perm((0, 1, 2, 3, 4, 5)),
            Perm((2, 3, 4, 5, 0, 1)),
            Perm((3, 2, 1, 0, 5, 4)),
            Perm((1, 0, 5, 4, 3, 2)),
            Perm((4, 5, 0, 1, 2, 3)),
            Perm((5, 4, 3, 2, 1, 0)),
            Perm((5, 0, 1, 2, 3, 4)),
            Perm((0, 5, 4, 3, 2, 1)),
            Perm((1, 2, 3, 4, 5, 0)),
        },
        7: {
            Perm((2, 3, 4, 5, 6, 0, 1)),
            Perm((5, 6, 0, 1, 2, 3, 4)),
            Perm((0, 1, 2, 3, 4, 5, 6)),
            Perm((4, 3, 2, 1, 0, 6, 5)),
            Perm((1, 0, 6, 5, 4, 3, 2)),
            Perm((0, 6, 5, 4, 3, 2, 1)),
            Perm((3, 2, 1, 0, 6, 5, 4)),
            Perm((6, 5, 4, 3, 2, 1, 0)),
            Perm((4, 5, 6, 0, 1, 2, 3)),
            Perm((2, 1, 0, 6, 5, 4, 3)),
            Perm((1, 2, 3, 4, 5, 6, 0)),
            Perm((6, 0, 1, 2, 3, 4, 5)),
            Perm((3, 4, 5, 6, 0, 1, 2)),
            Perm((5, 4, 3, 2, 1, 0, 6)),
        },
        8: {
            Perm((1, 0, 7, 6, 5, 4, 3, 2)),
            Perm((7, 0, 1, 2, 3, 4, 5, 6)),
            Perm((4, 5, 6, 7, 0, 1, 2, 3)),
            Perm((7, 6, 5, 4, 3, 2, 1, 0)),
            Perm((2, 1, 0, 7, 6, 5, 4, 3)),
            Perm((6, 5, 4, 3, 2, 1, 0, 7)),
            Perm((1, 2, 3, 4, 5, 6, 7, 0)),
            Perm((0, 7, 6, 5, 4, 3, 2, 1)),
            Perm((2, 3, 4, 5, 6, 7, 0, 1)),
            Perm((0, 1, 2, 3, 4, 5, 6, 7)),
            Perm((3, 2, 1, 0, 7, 6, 5, 4)),
            Perm((6, 7, 0, 1, 2, 3, 4, 5)),
            Perm((5, 6, 7, 0, 1, 2, 3, 4)),
            Perm((5, 4, 3, 2, 1, 0, 7, 6)),
            Perm((3, 4, 5, 6, 7, 0, 1, 2)),
            Perm((4, 3, 2, 1, 0, 7, 6, 5)),
        },
        9: {
            Perm((3, 4, 5, 6, 7, 8, 0, 1, 2)),
            Perm((7, 8, 0, 1, 2, 3, 4, 5, 6)),
            Perm((4, 5, 6, 7, 8, 0, 1, 2, 3)),
            Perm((0, 1, 2, 3, 4, 5, 6, 7, 8)),
            Perm((5, 4, 3, 2, 1, 0, 8, 7, 6)),
            Perm((2, 3, 4, 5, 6, 7, 8, 0, 1)),
            Perm((8, 7, 6, 5, 4, 3, 2, 1, 0)),
            Perm((0, 8, 7, 6, 5, 4, 3, 2, 1)),
            Perm((2, 1, 0, 8, 7, 6, 5, 4, 3)),
            Perm((3, 2, 1, 0, 8, 7, 6, 5, 4)),
            Perm((4, 3, 2, 1, 0, 8, 7, 6, 5)),
            Perm((5, 6, 7, 8, 0, 1, 2, 3, 4)),
            Perm((6, 5, 4, 3, 2, 1, 0, 8, 7)),
            Perm((7, 6, 5, 4, 3, 2, 1, 0, 8)),
            Perm((6, 7, 8, 0, 1, 2, 3, 4, 5)),
            Perm((8, 0, 1, 2, 3, 4, 5, 6, 7)),
            Perm((1, 0, 8, 7, 6, 5, 4, 3, 2)),
            Perm((1, 2, 3, 4, 5, 6, 7, 8, 0)),
        },
        10: {
            Perm((3, 2, 1, 0, 9, 8, 7, 6, 5, 4)),
            Perm((6, 5, 4, 3, 2, 1, 0, 9, 8, 7)),
            Perm((4, 5, 6, 7, 8, 9, 0, 1, 2, 3)),
            Perm((6, 7, 8, 9, 0, 1, 2, 3, 4, 5)),
            Perm((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
            Perm((5, 6, 7, 8, 9, 0, 1, 2, 3, 4)),
            Perm((3, 4, 5, 6, 7, 8, 9, 0, 1, 2)),
            Perm((5, 4, 3, 2, 1, 0, 9, 8, 7, 6)),
            Perm((7, 8, 9, 0, 1, 2, 3, 4, 5, 6)),
            Perm((9, 8, 7, 6, 5, 4, 3, 2, 1, 0)),
            Perm((9, 0, 1, 2, 3, 4, 5, 6, 7, 8)),
            Perm((2, 3, 4, 5, 6, 7, 8, 9, 0, 1)),
            Perm((0, 9, 8, 7, 6, 5, 4, 3, 2, 1)),
            Perm((2, 1, 0, 9, 8, 7, 6, 5, 4, 3)),
            Perm((8, 7, 6, 5, 4, 3, 2, 1, 0, 9)),
            Perm((1, 0, 9, 8, 7, 6, 5, 4, 3, 2)),
            Perm((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)),
            Perm((8, 9, 0, 1, 2, 3, 4, 5, 6, 7)),
            Perm((4, 3, 2, 1, 0, 9, 8, 7, 6, 5)),
            Perm((7, 6, 5, 4, 3, 2, 1, 0, 9, 8)),
        },
    }
    for i in range(11):
        assert set(dihedral_group(i)) == first_11[i]
