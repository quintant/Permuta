import abc
import numbers

from permuta.descriptors import Descriptor
from permuta.descriptors import Basis
from permuta.descriptors import Predicate
from permuta._perm_set import PermSetBase
from permuta._perm_set.finite import PermSetStatic
from permuta._perm_set.unbounded.all import PermSetAll
from permuta._perm_set.unbounded.described import PermSetDescribed


class PermSetMetaclass(type):
    def __instancecheck__(self, instance):
        return isinstance(instance, PermSetBase)
    def __subclasscheck__(self, subclass):
        return issubclass(subclass, PermSetBase)

class PermSet(object, metaclass=PermSetMetaclass):
    def __new__(cls, descriptor=None):
        if descriptor is None:
            return PermSetAll()
        elif isinstance(descriptor, numbers.Integral):
            # Descriptor is actually just a number
            return PermSetAll().of_length(descriptor)
        elif isinstance(descriptor, Descriptor):
            cls._dispatch_described(descriptor)
        else:
            # Descriptor might just be a set of perms
            return PermSetStatic(descriptor)

    @classmethod
    def _dispatch_described(cls, descriptor):
        described_class = cls._find_described_class(descriptor, PermSetDescribed)
        if described_class is None:
            raise RuntimeError("PermSet for descriptor {} not found".format(repr(descriptor)))  # TODO: Something else?
        else:
            return described_class(descriptor)

    @classmethod
    def _find_described_class(cls, descriptor, current_class):
        # TODO: Use metaclasses to track subclasses
        print(current_class)
        print("\t", current_class.descriptor)
        print("\t", descriptor)
        print("\t", current_class.descriptor == descriptor)
        if current_class.descriptor == descriptor:
            return current_class
        else:
            for subclass in current_class.__subclasses__():
                described_class = cls._find_described_class(descriptor, subclass)
                if described_class is not None:
                    return described_class
        return None

    @classmethod
    def avoiding(cls, basis):
        return cls(Basis(basis))

    @classmethod
    def filtered(cls, predicate):
        return cls(Predicate(predicate))
