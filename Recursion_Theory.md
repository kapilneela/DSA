Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

Every recursive function needs two parts:
- Base case → stops the recursion.
- Recursive case → function calls itself with a smaller/simpler input.

Every recursion gets stored in stack space and as for python default recursion stops at 937 count

eg :
  def countdown(n):
    if n == 0:          # Base case
        return 
    print(n)
    countdown(n - 1)    # Recursive case
  countdown(5) 

Head Recursion

In head recursion, the recursive call happens before the function performs its remaining work.
eg:
  def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
  print_numbers(5)

Tail Recursion

Tail recursion is a type of recursion where the recursive call is the very last operation performed by the function.
eg:
  def factorial(n, result=1):
    if n == 0:
        return result
    return factorial(n - 1, result * n)
  print(factorial(5))
