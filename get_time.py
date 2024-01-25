import time

def get_time(function):
   def wrapper(*args, **kwargs):
      start = time.time()
      result = function(*args, **kwargs)
      end = time.time()
      print(f"time taken by {function.__name__}: {(end-start)*10**3} ms")
      return result
   return wrapper