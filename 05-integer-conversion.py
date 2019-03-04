# 引入 socket
import socket

# 定義 轉換整數 的功能 需要 數值


def convert_integer(num):
    # 印出
    print(
        # 32-bit的本機長度與網路長度
        "Original: %s => Long  host byte order: %s, Network byte order: %s"
        % (num, socket.ntohl(num), socket.htonl(num))
    )

    # 印出
    print(
        # 16-bit的本機長度與網路長度
        "Original: %s => Short  host byte order: %s, Network byte order: %s"
        % (num, socket.ntohs(num), socket.htons(num))
    )


# 若該檔案作為主程式時
if __name__ == '__main__':
    # 轉換整數 代入 1234
    convert_integer(1234)
