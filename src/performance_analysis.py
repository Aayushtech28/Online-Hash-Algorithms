import time
from hash_algorithms import md5, sha256, murmur3

def measure_execution_time(hash_function, input_data):
    """
    Measure the execution time of a given hash function for the input data.
    
    Args:
        hash_function (callable): The hash function to be measured.
        input_data (bytes or str): The input data to be hashed.
        
    Returns:
        float: The execution time in milliseconds.
    """
    start_time = time.time()
    hash_function(input_data)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def analyze_performance(input_data):
    """
    Analyze the performance of different hash algorithms for the given input data.
    
    Args:
        input_data (bytes or str): The input data to be hashed.
    """
    md5_time = measure_execution_time(md5.md5_hash, input_data)
    sha256_time = measure_execution_time(sha256.sha256_hash, input_data)
    murmur3_time = measure_execution_time(murmur3.murmur3_hash, input_data)
    
    print("Performance Analysis:")
    print(f"MD5 execution time: {md5_time} ms")
    print(f"SHA-256 execution time: {sha256_time} ms")
    print(f"MurmurHash3 execution time: {murmur3_time} ms")