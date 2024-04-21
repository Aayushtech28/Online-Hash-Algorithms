import hashlib

def sha256_hash(input_data):
    """
    Calculate the SHA-256 hash of the given input data.
    
    Args:
        input_data (bytes or str): The input data to be hashed.
        
    Returns:
        str: The SHA-256 hash value as a hexadecimal string.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_data.encode() if isinstance(input_data, str) else input_data)
    return sha256_hash.hexdigest()