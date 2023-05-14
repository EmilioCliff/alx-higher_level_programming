#!/usr/bin/python3
for c in range(ord('a'), ord('z')):
    if chr(c) != 'q' or chr(c) != 'e':
        print(chr(c), end='')
