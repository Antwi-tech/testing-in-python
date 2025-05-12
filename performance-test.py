"""
Perfromance measures the efficiency if a software. It tests software performance
1. Testing the load time
2. Processing huge sum of data

python-benchmark is used for performance testing
benchmark can be used as function by passing it as an argument to the main func or it can be used with a decorator
and after a fucntion is defined
"""

def create_list():
    return [i for i in range(1000)]
def create_set():
    return set([i for i in range(1000)])
def find(it, el=50):
    return el in it

# Using a decorator with benchmark

# Write the performance test for a list
def test_list(benchmark):
    benchmark(find,it=create_list())

# Write the performance test for a set
def test_set(benchmark):
    benchmark(find,it=create_set())
    
def test_list(benchmark):
	# Add decorator here
    @benchmark
    def iterate_list():
		# Complete the loop here
        for test_list in [i for i in range(1000)]:
            pass

def test_set(benchmark):
	# Add decorator here
    @benchmark
    def iterate_set():
        # Complete the loop here
        for iterate_list in {i for i in range(1000)}:
            pass    