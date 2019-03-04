# 引入 socket
import socket

# 定義 印出遠端機器資訊 的功能 需要 遠端主機名稱


def get_remote_machine_info(remote_host):
    # 嘗試
    try:
        # 印出
        print(
            # 主機名稱與IP位址
            "IP address of %s: %s"
            % (remote_host, socket.gethostbyname(remote_host))
        )

    # 例外處理 socket錯誤
    except socket.error as err_msg:
        # 印出 遠端主機名稱與錯誤訊息
        print("%s: %s" % (remote_host, err_msg))


# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 印出 遠端機器資訊 代入 'www.python.org'
    get_remote_machine_info('www.python.org')
