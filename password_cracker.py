import hashlib  # Import the hashlib module for hashing functions like SHA-1

def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 common passwords from file into a list
    passwords = read_file_lines("top-10000-passwords.txt")

    if use_salts:
        # If salts should be used, load the known salts from file into a list
        salts = read_file_lines("known-salts.txt")

        # Try all combinations of salt and password
        for salt in salts:
            for password in passwords:
                # Create two combinations: salt+password and password+salt
                combo1 = (salt + password).encode('utf-8')  # Prepend salt
                combo2 = (password + salt).encode('utf-8')  # Append salt

                # Compute the SHA-1 hash for both combinations and compare to input hash
                if hashlib.sha1(combo1).hexdigest() == hash:
                    return password  # Return the matching password if found
                if hashlib.sha1(combo2).hexdigest() == hash:
                    return password  # Also check the appended case
    else:
        # If not using salts, check each password directly
        for password in passwords:
            # Encode the password and compute SHA-1 hash
            if hashlib.sha1(password.encode('utf-8')).hexdigest() == hash:
                return password  # Return password if it matches the given hash

    # If no matching hash is found, return a default message
    return "PASSWORD NOT IN DATABASE"

def read_file_lines(file_name):
    """
    Reads a file line by line, strips whitespace, and returns a list of lines.
    Assumes UTF-8 encoding.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]  # Strip newline and extra whitespace
