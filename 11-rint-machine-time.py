# 引入 ntplib
import ntplib

# 由 time 引入 ctime
from time import ctime

# 定義 印出時間 的功能
def print_time():
    # ntp用戶端 為 讓ntplib 建立 NTP用戶端
    ntp_client = ntplib.NTPClient()

    # 回應 為 讓ntp用戶端 執行 請求 代入 watch.stdtime.gov.tw
    response = ntp_client.request('watch.stdtime.gov.tw')

    # 印出 時間
    print (ctime(response.tx_time))

# 若 該檔案 為 主程式 時
if __name__ == '__main__':
    # 執行 印出時間
    print_time()