# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from pyforce.commons import ENCRYPTIONS
import sys
import time

def dict_attack(password_hash, dict_path, encryption):
    with open(dict_path, "rU") as read_file:
        for row in read_file:
            row = row.split('\n')[0]
            tested_hash = ENCRYPTIONS[encryption](
                row.encode('utf-8')).hexdigest()
            if tested_hash == password_hash:
                print('$$ GG Password is: "{}"'.format(row))
                print('$$ Finished at: {}'.format(time.strftime('%H:%M:%S')))
                sys.exit(0)
        read_file.closed
        print('password not found')
        sys.exit(1)
