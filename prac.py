# import threading

# count = 0

# def increment():
#     global count
#     for _ in range(10_000_000):
#         count += 1

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(count)  # Won't be 20,000,000 due to GIL and race conditions


import threading, time

count = 0

def increment():
    global count
    for _ in range(10000):
        temp = count
        # time.sleep(0.0001)  # Force context switch
        count = temp + 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(count)  # Ab yeh 20,000,000 nahi hoga
