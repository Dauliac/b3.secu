# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from hashlib import md5
from hashlib import sha256
from hashlib import sha384

ENCRYPTIONS = {1: md5, 5: sha256, 6: sha384}

HEADER = """
.______   ____    ____  _______   ______   .______        ______  _______
|   _  \  \   \  /   / |   ____| /  __  \  |   _  \      /      ||   ____|
|  |_)  |  \   \/   /  |  |__   |  |  |  | |  |_)  |    |  ,----'|  |__
|   ___/    \_    _/   |   __|  |  |  |  | |      /     |  |     |   __|
|  |          |  |     |  |     |  `--'  | |  |\  \----.|  `----.|  |____
| _|          |__|     |__|      \______/  | _| `._____| \______||_______|
"""

def log_into_file(log_file, password, hash_string):
    with open(log_file , "a") as read_file:
        read_file.write(_line)
    read_file.closed
