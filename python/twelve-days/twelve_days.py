def recite(start_verse, end_verse):
    days = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree.",
    ]

    nums = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    if (start_verse == 1):
        days[len(days)-1] = days[len(days)-1][4:]
        # print(days[0])

    # print(nums[start_verse - 1])

    ret = ["On the " + str(nums[start_verse - 1]) + " day of Christmas my true love gave to me: "]

    for j in range(len(days) - start_verse, len(days)):
        # ret.append(days[j])
        ret[0] += days[j]

    print(ret)

    if (start_verse == end_verse):
        return ret

    else:
        return ret + recite(start_verse + 1, end_verse)


recite(2, 2)
