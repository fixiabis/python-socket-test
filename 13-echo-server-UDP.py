# 引入 socket
import socket
# 引入 sys
import sys
# 引入 argparse
import argparse


# 主機 為 localhost
host = 'localhost'
# 資料負載 為 2048
data_payload = 2048
# 備份紀錄 為 5
backlog = 5 

# 定義 迴響server端 需要 埠號
def echo_server(port):
    # sock 為 讓socket 建立 socket 代入 設定domain為IPV4協定, type為TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 舊狀態 為 讓sock 執行 取得socket選項 代入 正在使用的SOCKET socket選項, socket重用地址
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 伺服器地址 為 (主機, 埠號)
    server_address = (host, port)

    # 印出 連接到的 port
    print ("Starting up echo server  on %s port %s" % server_address)

    # 讓socket 執行 綁定 代入 伺服器地址
    sock.bind(server_address)
    
    # 讓socket 執行 監聽 代入 備份紀錄
    sock.listen(backlog)

    # 無限循環
    while True: 
        # 印出 等待接收訊息
        print ("Waiting to receive message from client")

        # client, 地址為 讓伺服器 接受
        client, address = sock.accept() 

        # 資料 為 讓client 接收 代入 資料負載
        data = client.recv(data_payload)

        # 若 有資料
        if data:
            # 印出 資料
            print ("Data: %s" %data)
            # 讓client 執行 送出 代入 資料
            client.send(data)

            # 印出 送出 訊息
            print ("sent %s bytes back to %s" % (data, address))

        # 讓client 執行 關閉
        client.close() 

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

    # 執行 迴響server端 代入 埠號
    echo_server(port)