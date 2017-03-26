#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org

def select_a_list(n):
    if n < 2047:
        return [2,]
    elif n < 1373653:
        return [2, 3]
    elif n < 9080191:
        return [31, 73]
    elif n < 25326001:
        return [2, 3, 5]
    elif n < 3215031751:
        return [2, 3, 7]
    elif n < 4759123141:
        return [2, 7, 61]
    elif n < 1122004669633:
        return [2, 13, 23, 1662803]
    elif n < 2152302898747:
        return [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        return [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        return [2, 3, 5, 7, 11, 13, 17]
    elif n < 3825123056546413051:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n < 318665857834031151167461:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3317044064679887385961981:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    else:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def calc_r_d(n):
    n -= 1
    r = 0
    d = n
    while 1:
        if n % 2 != 0:
            break
        r += 1
        d = n / 2
        n /= 2
    return r, d

def miller_rabin_primality_test(n):
    """use miller rabin primality test to judge n whether prime"""
    if n < 0:
        n = -n
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    r, d = calc_r_d(n)
    a_list = select_a_list(n)
    for k in xrange(len(a_list)):
        a = random.sample(a_list, 1)[0] # Select one non-repeating random number from the list at a time
        a_list.remove(a)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for t in xrange(r - 1):
            x = pow(x, 2, n)
            if x ==1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True