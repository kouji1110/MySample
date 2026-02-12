"""簡単な計算機モジュール - GitHub Actions デモ用"""

def add(a, b):
    """2つの数値を足し算"""
    return a + b

def subtract(a, b):
    """2つの数値を引き算"""
    return a - b

def multiply(a, b):
    """2つの数値を掛け算"""
    return a * b

def divide(a, b):
    """2つの数値を割り算"""
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b
