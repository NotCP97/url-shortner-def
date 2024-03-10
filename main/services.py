import uuid
from main.models import ShortURL

def generate_short_url(url: str) -> str:
    """
    Generate a short URL for the given long URL.
    """
    count = ShortURL.objects.count()
    get_hash = decimal_to_base62(count, 7)
    return f"http://localhost:8000/{get_hash}/"


BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decimal_to_base62(decimal_num, pad_length=7):
    """
    Convert a decimal number to a base62 string with a fixed length.
    
    Args:
        decimal_num (int): The decimal number to convert.
        pad_length (int, optional): The desired length of the base62 string.
            If the resulting hash is shorter than this length, it will be padded
            with leading zeros. Defaults to 0 (no padding).
    
    Returns:
        str: The base62 representation of the input decimal number.
    """
    base62_str = ""
    while decimal_num > 0:
        decimal_num, remainder = divmod(decimal_num, 62)
        base62_str = BASE62_CHARS[remainder] + base62_str
    
    # Pad the base62 string with leading zeros if necessary
    if pad_length > 0:
        base62_str = base62_str.zfill(pad_length)
    
    return base62_str