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
    # sock 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 伺服器地址 為 (主機, 埠號)
    server_address = (host, port)

    # 印出 連接到的 port
    print ("Connecting to %s port %s" % server_address)

    # 讓sock 執行 連接 代入 伺服器地址
    sock.connect(server_address)
    
    # 嘗試
    try:
        # 訊息 為 Test message. This will be echoed
        message = "Test message. This will be echoed"

        # 印出 送出 訊息
        print ("Sending %s" % message)

        # 讓 sock 執行 送出全部 代入 讓 訊息 執行 編碼 代入 utf-8
        sock.sendall(message.encode('utf-8'))

        # 接收總數 為 0
        amount_received = 0
        # 期待總數 為 長度 代入 訊息
        amount_expected = len(message)

        # 循環 當 接收總數 < 期待總數
        while amount_received < amount_expected:
            # 資料 為 讓sock 執行 接收 代入 16
            data = sock.recv(16)
            
            # 接收總數 累加 長度 代入 資料
            amount_received += len(data)

            # 印出 接收的資料
            print ("Received: %s" % data)

    # 例外處理 socket的錯誤 為 msg
    except socket.error as e:
        # 印出 錯誤訊息
        print ("Socket error: %s" %str(e))

    # 例外處理 socket的錯誤 為 msg
    except Exception as e:
        # 印出 錯誤訊息
        print ("Other exception: %s" %str(e))

    # 測試結果
    finally:
        # 印出 結束連結訊息
        print ("Closing connection to the server")

        # 讓sock 執行 close
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