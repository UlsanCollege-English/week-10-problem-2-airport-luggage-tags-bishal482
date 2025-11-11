"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# ---- Step 4: create unique markers ----
EMPTY = object()
DELETED = object()


def _hash_basic(key):
    """Simple stable hash (sum of ord chars)."""
    return sum(ord(c) for c in key)


def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    return [EMPTY] * m


def _find_slot_for_insert(t, key):
    """
    Return index to insert/overwrite (may return first DELETED).
    Return None if table is full.
    """
    m = len(t)
    start = _hash_basic(key) % m
    first_deleted = None

    i = start
    while True:
        slot = t[i]

        if slot is not EMPTY and slot is not DELETED and slot[0] == key:
            return i

        if slot is DELETED and first_deleted is None:
            first_deleted = i

        if slot is EMPTY:
            return first_deleted if first_deleted is not None else i

        i = (i + 1) % m
        if i == start:
            return None


def _find_slot_for_search(t, key):
    """
    Return index where key is found; else None.
    DELETED does not stop searching.
    """
    m = len(t)
    start = _hash_basic(key) % m

    i = start
    while True:
        slot = t[i]

        if slot is EMPTY:
            return None

        if slot is not DELETED and slot[0] == key:
            return i

        i = (i + 1) % m
        if i == start:
            return None


def put_open(t, key, value):
    """Insert or overwrite. Return True if successful else False."""
    idx = _find_slot_for_insert(t, key)
    if idx is None:
        return False
    t[idx] = (key, value)
    return True


def get_open(t, key):
    """Return value for key or None if missing."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return None
    return t[idx][1]


def delete_open(t, key):
    """Delete key. Return True if removed else False."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return False
    t[idx] = DELETED
    return True


if __name__ == "__main__":
    pass
