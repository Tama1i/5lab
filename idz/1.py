#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("enter kVt/h "))

    if (a <= 250):
       print("k oplate ",a * 7)
    elif a > 250 and a <= 300:
      print("k oplate ",a * 17)
    elif a > 300:
      print("k oplate ", a * 20)
