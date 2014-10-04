#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Password cracking"""


import data
SALT = 'monosodium-glutamate'
 

def test_passwords(pwd_list=[]):
    """"reads list, tests the password"""
    crackedPwds = []
    for entry in pwd_list:
        fields = entry.split(':')  #splits items into pieces by :
        word = crack_it(fields[1])  # word = encrypted password
        if (word != ''):  # if the field isn't empty, add to list
            crackedPwds.append(fields[4], word)  # report wants names

    report(crackedPwds)

def crack_it(cryptedPwd):
    """compares password to common ones"""
    for word in data.WORDS:
        if (cryptedPwd == data.crypt(word, SALT)):
            return word
    return ''


def report(crackedPwds):
    """"display bad passwords"""
    print 'Cracked passwords'
    print '-------------------------------'
    for pwd in crackedPwds:
        print '{0}     {1}'.format(pwd[0], pwd[1])

test_passwords(data.PASSWD)