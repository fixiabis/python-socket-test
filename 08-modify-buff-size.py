# 引入 socket
import socket

# 設定 發送緩衝大小
SEND_BUF_SIZE = 4096

# 設定 接收緩衝大小
RECV_BUF_SIZE = 4096

# 定義 變更緩衝大小 的功能
def modify_buff_size():
    # sock 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為TCP
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    
    # 緩衝大小為 讓sock 執行 取得socket選項 代入 正在使用的socket選項, socket發送緩衝大小
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    # 印出 緩衝大小
    print ("Buffer size [Before]:%d" %bufsize)

    # 讓sock 執行 設定socket選項 代入 正在使用的TCP socket選項, TCP無延遲, 是
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)

    # 讓sock 執行 設定socket選項 代入 正在使用的SOCKET socket選項, socket發送緩衝大小, 為發送緩衝大小
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE
    )

    # 讓sock 執行 設定socket選項 代入 正在使用的SOCKET socket選項, socket接收緩衝大小, 為接收緩衝大小
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )

    # 緩衝大小為 讓sock 執行 取得socket選項 代入 正在使用的socket選項, socket發送緩衝大小
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    # 印出 緩衝大小
    print ("Buffer size [After]:%d" %bufsize)

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 變更緩衝大小
    modify_buff_size()