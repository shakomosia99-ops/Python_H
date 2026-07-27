# Task 1

def commission(func):
    def wrapper(balance, amount):
        total = amount + 1
        if total > balance:
            return f"Error: Insufficient funds! Need {total}$, Balance: {balance}$"
        return func(balance, total)
    return wrapper


@commission
def transaction(balance, amount):
    balance -= amount
    return f"Transaction successful! Remaining Balance: {balance}$"


print(transaction(100, 50))
print(transaction(100, 100))

print("____________________________")


# Task 2

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} Called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@count_calls
def say_hello():
    print("Hello!")


say_hello()
say_hello()
say_hello()
