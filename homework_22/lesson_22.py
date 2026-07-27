import threading


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_prime(n, results):
    results[n] = is_prime(n)


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

results = {}
threads = []

for num in num_list:
    thread = threading.Thread(target=check_prime, args=(num, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for num in num_list:
    if results[num]:
        print(f"{num} is prime number")
    else:
        print(f"{num} is composite number")
