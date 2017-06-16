# 用 Django 建立一個可以設定爬蟲排程任務與監控的網站

+ PyConTW 2017 Talk
+ Speaker: Yi-Chieh Chen
+ [Slider](https://chairco.github.io/2017Talk-Django-crawler-monitor/#about-me)
+ [大會網站](https://tw.pycon.org/2017/events/talk/314386410792550475/)
+ [共筆內容](http://beta.hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FSJlQavv1b)

## 範例環境設定
+ 建立環境變數 local.env
```shell
cp pycontw\pycontw\settings\local_sample.env pycontw\pycontw\settings\local.env
```
+ 設定環境變數
在執行終端機模式執行下面指令取得 Secret_key：
```shell
$ python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'']'
```
`vim local.env` 將剛剛產生的 key 填入 SECRET_KEY= 不用加引號 ''

+ 確認 requirments.txt 內套件都安裝，執行 migrate 就完成了。


## 講題摘要
一位小工程師，經常需要取得客戶資料又遭遇客戶不開放 API 接口來取得資料。為此經常需要撰寫爬蟲程式爬資料。但爬蟲任務變多時管理變得複雜，早期會透過 Linux crontab 設定時刻表來安排爬蟲任務，卻容易出現各種例外，例如：透過 selenium 來爬網頁可能因為不可預期使得瀏覽器 driver 沒有被正常關閉的錯誤，進而可能產生非常多死掉的 processes 得經常做各種錯誤檢查（不管透過自動化程式或是人工）。幾次因為不同的錯誤原因造成無法正常取得資料加上工程師講求效率不愛人工檢查（懶惰）的性格因而萌生開發念頭。
網站主要透過 Django, Django-Q 與 ORM(Broker 也可選擇 redis 等)作為架構。會透過案例分享撰寫一個可以被設定與監控的 task（任務），會包含任務的流程並將產生出序列的 log 紀錄。透過 Django‘s Admin 後台管理介面去設定 Django-Q 並建立的任務排程。最後則會展示前端介面設計，讓管理者透過序列的 log 快速地瀏覽歷程紀錄以及發生錯誤時的訊息與狀態。
雖然曾經聽過其他人分享透過 Luigi 或是 Airflow 來處理排程任務。但本篇希望結合 Django 來作為框架但會討論比較。
聆聽這個演講需要一點 Django 的背景知識以及撰寫過爬蟲經驗。


## 目的
本次演講希望提供給經常撰寫 Python 爬蟲需要定時爬資料卻又想要透過一個簡單方式管理任務的夥伴。
這個演講之後您將知道怎麼透過 Django 建立一個 UI 介面方便你去建立多個任務與監控這些任務的狀態，最後透過作者觀點去了解目前協助任務排程的工具（Django-Q），作為您選擇建置的參考（或許可以協助您省去比較時間）。


## 詳細內容
這個演講會提及 Django-Q 這個用於 Django 任務管理套件。並且撰寫一個運作在上面的 task。將會提到幾個有趣的經驗：

+ 快速整合 job script(crawler flow) 進入 Django-Q 建構的任務管理內。
通常在撰寫爬蟲時都是一段 job script，將會分享如何將每個爬蟲改變成類似 Django 內的 app，這樣就能快速套入 Django-Q 的任務。
+ tasks 的流程如何紀錄
因為爬蟲程式的訊息會採用 logging 的方式產生，是一個 stdout 的訊息，將告訴大家怎麼把這份訊息擷取並且記錄。
+ lazy_logger 套件分享
呈上，這是一個 2016 年 pycontw sprint 活動開發的套件，將會接續介紹如何用這個套件簡化 logging 訊息的產生與紀錄。
+ Django 後台排程與前端介面
當一個 task 順利建立且可以成功運作、產生紀錄與儲存後將介紹如何透過 Django-Admin 後台設定排程與設計一個前端監控介面的頁面。


## 時間規劃
0. 簡單比較目前較為流行的排程任務工具或框架 [2 min]
1. Django 與 Django-Q 介紹與設定 [5 min]
2. 爬蟲程式範例 [5 min]
    * stdout 我們想知道訊息
    * 回傳格式設計
4. Tasks 程式範例 [5 min]
    * 如何擷取 stdout 訊息並且記錄
5. Django 前端設計 (view) [6 min]
    * 如何擷取 Django-Q 正在運行任務
    * 如何擷取 Django-Q 已經完成任務
    * 設計 一個 template 頁面 
6. Django admin 建立一個任務 [1 min]
7. Demo [3 min]
