import mmh3

def murmur3_hash(input_data, seed=0):
    """
    Calculate the MurmurHash3 hash of the given input data.
    
    Args:
        input_data (bytes or str): The input data to be hashed.
        seed (int, optional): The seed value for the hash function. Defaults to 0.
        
    Returns:
        int: The MurmurHash3 hash value as an integer.
    """
    input_bytes = input_data.encode() if isinstance(input_data, str) else input_data
    return mmh3.hash(input_bytes, seed)