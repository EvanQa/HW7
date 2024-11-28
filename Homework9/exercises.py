
#exercise 1

def function(a: int, b: int):
    if a > b:
        print(" A bigger than B", a)
    else:
        print(" A smaller than B", b)
    return a and b

if __name__ == '__main__':
    result = function(10,20)
    print(result)
#
# #exercise 2

def add_and_return(a: int, b: int):
    if a > b:
        print(" A bigger than B \n A = ", a)
    elif a == b:
        a += 1
        print(f" A equal B , and add 1 to the first parameter",a)
    else:
        print(" A smaller than B \n B = ", b)
    return a and b

if __name__ == '__main__':
   result = add_and_return(10, 10)
   print(result)

#exercise 3

def minimal(a, b, c, d):
    if (1 <= a <= 5) or (1 <= b <= 5) or (1 <= c <= 5) or (1 <= d <= 5):
        return -1
    return min(a,b,c,d)

print(minimal(1,6,9,10))
print(minimal(6,12,45,55))
#
# #exercise 4
def even_not_even(a):
    return "even" if a % 2 == 0 else "not even"

print(even_not_even(5))
print(even_not_even(2))

#exercise 5

def equals_numbers(a, b, c, d):
    if a == b == c == d:
        return "all equals"
    elif a == b and c!= d:
        return "only 2 numbers are equals"
    else:
        return "all numbers not equals"

print(equals_numbers(2,2,2,2))
print(equals_numbers(2,2,4,5))
print(equals_numbers(3,4,5,7))

#exercise 6
def switch(day):
    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return  "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else:
       return "Error"


print(switch(1))
print(switch(2))
print(switch(3))
print(switch(4))
print(switch(5))
print(switch(6))
print(switch(7))
print(switch(8))

print()
#exercise 7

def day_in_month(month):
    if month < 1 or month > 12:
        return -1
    if month in {1, 3, 5, 7, 8, 10, 12}:  # Months with 31 days
        return 31
    elif month == 2:  # February
        return 28
    else: # Months with 30 days
        return 30

print(day_in_month(1), "January")
print(day_in_month(2), "February")
print(day_in_month(3), "March")
print(day_in_month(4), "April")
print(day_in_month(5), "May")
print(day_in_month(6), "June")
print(day_in_month(7), "July")
print(day_in_month(8), "August")
print(day_in_month(9), "September")
print(day_in_month(10),"October")
print(day_in_month(11),"November")
print(day_in_month(12),"December")
print(day_in_month(13),"Invalid month")

#exercise 8