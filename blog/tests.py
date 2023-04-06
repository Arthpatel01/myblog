from django.test import TestCase

# Create your tests here.

from cryptography.fernet import Fernet
import os

# Generate a secure 256-bit key
key = Fernet.generate_key()

# Generate a 128-bit nonce
nonce = os.urandom(16)

# Generate a 16-byte salt
salt = os.urandom(16)

# Create an instance of Fernet cipher
cipher = Fernet(key)

print('---------------->>nonce', nonce.decode())
print('---------------->>salt', salt)
print('---------------->>cipher', cipher)