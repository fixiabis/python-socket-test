# 引入 socket
import socket

# 定義 測試socket超時 的功能
def test_socket_timeout():
    # s 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 印出 預設socket超時
    print("Default socket timeout: %s" % s.gettimeout())

    # 讓s 執行 設定超時 代入 100
    s.settimeout(100)

    # 印出 目前socket超時
    print("Current socket timeout: %s" % s.gettimeout())


# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 測試socket超時
    test_socket_timeout()
