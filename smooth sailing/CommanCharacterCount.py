def commonCharacterCount(s1, s2):
    s3 = list(s1)
    s4 = list(s2)

    c = []
    for x in s3:
        if x in s4:
            s4.remove(x)
            c.append(x)
    return len(c)
