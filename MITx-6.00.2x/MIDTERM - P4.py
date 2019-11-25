def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    if s == 0:
        return [0,0,0,0]
    else:
        l = [0,0,0,0]
        val = 0
        for a, i in enumerate([25,10,5,1]):
            x =0
            flag = True
            while flag:
                x+=1
                if val + x*i <= s:
                    l[a] = x
                else:
                    val += (x-1)*i
                    flag = False
            if val == s:
                break
            else:
                pass
        return l