# 引入 socket
import socket

# 定義 測試socket模式 的功能
def test_socket_modes():
    # s 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為序列化的連接導向位元串流
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 讓s 執行 設定阻塞 代入 非阻塞
    s.setblocking(0) #0 = non-blocking mode, 1 = blocking mode and default value

    # 讓s 執行 設定超時 代入 0.5
    s.settimeout(0.5)

    # 讓s 執行 綁定 代入 (本機, 0)
    s.bind(("127.0.0.1", 0))
    
    # socket地址 為 讓s 執行 取得socket名稱
    socket_address = s.getsockname()

    # 印出 socket地址
    print ("Trivial Server launched on socket: %s" %str(socket_address))

    # 無限循環
    while(1):
        # 讓s 執行 監聽 代入 1
        s.listen(1)

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 測試socket模式
    test_socket_modes()