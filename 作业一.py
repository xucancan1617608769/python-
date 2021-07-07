def count_letter_number(string):   #封装的函数
    letter_count = 0
    digit_count = 0
    for ch in string:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            letter_count += 1
        elif '0' <= ch <= '9':
            digit_count += 1
    return letter_count, digit_count
# 比如我们只想导入以上这一部分函数,不需要导入以下的main()函数,那么我们就把main()函数执行的返回值放在if里面.main()函数只能在本文件名中执行,不会被其他模块调用.
def main():
    print(count_letter_number('a1b2c3d4'))  # (4, 4)      #调用封装的函数
    print(count_letter_number('a123456b'))  # (2, 6)      #执行语句
    print(count_letter_number('123456!!'))  # (0, 6)
if __name__ == '__main__':
    main()   
# 总结:如果对封装的函数返回的结果不想在导入的模块中执行,那么就把函数执行返回的函数名放在if __name__ == '__main__':下面保护起来.它就相当于一把闭加锁.
