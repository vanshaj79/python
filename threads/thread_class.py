from concurrent.futures import ThreadPoolExecutor


class BackgroundTask:
    def __init__(self, max_workers=4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        
    def do_in_background(self, func, *args, **kwargs):
        def do_task():
            try:
                return func(*args, **kwargs)
            except:
                print("failed")
        return self.executor.submit(do_task)
    