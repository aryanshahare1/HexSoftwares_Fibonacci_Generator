
def fibonacci_generator(limit):
   
    a, b = 0, 1
    
    # Continue generating Fibonacci numbers until the current number exceeds the limit
    while a < limit:
        yield a  
        a, b = b, a + b 

# Example usage
limit = int(input("Enter the limit for Fibonacci series: "))  

# Loop through the generator and print each Fibonacci number
for number in fibonacci_generator(limit):
    print(number)  
