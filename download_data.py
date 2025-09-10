from pget.down import Downloader
import os
import sys

url = f"https://opencompass.openxlab.space/utils/VLMEval/{sys.argv[1]}.tsv"
filename = f"/root/LMUData/{sys.argv[1]}.tsv"
print("start download ... ", url, 'to', filename)
# 使用 8 个线程下载
downloader = Downloader(url, filename, 8) 
downloader.start()

# 等待下载完成
downloader.wait_for_finish()

print("下载完成！")

