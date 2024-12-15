import time

def timer_decorator(func):
    """
    A decorator that calculates and prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result  # Return the function's result
    return wrapper
@timer_decorator
def slow_function():
    time.sleep(2)  # Simulate a slow operation
    print("Finished slow function!")

@timer_decorator
def add(a, b):
    return a + b

# Call the decorated functions
slow_function()  # Outputs the execution time
result = add(3, 5)
print(f"Result: {result}")