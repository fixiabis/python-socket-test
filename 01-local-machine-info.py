# 引入 socket
import socket

# 定義 印出機器資訊 的功能


def print_machine_info():
    # 主機名稱 為 從socket中 取得本機名稱
    host_name = socket.gethostname()

    # 本機IP 為 從socket中 取得本機藉由名稱 代入 本機名稱
    ip_address = socket.gethostbyname(host_name)

    # 印出 本機名稱
    print("Host name: %s" % (host_name))

    # 印出 本機IP
    print("IP address: %s" % (ip_address))


# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 印出機器資訊
    print_machine_info()
