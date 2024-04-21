from hash_algorithms import md5, sha256, murmur3

def get_user_input():
    """
    Get input data from the user.
    
    Returns:
        str: The input data provided by the user.
    """
    return input("Enter input data: ")

def display_hash_values(input_data):
    """
    Display the hash values for the given input data using different algorithms.
    
    Args:
        input_data (str): The input data to be hashed.
    """
    print(f"Input data: {input_data}")
    print(f"MD5 hash: {md5.md5_hash(input_data)}")
    print(f"SHA-256 hash: {sha256.sha256_hash(input_data)}")
    print(f"MurmurHash3 hash: {murmur3.murmur3_hash(input_data)}")

def run_user_interface():
    """
    Run the user interface loop to get input data and display hash values.
    """
    while True:
        input_data = get_user_input()
        if input_data.lower() == "exit":
            break
        display_hash_values(input_data)