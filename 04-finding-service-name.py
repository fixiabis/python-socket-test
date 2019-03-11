# 引入 socket
import socket

# 定義 尋找服務名稱 的功能
def find_service_name():
    # 協定名稱 為 TCP
    protocol_name = 'tcp'

    # 埠號 取得自 [80, 25]
    for port in [80, 25]:
        # 印出 埠號與服務名稱
        print(
            "Port: %s => service name: %s"
            % (port, socket.getservbyport(port, protocol_name))
        )

    # 埠號 為 53
    port = 53

    # 協定名稱 為 UDP
    protocol_name = 'udp'

    # 印出 埠號與服務名稱
    print(
        "Port: %s => service name: %s"
        % (port, socket.getservbyport(port, protocol_name))
    )

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 尋找服務名稱
    find_service_name()
