import abc


class PermSetBase(metaclass=abc.ABCMeta):
    def contains(self, perm):
        return perm in self

    @abc.abstractmethod
    def up_to(self, perm):
        pass

    @abc.abstractmethod
    def __contains__(self, perm):
        pass

    @abc.abstractmethod
    def __getitem__(self, key):
        pass

    def __repr__(self):
        return "<A set of some perms>"
