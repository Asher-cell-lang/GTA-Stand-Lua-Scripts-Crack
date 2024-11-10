import sys

# 定义Base64字符集
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def enc(byte_data):
    """
    模拟Lua脚本中的加密过程，用于加密Lua脚本。
    """
    # 第一步：将字节数据转换为二进制字符串
    binary_str = ""
    for byte in byte_data:
        binary_str += bin(byte)[2:].zfill(8)

    # 第二步：将二进制字符串按6位分组，转换为Base64字符
    encoded_str = ""
    for i in range(0, len(binary_str), 6):
        group = binary_str[i:i+6]
        if len(group) < 6:
            # 如果最后一组不足6位，用0补齐
            group = group.ljust(6, '0')
        index = int(group, 2)
        encoded_str += BASE64_CHARS[index]

    return encoded_str


def read_file(file_path):
    """
    读取文件内容。
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错: {e}")
        sys.exit(1)


def write_file(file_path, data):
    """
    写入数据到文件。
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"写入文件时出错: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("使用方法: python 加密.py <原始文件.lua> <加密输出.lua>")
        sys.exit(1)

    input_file = sys.argv[1]
    encrypted_output = sys.argv[2]

    # 读取原始Lua脚本内容
    raw_data = read_file(input_file)

    # 执行加密
    encrypted_str = enc(raw_data)

    # 写入加密后的Lua脚本
    write_file(encrypted_output, encrypted_str)

    print(f"加密成功！加密后的脚本已保存到 '{encrypted_output}'。")


if __name__ == "__main__":
    main()
