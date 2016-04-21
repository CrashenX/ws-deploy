#!/usr/bin/env python

from passlib.hash import sha512_crypt
from getpass import getpass

pass1 = getpass("Type your password: ")
pass2 = getpass("Type your password again: ")
if pass1 != pass2:
    print("Passwords do not match")
else:
    print(sha512_crypt.encrypt(pass1))
