def int_to_base(num, base):
    if num == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    is_negative = num < 0
    num = abs(num)

    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num = num // base

    if is_negative:
        result = "-" + result

    return result
    
