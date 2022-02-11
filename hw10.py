def collatz(n):
    '''
    Purpose:
        To take a parameters n (a positive integer).  If n is even, divide it by
        2 to get n / 2.  If n is odd, multiply it by 3 and add 1 to obtain 3n +
        1. The process will be repeated until the value "1" is reached. The
        returned value will be the sum of the number in the collatz sequence
        from n to 1.
    Parameter(s):
        n: A positive integer
    Return Value:
        The sum of the number in the collatz sequence from n to 1.
    '''
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return int(n + (collatz(n/2)))
        else:
            return int(n + (collatz(3*n+1)))

def is_pos_reversible(alist):
    '''
    Purpose:
        To take a  list of integers and tests whether the positive integers in
        that list could be read the same forward as backwards. The positions of
        0s and negative values will not matter.
    Parameter(s):
        alist: A list of integers.
    Return Value:
        The boolean value True if the list could be read the same forward as
        backwards when ignoring the 0s and the negative values and the Boolean
        value false if it cant.
    '''
    x = is_pos_reversible_helper(alist)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False

def is_pos_reversible_helper(alist):
    '''
    Purpose:
        To take the list passed to the function called is_pos_reversible and
        return the same lsit but removing the 0s and the negative values in
        order to check if it can be read backwards or not in the actual function.
    Parameter(s):
        alist: A list of integers
    Return Value:
        A list containing the same values as the list passed but removing the 0s
         and the negative values in order to check if it can be read backwards
         or not in the actual function.
    '''
    if alist == []:
        return []
    if alist[0] <= 0:
        return is_pos_reversible_helper(alist[1:])
    else:
        return [alist[0]] + is_pos_reversible_helper(alist[1:])

def all_subsets(alist):
    '''
    Purpose:
        To take a list of itens as a parameter and return a list containing all
        possible subsets
    Parameter(s):
        alist: A list of items
    Return Value:
        A list of possible subsets from "alist"
    '''
    lst = []
    if alist == []:
        lst.append([])
    else:
        x = all_subsets(alist[1:])
        for i in x:
            lst.append(i)
            lst.append(i + [alist[0]])
    return lst
