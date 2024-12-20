import base64

def decode_base64(encoded_str):
    try:
        # Decode the base64 string
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"Error decoding base64: {e}"

# Encoded string
encoded_string = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg=="

# Decode and print the result
decoded_string = decode_base64(encoded_string)
print("Decoded string:", decoded_string)

