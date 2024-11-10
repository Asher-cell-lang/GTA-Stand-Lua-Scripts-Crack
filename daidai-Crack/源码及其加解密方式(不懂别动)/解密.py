import sys

# 定义Base64字符集
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def remove_random_chars_bytes(byte_data, chars_to_remove):
    """
    从字节数据中移除指定的随机字符。
    """
    chars_to_remove_bytes = chars_to_remove.encode('ascii')
    return bytes(c for c in byte_data if c not in chars_to_remove_bytes)


def dec(encoded_str):
    """
    模拟Lua脚本中的dec函数，用于解密加密的Lua脚本。
    """
    # 第一步：移除所有不在Base64字符集或'='中的字符
    cleaned = ''.join(c for c in encoded_str if c in BASE64_CHARS or c == '=')
    
    # 第二步：将每个Base64字符转换为6位二进制字符串
    binary_str = ""
    for char in cleaned:
        if char == '=':
            # 跳过填充字符
            continue
        index = BASE64_CHARS.find(char)
        if index == -1:
            # 如果字符不在Base64字符集中，跳过
            continue
        # 转换为6位二进制
        bits = bin(index)[2:].zfill(6)
        binary_str += bits
    
    # 第三步：将二进制字符串按8位分组并转换为字节
    byte_array = bytearray()
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) < 8:
            # 如果最后一组不足8位，忽略
            continue
        byte_int = int(byte, 2)
        byte_array.append(byte_int)
    
    return byte_array


def read_file(file_path):
    """
    读取文件内容。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错: {e}")
        sys.exit(1)


def write_file(file_path, byte_data):
    """
    写入字节数据到文件。
    """
    try:
        with open(file_path, 'wb') as file:
            file.write(byte_data)
    except Exception as e:
        print(f"写入文件时出错: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("使用方法: python 解密.py <加密文件.lua> <解密输出.lua>")
        sys.exit(1)

    encrypted_file = sys.argv[1]
    decrypted_output = sys.argv[2]

    # 读取加密的Lua脚本内容
    encrypted_data = read_file(encrypted_file)

    # 执行解密
    decrypted_bytes = dec(encrypted_data)

    # 写入解密后的Lua脚本
    write_file(decrypted_output, decrypted_bytes)

    print(f"解密成功！解密后的脚本已保存到 '{decrypted_output}'。")


if __name__ == "__main__":
    main()