def write_file(file_path, content):
    """
        方法：写入文件
        参数：
            - file_path:要写入的文件路径
            - content：要写入的内容
    """
    with open(file_path, 'w') as f:
        f.write(content)


def read_file(file_path):
    """
        方法：读取文件
        参数：
            - file_path:要写入的文件路径
    """
    with open(file_path, 'r') as f:
        t = f.readline()

    return t

# 写入demo
# a = "这是测试的token"
# write_file('token.txt', a)

# 读取demo
# res = read_file('token.txt')
# print(res)