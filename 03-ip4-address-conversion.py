# 引入 socket
import socket
# 從 binascii 引入 hexlify
from binascii import hexlify

# 定義 轉換IPV4位址 的功能 需要 IP位址陣列


def convert_ip4_address(ip_addrs):
    # IP位址 取得自 IP位址陣列
    for ip_addr in ip_addrs:
        # 32位元IP位址 為 從socket中 轉換整數 代入 IP位址
        packed_ip_addr = socket.inet_aton(ip_addr)

        # IP位址 為 從socket中 轉換IP位址 代入 32位元IP位址
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        # 印出
        print(
            # IP位址與轉換結果
            "IP Address: %s => Packed: %s, Unpacked: %s"
            % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)
        )


# 若該檔案作為主程式時
if __name__ == '__main__':
    # 轉換IPV4位址 代入 IP位址陣列
    convert_ip4_address(['127.0.0.1', '192.168.0.1'])
