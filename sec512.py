import random

def hash(s):
    random.seed(s)
    return "".join(random.choices("0123456789abcdef",k=128))

if __name__=="__main__":
    s="This is a test string to hash"
    print(hash(s))
