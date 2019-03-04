# 引入 sys
import sys
# 引入 socket
import socket
# 引入 argparse
import argparse

# 定義 主程式 的功能


def main():
    # 解析器 為 從argparse中 建立參數解析器
    parser = argparse.ArgumentParser(description='Socket Error Examples')

    # 從解析器中 增加參數
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)

    # 獲得參數 為 從解析器中 解析參數
    given_args = parser.parse_args()

    # 主機 為 獲得參數 的 主機
    host = given_args.host

    # 埠號 為 獲得參數 的 埠號
    port = given_args.port

    # 檔名 為 獲得參數 的 檔案
    filename = given_args.file

    # 測試
    try:
        # s 為 從socket中 建立 socket 代入 設定domain為IPV4協定, type為序列化的連接導向位元串流
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 例外處理 socket錯誤
    except socket.error as e:
        # 印出錯誤訊息
        print("Error creating socket: %s" % e)
        sys.exit(1)

    # 測試
    try:
        # 從s中 連接 
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while 1:
        # Fourth tr-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf.decode('utf-8'))


# 若該檔案作為主程式時
if __name__ == '__main__':
    # 執行主程式
    main()
