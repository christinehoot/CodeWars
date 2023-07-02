# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    result = ''
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result


print(fake_bin('366058562030849490134388085'))  # 01101111000010
