import hashlib

str_given=b"hello everyone"

md5_value=hashlib.md5(str_given)

print(md5_value.hexdigest())