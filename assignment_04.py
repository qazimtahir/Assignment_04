name = str(input("What is your name:  "))
first_number = int(input('Enter your first favorite number:  '))
second_number = int(input('Enter your first favorite number:  '))
third_number = int(input('Enter your first favorite number:  '))

print(f"Hello, {name}! Let's explore your favorite numbers:")



numbers_list = [first_number, second_number, third_number]

i = 0
while i<len(numbers_list):
  if(numbers_list[i]%2==0):
    print(f"{numbers_list[i]} is an EVEN number")
  else:
    print(f"{numbers_list[i]} is an ODD number")
  # print(numbers_list[i])
  i+=1
  
for j in numbers_list:
  print (f"The number {j} and its square: ({j}, {j*j}) ")
  
  
def is_prime(total_of_all):
    if total_of_all <= 1:
        return False
    if total_of_all <= 3:
        return True
    if total_of_all % 2 == 0 or total_of_all % 3 == 0:
        return False
    i = 5
    while i * i <= total_of_all:
        if total_of_all % i == 0 or total_of_all % (i + 2) == 0:
            return False
        i += 6
    return True

total_of_all = int(first_number+second_number+third_number)
if total_of_all%2 ==0:
  print(f"Amazing! The sum of your favorite numbers is: {total_of_all}")
if is_prime(total_of_all):
  print(f"Wow, {total_of_all} 'is' a prime number!")
else:
  print(f"Wow, {total_of_all} 'is' not a prime number!")

  
