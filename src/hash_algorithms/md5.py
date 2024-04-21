import hashlib

def md5_hash(input_data):
    """
    Calculate the MD5 hash of the given input data.
    
    Args:
        input_data (bytes or str): The input data to be hashed.
        
    Returns:
        str: The MD5 hash value as a hexadecimal string.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(input_data.encode() if isinstance(input_data, str) else input_data)
    return md5_hash.hexdigest()