from .Avoiding import *
from permuta import Perm
from .CatalanAvoiding import CatalanAvoidingClass


class Avoiding201(AvoidingGeneric, CatalanAvoidingClass):
    descriptor = Basis(Perm((2, 0, 1)))

    def _ensure_level(self, level_number):
        while len(self.cache) <= level_number:
            new_level = set()
            frame = Perm((0,2,1))
            for lower_length in range(level_number):
                upper_length = level_number - lower_length - 1
                for lower_perm in self.cache[lower_length]:
                    for upper_perm in self.cache[upper_length]:
                        new_perm = frame.inflate([lower_perm, upper_perm, None])
                        new_level.append(new_perm)
            self.cache.append(new_level)
