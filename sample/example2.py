
def check_substring(str, substr):
    if substr.lower() in str.lower():
        return True
    else:
        return False


if __name__ == '__main__':
    import sys
    print(check_substring('my name is ali', 'Alia'))
