def latest(scores):
    return scores[len(scores)- 1]


def personal_best(scores):
    best = scores[0]
    for k in scores:
        if k > best:
            best = k

    return best


def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    return scores[0:3]
