# 用 Django 建立一個可以設定爬蟲排程任務與監控的網站

+ PyConTW 2017 Talk
+ Speaker: Yi-Chieh Chen
+ [Slider](http://chairco.github.io/2017_PyConTW_Talk/#cover)
+ [大會網站](https://tw.pycon.org/2017/events/talk/314386410792550475/)
+ [共筆內容](http://beta.hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FSJlQavv1b)
+ [錄影](https://www.youtube.com/watch?v=Ljs9e0kI7Ow)

## 範例環境設定
+ 建立 log 資料夾和 .log 檔案
    ```shell
    cd code/pycontw/
    mkdir -p logs
    cd logs
    touch django.log ghostdriver.log project.log
    ```

+ 建立環境變數 local.env, local.py
    ```shell
    cp pycontw/settings/local_sample.env pycontw/settings/local.env
    cp pycontw/settings/local_sample.py pycontw/settings/local.py
    ```

+ 設定環境變數
    在執行終端機模式執行下面指令取得 Secret_key：
    ```shell
    $ python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'
    ```
    `vim local.env` 將剛剛產生的 key 填入 SECRET_KEY= 不用加引號 ''

+ 確認 requirments.txt 內套件都安裝，執行 migrate 就完成了。
    ~因為 lazy_logger 最新版本 0.1.2 尚未上傳到 PyPi 所以請先到 lazy-logger 資料夾內 `python setup.py install` 安裝最新版本 lazy_logger~ 確認 lazy_logger 的版本是 0.1.2 萬一低於 0.1.2 版本會造成使用 @logger.patch 的 hook 回傳值是 None。
