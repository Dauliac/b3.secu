# -*- coding: utf-8 -*-
# !/usr/bin/env python3


def dict_attack(password_hash, dict_path, max_size, encryption):
    with open(dict_path, "rU") as read_file:
        tested_hash = ENCRYPTIONS[encryption](
            tested_string.encode('utf-8')).hexdigest()
        if tested_string == row:
            print('$$ GG Password is: "{}"'.format(tested_string))
            print('$$ Finished at: {}'.format(time.strftime('%H:%M:%S')))
            sys.exit(0)
    read_file.closed
    print('password not found')
    sys.exit(1)
