# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import time
import itertools
import sys
import multiprocessing
import math
from itertools import islice
from queue import Queue

from pyforce.commons import ENCRYPTIONS

#  from string import ascii_letters as charters_pool
from string import ascii_lowercase as charters_pool

CHAR_POOL = charters_pool
REVERSE_CHAR_POOL = CHAR_POOL[::-1]

CHAR_POOLS = [CHAR_POOL, REVERSE_CHAR_POOL]


#  def attack_sized_string(pass_list):
#      #  tested_strings = itertools.product(kwargs['char_pool'], repeat=length)
#      _encryption = kwargs['encryption']
#      for characters in tested_strings:
#          tested_string = ''.join(characters)
#          tested_hash = ENCRYPTIONS[_encryption](
#              tested_string.encode('utf-8')).hexdigest()
#          _line = "{} :: {} \n".format(tested_string, tested_hash)
#          if tested_hash == kwargs['password_hash']:
#              print('$$ GG Password is: "{}"'.format(tested_string))
#              print('$$ Finished at: {}'.format(time.strftime('%H:%M:%S')))
#              for job in jobs is not None:
#                  job.terminate()
#              sys.exit(0)

def attack_sized_string(**kwargs):
    _encryption = kwargs['encryption']
    for test_pass in kwargs['pass_list']:
        tested_string = ''.join(test_pass)
        tested_hash = ENCRYPTIONS[_encryption](
            tested_string.encode('utf-8')).hexdigest()
        print(tested_string)
        _line = "{} :: {} \n".format(tested_string, tested_hash)
        if tested_hash == kwargs['password_hash']:
            print('$$ GG Password is: "{}"'.format(tested_string))
            print('$$ Finished at: {}'.format(time.strftime('%H:%M:%S')))
            for job in jobs is not None:
                job.terminate()
            sys.exit(0)


def process_char_pool(char_pool, **kwargs):
    char_pool_jobs = []
    #  process = multiprocessing.Process(
    #      target=attack_sized_string, args=(n,), kwargs=_kwargs)
    #  char_pool_jobs.append(process)
    #  process.start()
    #  combination = itertools.product(char_pool, repeat=kwargs['size'])
    #  it = iter(combination)
    #  chain([xs[0:n]], groupsof(n, xs[n:]))

    size = kwargs['size']
    print(type(size))
    combination_number = int(math.pow(len(char_pool), size))
    print(combination_number)
    chunck_size = combination_number // kwargs['thread_number']
    _kwargs = {
        #  'char_pool': char_pool,
        'encryption': kwargs['encryption'],
        'password_hash': kwargs['password_hash']
    }
    for start in range(0, combination_number, chunck_size):
        print('test')
        stop = start + chunck_size
        #  pass_list = list(islice(combination, start, stop))
        _kwargs['pass_list'] = pass_list
        #  process = multiprocessing.Process(
        #      target=attack_sized_string, kwargs=_kwargs)
        #  char_pool_jobs.append(process)
        #  process.start()
    #  attack_sized_string(n, char_pool=char_pool,
    #  encryption=kwargs['encryption'],
    #  password_hash=kwargs['password_hash'])


def attack(password_hash, encryption, size=6, thread_number=4):
    print('$$ Start at: {}'.format(time.strftime('%H:%M:%S')))
    global jobs
    jobs = []
    _kwargs = {
        'password_hash': password_hash,
        'encryption': encryption,
        'size': size,
        'thread_number': thread_number,
        'password_hash': password_hash
    }
    #  for char_pool in CHAR_POOLS:
    #      process = multiprocessing.Process(
    #          target=process_char_pool, args=(char_pool,), kwargs=_kwargs)
    #      jobs.append(process)
    #      process.start()
    process = multiprocessing.Process(
        target=process_char_pool, args=(CHAR_POOLS[0],), kwargs=_kwargs)
    jobs.append(process)
    process.start()

    for job in jobs:
        job.join()
    char_pool = CHAR_POOLS[0]
    process_char_pool(char_pool, kwargs=_kwargs)
    print('$$ password not found')
    sys.exit(1)
