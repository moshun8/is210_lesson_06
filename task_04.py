#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Password cracking"""


import data
SALT = 'monosodium-glutamate'


def test_passwords(pwd_list):
    """"reads list, tests the password"""
    cracked_pwds = []
    if isinstance(pwd_list, list):
        for entry in pwd_list:
            fields = entry.split(':')
            word = crack_it(fields[1])
            if word:
                cracked_pwds.append((fields[4], word))
    else:
        pwd_list = []
        return pwd_list
    report(cracked_pwds)


def crack_it(crypt_pwd):
    """compares password to common ones"""
    for word in data.WORDS:
        if crypt_pwd == data.crypt(word, SALT):
            return word
    return ''


def report(cracked_pwds):
    """"display bad passwords"""
    print 'Cracked passwords'
    print '-------------------------------'
    if isinstance(cracked_pwds, list):
        for pwd in cracked_pwds:
            print '{0:<15}  {1:<5}'.format(pwd[0], pwd[1])
    else:
        cracked_pwds = []
        return cracked_pwds

test_passwords(data.PASSWD)
test_passwords(None)