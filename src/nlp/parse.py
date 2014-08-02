import os
import logging

def get_noun_phrase(string):
    command = """\"C:\\Program Files (x86)\\Python27\python.exe\" .\\src\\factcheck.py"""
    command = "echo 'hello'"
    p = os.popen(command).readline()
    logging.info(command)
    logging.info(p)
    return p
