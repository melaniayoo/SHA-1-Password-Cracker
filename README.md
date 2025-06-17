# 🔐 SHA‑1 Password Cracker

A dictionary-based SHA‑1 password cracker built in Python. Given a SHA‑1 hash, it attempts to find the original password using a list of the top 10,000 passwords, with optional salt support. 

(A salt is a random or fixed string added to a password before hashing to make the resulting hash more secure and unique, even if the password itself is common or reused.)

## Project Features

- Dictionary attack using top-10000-passwords.txt
- Optional salted cracking, trying both salt + password and password + salt
- Built with Python’s standard hashlib (no external dependencies)
- Includes test integration (test_module.py) for validation

## Project Structure: 

```
├── main.py               
├── password_cracker.py # Core cracking logic  
├── test_module.py      # Unit tests  
├── top-10000-passwords.txt  # Common password list  
└── known-salts.txt     # Optional salt list
```

## Build Instructions

Clone this repository and run:
```bash
python main.py
```

## Credits

This project is based on the boilerplate provided by freeCodeCamp.
You can find the original project instructions at:
https://www.freecodecamp.org/learn/information-security/information-security-projects/sha-1-password-cracker
