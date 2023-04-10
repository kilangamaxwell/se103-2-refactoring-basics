def is_sum_of_two_primes(number):
  """
  This function returns True if a given integer is the sum
  of two prime numbers and prints all unique prime number pairs
  whose sum amounts to the given integer.
  """
  if number < 4:
      return False
  
  found = set()
  for i in range(2, number):
      good = True
      # check if i is a prime
      for x in range(2, int(i**0.5)+1):
          if i % x == 0:
              good = False
              break
      if good:
          # i is a prime, now check if j = x - i is prime
          j = number - i
          good2 = True
          for x in range(2, int(j**0.5)+1):
              if j % x == 0:
                  good2 = False
                  break
          if good2 and (i,j) not in found and (j,i) not in found:
              #print(f"The number {number} equals "
                    #f"to the sum of {i} and {j}")
              found.add((i,j))
  return list(found)


def validate():
  """
  This function repeatedly asks the user for a number, checks for 
  non-integer values and prints an error message until a valid 
  number is entered.
  """
  while True:
    try:
      number = int(input("Enter a number: "))
      return number
    except ValueError:
      print("Error! Invalid number")


def print_lst(prime_lists):
  """
  This function prints the lists of primes that
  sum up to the number.
  """
  for pair in prime_lists:
    print(f"The number {pair[0] + pair[1]} equals " 
    f"to the sum of {pair[0]} and {pair[1]}")


def main():
  print_lst(is_sum_of_two_primes(validate()))


if __name__ == "__main__":
  main()
