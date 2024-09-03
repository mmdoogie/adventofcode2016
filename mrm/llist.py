class _lle:
    def __init__(self, val, el_prev = None, el_next = None):
        self.val = val
        self._prev = el_prev
        self._next = el_next

    def right(self):
        return self._next

    def left(self):
        return self._prev

    def far_right(self, amt):
        el = self
        for _ in range(amt):
            el = el.right()
        return el

    def far_left(self, amt):
        el = self
        for _ in range(amt):
            el = el.left()
        return el

    def insert_right(self, val):
        new_el = _lle(val, self)
        new_el._next = self._next
        self._next._prev = new_el
        self._next = new_el
        return new_el

    def insert_left(self, val):
        new_el = _lle(val, self._prev, self)
        self._prev._next = new_el
        self._prev = new_el
        return new_el

class llist:
    def __init__(self, items, circular = False):
        prev = None
        self._circular = False
        for i in items:
            el = _lle(i, prev)
            if prev is None:
                self._head = el
            else:
                el._prev._next = el
            prev = el
        if circular:
            self._circular = True
            self._head._prev = el
            el._next = self._head

    def head(self):
        return self._head

    def __iter__(self):
        return self._itgen()

    def _itgen(self):
        el = self._head
        yield el
        while True:
            el = el.right()
            if el is None:
                break
            yield el

    def find(self, val):
        pass_two = False
        for x in self:
            if x is self._head and pass_two:
                return None
            if x is self._head:
                pass_two = True
            if x.val == val:
                return x
        return None
