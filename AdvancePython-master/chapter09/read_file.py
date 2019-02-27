"""
需求：
    500G的文件, 每行内容是按分隔符 {|} 标识，存为一行。
    现在要一行一行地存入数据库。
分析：
    文件太大，不能直接读进内存；
    只有一行，也不能按行读取；
    只能按固定的字节数读取，并解析分隔符
"""


def my_read_lines(file, sep):
    buf = ""

    while True:
        while sep in buf:  # 如果buf中有分隔符
            pos = buf.index(sep)  # buf中出现第一个分隔符的位置
            yield buf[:pos]  # 返回buf中从开头到出现第一个分隔符之间的内容
            buf = buf[pos + len(sep):]  # 只保留buf中第一个分隔符之后的内容

        chunk = file.read(4096 * 10)  # 每次从文件中读4096 * 10字节

        if not chunk:  # 说明已经读到了文件结尾
            yield buf
            break

        buf += chunk  # 将读取的内容，追加进buf中

with open("input.txt") as f:
    for line in my_read_lines(f, "{|}"):
        print(line)

