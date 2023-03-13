#!/usr/bin/env python3

# 0-25 alphabet UPPER CASE
# 26-35 are the decimal digits
# 36 underscore
# flag structure: picoCTF{decrypted_message}

import string
alphabet = string.ascii_uppercase
digits = string.digits
flag = []

with open('message.txt') as f:
    f_content = f.read()
    f_con_lst = [int(n) for n in f_content.split()]
    for i in f_con_lst:
        mod_val = i % 37
        if mod_val in range(26):
            flag.append(alphabet[mod_val])
        elif mod_val in range(26, 36):
            flag.append(digits[mod_val - 26]) # offset
        else:
            flag.append('_')

print('picoCTF{%s}' % ''.join(flag))