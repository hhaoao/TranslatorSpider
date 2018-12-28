import re


def concatenation(a, b):
    yield a
    yield b


def fib(file_str_obj, num_limit):
    f_str = file_str_obj  # .decode()
    file_str = [f_str[start:(num_limit+start)] for start in range(0, len(f_str), num_limit)]  # 根据字数分割字符串
    str_num = len(file_str)
    pattern = re.compile(r"[\s\S]+(?<=[.!])")  # 读取任意字符直到遇到点或！为止
    sun_pattern = re.compile(r'([.!])')
    temp_str_new, temp_bool_new = [''] * (2 * str_num), [False] * (2 * str_num)  # 存储二次分割的字符串及布尔值
    cor_str, index_one = [None] * (str_num + 1), 0  # 存储处理完的字符串， 指针

    for index, new_str in enumerate(file_str):  # 二次分割字符串
        temp_num_new = re.match(pattern, new_str)
        if temp_num_new:
            temp_num = temp_num_new.span()
            temp_bool_new[index * 2] = True
        else:
            temp_num = (0, len(new_str))
        temp_str_new[index * 2] = ''.join(new_str[temp_num[0]:temp_num[1]])
        temp_str_new[index * 2 + 1] = ''.join(new_str[temp_num[1]:])
    else:
        cor_str_new = [(temp_str_new[i], temp_bool_new[i]) for i in range(len(temp_str_new)) if temp_str_new[i] != '']

    for index, new_str in enumerate(cor_str_new):
        if not index:  # 第一组字符串特殊处理
            cor_str[index_one] = cor_str_new[index][0]
            index_one += 1
            continue
        if not cor_str_new[index - 1][1]:  # 上个为假
            index_one -= 1
            cor_str[index_one] = ''.join(concatenation(cor_str[index_one], cor_str_new[index][0]))
        else:
            cor_str[index_one] = ''.join(cor_str_new[index][0])
        index_one += 1

    cor_str = [i for i in cor_str if i is not None]
    for index, new_str in enumerate(cor_str):
        #  根据字数分割字符串,超字数时处理
        if len(new_str) > num_limit:
            cor_str_new = [new_str[start:(num_limit+start)] for start in range(0, len(new_str), num_limit)]
            cor_str[index:index+1] = cor_str_new
    # ['a!', 'bc!', '!', 'd!', 'ef!', 'ghi', 'j!', 'klm', 'n!', 'opq', 'uvw', '!', 'syz', '!!', '!!!', '!!!']

    for index, new_str in enumerate(cor_str):           # 最后整理,未解决. 2018.6.28
        index_one = index - 1
        if not index:
            continue
        str_len = len(cor_str[index_one])
        new_str_len = num_limit - str_len  # 能添加字符串长度
        temp_str = re.search(sun_pattern, new_str[:new_str_len])
        if new_str_len and temp_str:
            cor_str[index_one] = ''.join(concatenation(cor_str[index_one], new_str[:new_str_len]))
            if new_str[new_str_len:]:
                cor_str[index] = new_str[new_str_len:]
            else:
                del cor_str[index]

    return cor_str


class File_str:
    def __init__(self, fe_str, str_len):
        # self.file_obj = codecs.open(filename=fe_str, mode='r', encoding='utf-8')
        self.file_str = fe_str  # self.file_obj.read()  # 保存文件内容
        self.p_file_str = fib(self.file_str, str_len)


# d = 'a!bc!!d!ef!ghij!klmn!opquvw!syz!!!!!!!!'
# dd = fib(d, 3)
# print(dd)
