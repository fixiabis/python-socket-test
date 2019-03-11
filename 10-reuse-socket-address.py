# 引入 socket
import socket

# 引入 sys
import sys

# 定義 重用socket地址 的功能
def reuse_socket_addr():
    # sock 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為序列化的連接導向位元串流
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # 舊狀態 為 讓sock 執行 取得socket選項 代入 正在使用的SOCKET socket選項, socket重用地址
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR )

    # 印出 舊狀態
    print ("Old sock state: %s" %old_state)

    # 讓sock 執行 設定socket選項 代入 正在使用的SOCKET socket選項, socket重用地址, 啟用
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    # 新狀態 為 讓sock 執行 取得socket選項 代入 正在使用的SOCKET socket選項, socket重用地址
    new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )

    # 印出 新狀態
    print ("New sock state: %s" %new_state)

    # 本地埠號 為 8282
    local_port = 8282
    
    # 伺服器 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為序列化的連接導向位元串流
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 讓伺服器 執行 設定socket選項 代入
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 讓伺服器 執行 綁定 代入 (本機位址, 0)
    srv.bind( ('', local_port) )

    # 讓伺服器 執行 監聽 1
    srv.listen(1)

    # 印出 埠號
    print ("Listening on port: %s " %local_port)

    # 無限循環
    while True:
        # 嘗試
        try:
            # 連接, 地址為 讓伺服器 接受
            connection, addr = srv.accept()
            # 印出 地址
            print ('Connected by %s:%s' % (addr[0], addr[1]))
        # 例外處理 鍵盤中斷
        except KeyboardInterrupt:
            break
        # 例外處理 socket的錯誤 為 msg
        except socket.error as msg:
            # 印出 錯誤訊息
            print ('%s' % (msg,))

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 重用socket地址
    reuse_socket_addr()