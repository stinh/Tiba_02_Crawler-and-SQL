from bs4 import BeautifulSoup
import requests, os, time

key_word = input("請輸入要下載的圖片：")
url = 'https://www.google.com.tw/search?q='+key_word+' &rlz=1C1CAFB_enTW617TW621&source=lnms&tbm=isch&sa=X&ved=0ahUKEwienc6V1oLcAhVN-WEKHdD_B3EQ_AUICigB&biw=1128&bih=863'
photolimit = 10
header = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers = header)
soup = BeautifulSoup(response.content, 'html.parser')
# soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all('img')
folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在
    os.makedirs(folder_path)

for index , item in enumerate (results):

    if (item and index < photolimit ):
        html = requests.get(item.get('src'))
        img_name = folder_path + str(index + 1) + '.png'

        with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入
            file.write(html.content)
            file.flush()
        file.close()
        print('第 %d 張' % (index + 1))
        time.sleep(1)

print('Done')

'''
results = soup.find_all("img", {"class": "_2VWD4 _2zEKz"}, limit=5)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結

for index, link in enumerate(image_links):
    if not os.path.exists("images"):
        os.mkdir("images")  # 建立資料夾

    img = requests.get(link)  # 下載圖片

    with open("images\\" + input_image + str(index + 1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼
'''
