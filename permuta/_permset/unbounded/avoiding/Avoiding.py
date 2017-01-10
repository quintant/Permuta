from .. import PermSetUnbounded
from ...descriptors import Basis


class Avoiding(PermSetUnbounded):
    descriptor = Basis
    def contains(self, perm):
        raise NotImplementedError
    def up_to(self, perm):
        raise NotImplementedError
    def __getitem__(self, perm):
        raise NotImplementedError
