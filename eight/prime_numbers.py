# def prime_checker(number):
#     if n > 1:
#         if n % n == 0:
#             if n % 1 ==0:
#
#                 print( "prime")
#             else:
#                 print("not prime")
#
def prime_checker(number):
    if number <= 1:
        print("Not prime or non-prime (must be greater than 1)")
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is prime.")
        else:
            print(f"{number} is non-prime.")



n = int(input()) # Check this number
prime_checker(number = n)