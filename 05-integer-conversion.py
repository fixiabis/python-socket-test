# 引入 socket
import socket

# 定義 轉換整數 的功能 需要 數值
def convert_integer(num):
    # 印出 32-bit的本機長度與網路長度
    print(
        "Original: %s => Long  host byte order: %s, Network byte order: %s"
        % (num, socket.ntohl(num), socket.htonl(num))
    )

    # 印出 16-bit的本機長度與網路長度
    print(
        "Original: %s => Short  host byte order: %s, Network byte order: %s"
        % (num, socket.ntohs(num), socket.htons(num))
    )


# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 轉換整數 代入 1234
    convert_integer(1234)
