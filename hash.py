import hashlib


def hash_str(s):
    return hashlib.md5(s).hexdigest()


# -----------------
# User Instructions
#
# Implement the function make_secure_val, which takes a string and returns a
# string of the format:
# s,HASH

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

# print make_secure_val("cool")


def check_secure_val(h):
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val


# print check_secure_val("cool","")
# 2nd argument above should contain value from _make_secure_val