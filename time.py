import timeit

# Define the code to be timed
code_to_test = """
l = [1, 2, 3, 4]
"""

# Measure the time it takes to execute the code
execution_time = timeit.timeit(stmt=code_to_test, number=1000000)

print(execution_time)
