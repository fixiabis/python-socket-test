# 引入 socket
import socket

# 定義 測試socket超時 的功能


def test_socket_timeout():
    # s 為 從socket中 建立 socket 代入 設定domain為IPV4協定, type為序列化的連接導向位元串流
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 印出預設socket超時
    print("Default socket timeout: %s" % s.gettimeout())
    # 從s中 設定超時 代入 100
    s.settimeout(100)
    # 印出目前socket超時
    print("Current socket timeout: %s" % s.gettimeout())


# 若該檔案作為主程式時
if __name__ == '__main__':
    # 測試socket超時
    test_socket_timeout()
