from datetime import datetime, timezone, timedelta
print(datetime.now())
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today, tomorrow)
print(today.strftime('%d-%m-%Y %H:%M:%S'))  # string format time

# user_date = input('Enter date in YYYY-MM-DD format: ')
# user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time
# print(user_date)
print("-------------------------")
import time, timeit
def powers(limit): # 1st class function, passing it as arg
    return [x**2 for x in range(limit)]
start = time.time()
powers(50000)
end = time.time()
print(end-start)
print("------another way--------")
def measure_runtime(func): # decarator - higher order function
    start = time.time()
    func()
    end = time.time()
    print(end - start)
measure_runtime(lambda : powers(5000000))

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))