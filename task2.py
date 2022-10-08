#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    numb = {5: 'five', 6: 'six', 1: "one"}
    dict_items = {v: k for k, v in numb.items()}
    print(numb)
    print(dict_items)
