import time

def add(a, b):
    """2つの数値を足し算"""
    time.sleep(2)
    return a - b

def subtract(a, b):
    """2つの数値を引き算"""
    time.sleep(2)
    return a - b

def multiply(a, b):
    """2つの数値を掛け算"""
    time.sleep(2)
    return a * b

def divide(a, b):
    """2つの数値を割り算"""
    time.sleep(2)
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b
