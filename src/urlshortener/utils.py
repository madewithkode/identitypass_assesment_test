import string
import random

URL_FRIENDLY_BASE56 = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

def generate_shortened_url(latest_id, length=8):
    """
        Generate a unique URL by encoding unique 
        integers into BASE56 using URL-friendly characters.
    """
    
    latest_id = latest_id + 1
    digits = string.digits
    result_str = ''.join((random.choice(digits) for i in range(length)))
    num = int(result_str) + latest_id

    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(URL_FRIENDLY_BASE56)
    while num:
        num, rem = _divmod(num, base)
        arr_append(URL_FRIENDLY_BASE56[rem])
    arr.reverse()
    result = ''.join(arr)
    
    return result