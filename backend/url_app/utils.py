import hashlib
import base64

def generate_short_key(url: str, length: int = 8) -> str:
    # Step 1: Generate SHA-256 hash of the URL
    sha256_hash = hashlib.sha256(url.encode()).digest()  # Get the raw bytes of the SHA-256 hash

    # Step 2: Encode the hash in base64
    base64_encoded = base64.urlsafe_b64encode(sha256_hash).decode('utf-8')  # Convert bytes to a base64 string

    # Step 3: Truncate the base64 encoded string to the desired length
    short_key = base64_encoded[:length]  # Limit the length to 'length' characters

    return short_key

# Example usage:
url = "https://www.example.com/some/path"
short_key = generate_short_key(url, 8)
print(f"Short Key: {short_key}")


