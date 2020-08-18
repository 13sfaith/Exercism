def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise Exception('Strands are of varying length')

    dist = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            dist += 1

    return dist
