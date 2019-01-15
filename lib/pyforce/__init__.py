# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from __future__ import absolute_import

from pyforce.bruteforce import attack
from pyforce.bruteforce import attack_sized_string
from pyforce.bruteforce import process_char_pool
from pyforce.dict import dict_attack


def read_shadow_file(file_name='TP1/shadow'):
    file_array = []
    with open(file_name, "rU") as read_file:
        for i, row in enumerate(read_file, 1):
            dot_split = row.split(":")
            if dot_split[1] not in ["*", "!"]:
                hash_split = dot_split[1].split("$", 2)

                user = dot_split[0]
                encryption = int(hash_split[1])
                password_hash = hash_split[2]
                did_line = {
                    'user': user,
                    'encryption': encryption,
                    'hash': password_hash
                }
                file_array.append(did_line)
            else:
                file_array.append(None)
    read_file.closed
    return file_array
