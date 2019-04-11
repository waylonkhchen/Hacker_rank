def repeatedString(s, n):

    s_len = len(s)
    q = n // s_len
    r = n % s_len
    m =s.count('a')
    rr = s[:r].count(a)
    return = q*m+rr


