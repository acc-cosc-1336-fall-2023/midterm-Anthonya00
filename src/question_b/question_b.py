#write functions here, don't add input('') statements here!

def is_prime (num):
    if num == 1 :
        return False
    elif num > 1 :
        for x in range (2, num):
            if num % x == 0:
                return False
            else:
                return True
    else:
        return False
    


    