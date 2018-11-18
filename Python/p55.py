#Problem 55 - Lychrel numbers. Iteratively add a number to its reverse until you produce a palindrome
#If it takes more than 50 iterations and no palindrome is achieved, it is a Lychrel number

#Reverse an integer's digits
def reverse_int(n):
    d = 0
    while n > 0:
        d = (d * 10) + (n % 10)
        n /= 10
    return d

def is_palindrome(n):
    return n == reverse_int(n)

#Count the number of lychrel numbers under 10000
def problem_55():
    lychrels = 0
    for n in xrange(1,10000):
        x = n
        isLychrel = True
        #it is a lychrel number if it doesn't produce a palindrome in under 50 iterations
        for its in xrange(49): 
            x += reverse_int(x)
            if is_palindrome(x):
                isLychrel = False
                break
        if isLychrel: lychrels += 1

    print lychrels

if __name__ == '__main__':
    problem_55()
