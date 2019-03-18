# 引入 socket
import socket
# 引入 sys
import sys
# 引入 argparse
import argparse

# 主機 為 localhost
host = 'localhost'

# 定義 迴響client端 需要 埠號
def echo_client(port):
    # sock 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 伺服器地址 為 (主機, 埠號)
    server_address = (host, port)

    # 印出 連接到的 port
    print ("Connecting to %s port %s" % server_address)
    message = 'This is the message.  It will be repeated.'

    # 嘗試
    try:
        # 訊息 為 Test message. This will be echoed
        message = "Test message. This will be echoed"

        # 印出 送出 訊息
        print ("Sending %s" % message)

        # 送出 為 讓sock 執行 送去 代入 訊息 執行 編碼 utf-8, 伺服器地址
        sent = sock.sendto(message.encode('utf-8'), server_address)

        # 資料, 伺服器 為 
        data, server = sock.recvfrom(data_payload)
        print ("received %s" % data)

    finally:
        print ("Closing connection to the server")
        sock.close()

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 解析器 為 從argparse中 建立參數解析器
    parser = argparse.ArgumentParser(description='Socket Server Example')
    
    # 從解析器中 增加參數
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)

    # 被給予的參數 為 讓解析器 執行 解析參數
    given_args = parser.parse_args() 

    # 埠號 為 被給予的參數 的 埠號
    port = given_args.port

    # 執行 迴響client端 代入 埠號
    echo_client(port)