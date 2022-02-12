def BigUnion(iter):
    """
    :param iter: Iterable collection of sets
    :return: The union of all of the sets
    """
    union = set()
    for s in iter:
        union.update(s)
    return union
def BigIntersection(iter):
    """
    :param iter: Iterable collection of sets
    :return: The intersection of all of the sets
    """
    intersection = None
    for s in iter:
        if intersection is None:
            intersection = s.copy()
        else:
            intersection = intersection.intersection(s)
        if len(intersection) == 0:
            return intersection
    return intersection