#global
x = 10

def print_global_x():
    print(f"global x: {x}")

print_global_x()  # Выведет: Глобальная x: 10
print(f"global x out of function: {x}")

#
def print_local_x():
    x = 10
    print(f"local x in function: {x}")
    print_local_x()