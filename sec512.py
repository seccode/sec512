import random

def get_equally_spaced_chars(s):
    n=len(s)
    if n==0:
        return ""  # Handle empty string case
    # Use integer division to calculate the step size
    step=max(n/1000,1)
    # Use list comprehension with round to select characters
    result=[s[round(i*step)%n] for i in range(1000)]
    return "".join(result)

def hash(s):
    c=get_equally_spaced_chars(s)
    random.seed(c)
    return "".join(random.choices("0123456789abcdef",k=64))

if __name__=="__main__":
    s="This is a test string to hash"
    print(hash(s))
