from thread_class import BackgroundTask

def square(a, b):
    print("inside thread", a*b)
    return a*b

def main():
    print("start")
    bg_helper = BackgroundTask(max_workers=4)
    
    bg_helper.do_in_background(square, 3, 4)
    # result = bg_helper.do_in_background(square, 3, 4)
    # print(result.result(), "result")
    # .result() blocks and waits for the thread to finish, then gives the return value of the thread function.
    
    
    
if __name__ == "__main__":
    main()
    
    

# future.result() => Result get karo (wait karta hai)
# future.done() => Complete hua ya nahi check karo
# future.running() => Currently running hai ya nahi
# future.cancel() => Task cancel karne ki koshish
