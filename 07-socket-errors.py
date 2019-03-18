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
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
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
        # s 為 從socket中 建立 socket 代入 設定domain為IPV4協定, type為TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 例外處理 socket錯誤 為 e
    except socket.error as e:
        # 印出 錯誤訊息
        print("Error creating socket: %s" % e)

        # 讓sys 執行 離開 代入 1
        sys.exit(1)

    # 測試
    try:
        # 從s中 連接 
        s.connect((host, port))

    # 例外處理 socket的gai錯誤 為 e
    except socket.gaierror as e:
        # 印出 錯誤訊息
        print("Address-related error connecting to server: %s" % e)

        # 讓sys 執行 離開 代入 1
        sys.exit(1)
        
    # 例外處理 socket的錯誤 為 e
    except socket.error as e:
        # 印出 錯誤訊息
        print("Connection error: %s" % e)

        # 讓sys 執行 離開 代入 1
        sys.exit(1)
    
    # 測試
    try:
        # 訊息 為 GET 請求 檔案
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        
        # 讓s 執行 送出全部 代入 讓訊息 編碼 代入 utf-8
        s.sendall(msg.encode('utf-8'))
    
    # 例外處理 socket的錯誤 為 e
    except socket.error as e:
        # 印出 錯誤訊息
        print("Error sending data: %s" % e)
        
        # 讓sys 執行 離開 代入 1
        sys.exit(1)


    # 無限循環
    while 1:
        # 測試
        try:
            # 緩衝 為 讓s 執行 接收 代入 2048
            buf = s.recv(2048)
        
        # 例外處理 socket的錯誤 為 e
        except socket.error as e:
            # 印出 錯誤訊息
            print("Error receiving data: %s" % e)
            
            # 讓sys 執行 離開 代入 1
            sys.exit(1)

        # 若 沒有 緩衝 長度
        if not len(buf):
            # 離開循環
            break
        
        # 讓sys的stdout 執行 寫出 緩衝 解碼 utf-8
        sys.stdout.write(buf.decode('utf-8'))


# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 主程式
    main()
