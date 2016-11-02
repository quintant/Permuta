import collections
from .permutation import Permutation
from .permutations import Permutations
from .math import catalan

class PermutationPatternClass(object):
    def __init__(self, n, pattern):
        self.n = n
        self.patt = pattern
        self.pattstr = "".join(map(str,self.patt))

    def __str__(self):
        return "Permutations of length %d avoiding %s" % (self.n, self.pattstr)

    def __repr__(self):
        return "PermutationPatternClass(%d,%s)" % (self.n, self.patt)


class AvoidanceClass(object):
    def __new__(cls, n, avoiding, **kwargs):
        if isinstance(avoiding, Permutation):
            p = avoiding
            if len(p) == 2:
                if p[0] == 1:
                    return PermutationsAvoiding12(n)
                else:
                    return PermutationsAvoiding21(n)
            if len(p) == 3:
                if p[0] == 1:
                    if p[1] == 2:
                        return PermutationsAvoiding123(n)
                    else:
                        return PermutationsAvoiding132(n)
                elif p[0] == 2:
                    if p[1] == 1:
                        return PermutationsAvoiding213(n)
                    else:
                        return PermutationsAvoiding231(n)
                else:
                    if p[1] == 1:
                        return PermutationsAvoiding312(n)
                    else:
                        return PermutationsAvoiding321(n)
            else:
                return PermutationsAvoidingGeneric(n,(avoiding,))
        elif (isinstance(avoiding, collections.Iterable) and
                all(isinstance(x, Permutation) for x in avoiding)):
            return PermutationsAvoidingGeneric(n,avoiding, **kwargs)
        else:
            raise RuntimeError("Cannot avoid " + repr(avoiding))


class PermutationsAvoidingGeneric(PermutationPatternClass):
    def __init__(self, n, patterns, upto=False):
        super(PermutationsAvoidingGeneric, self).__init__(n,tuple(patterns))
        self.n = n
        self.pattstr = "("+",".join(["".join(map(str,x)) for x in patterns])+")"
        self.upto = upto

    def __iter__(self):
        # TODO: make this lazy, i.e. use yield inside the generation (if possible)
        cur = set([ Permutation([]) ])
        if self.upto or self.n == 0:
            yield Permutation([])

        for l in range(1,self.n+1):
            nxt = set()
            for prev in cur:
                for i in range(len(prev)+1):
                    maybe = Permutation(prev[:i] + [len(prev)+1] + prev[i:])
                    ok = True
                    for p in self.patt:
                        if maybe.contains(p): # TODO: only check for occurrences that contain the new len(prev)+1 element
                            ok = False
                            break
                    if ok:
                        nxt.add(maybe)
            cur = nxt
            if self.upto or l == self.n:
                for p in cur:
                    yield p

class PermutationsAvoiding12(PermutationPatternClass):
    """Class for iterating through Permutations avoiding 12 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding12, self).__init__(n,[1,2])

    def __iter__(self):
        yield Permutation(range(self.n,0,-1))

    def __len__(self):
        return 1

class PermutationsAvoiding21(PermutationPatternClass):
    """Class for iterating through Permutations avoiding 21 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding21, self).__init__(n,[2,1])

    def __iter__(self):
        yield Permutation(range(1,self.n+1))

    def __len__(self):
        return 1

class CatalanAvoidingClass(PermutationPatternClass):
    def __init__(self, n, pattern):
        super(CatalanAvoidingClass, self).__init__(n,pattern)

    def __len__(self):
        return catalan(self.n)

class PermutationsAvoiding123(CatalanAvoidingClass):
    def __init__(self,n):
        super(PermutationsAvoiding123, self).__init__(n,[1,2,3])

    def __iter__(self):

        if self.n == 0:
            yield Permutation([])
            return
        elif self.n <3:
            for p in Permutations(self.n):
                yield p
            return
        elif self.n ==3:
            for p in Permutations(self.n):
                if p!= Permutation([1,2,3]):
                    yield p
            return

        for p in PermutationsAvoiding132(self.n):
            # use simion-schmidt bijection
            m = self.n + 1
            minima = []
            minima_positions = []
            for index, value in enumerate(p):
                if value < m:
                    minima_positions.append(index)
                    minima.append(value)
                    m = value
            new_perm = []
            non_minima = [x for x in range(self.n, 0, -1) if x not in minima]
            a = 0
            b = 0
            for i in range(self.n):
                if i in minima_positions:
                    new_perm.append( minima[a] )
                    a += 1
                else:
                    new_perm.append( non_minima[b] )
                    b += 1
            yield Permutation(new_perm)

class PermutationsAvoiding132(CatalanAvoidingClass):
    """Class for iterating through Permutations avoiding 132 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding132, self).__init__(n,[1,3,2])

    def __iter__(self):

        if self.n == 0:
            yield Permutation([])
            return
        elif self.n < 3:
            for p in Permutations(self.n):
                yield p
            return
        elif self.n == 3:
            for p in Permutations(self.n):
                if p != Permutation([1,3,2]):
                    yield p
            return

        for left_length in range(0,self.n):
            right_length = self.n - 1 - left_length
            for left in PermutationsAvoiding132(left_length):
                for right in PermutationsAvoiding132(right_length):

                    yield Permutation([x + right_length for x in left]
                                         + [self.n]
                                         + list(right))
        return


class PermutationsAvoiding213(CatalanAvoidingClass):
    """Class for iterating through Permutations avoiding 213 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding213, self).__init__(n,[2,1,3])

    def __iter__(self):
        for p in PermutationsAvoiding132(self.n):
            yield p.reverse().complement()


class PermutationsAvoiding231(CatalanAvoidingClass):
    """Class for iterating through Permutations avoiding 231 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding231, self).__init__(n,[2,3,1])

    def __iter__(self):
        for p in PermutationsAvoiding132(self.n):
            yield p.reverse()


class PermutationsAvoiding312(CatalanAvoidingClass):
    """Class for iterating through Permutations avoiding 312 of length n"""
    def __init__(self, n):
        super(PermutationsAvoiding312, self).__init__(n,[3,1,2])

    def __iter__(self):
        for p in PermutationsAvoiding132(self.n):
            yield p.complement()

class PermutationsAvoiding321(CatalanAvoidingClass):
    def __init__(self,n):
        super(PermutationsAvoiding321, self).__init__(n,[3,2,1])

    def __iter__(self):
        for p in PermutationsAvoiding123(self.n):
            yield p.reverse()
