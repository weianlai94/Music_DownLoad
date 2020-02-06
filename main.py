# 网易云音乐下载器 v0.1
import os
from urllib.request import urlretrieve
from tkinter import *
from requests import *
from selenium import webdriver

def get_music_name():
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
    print(a_id)
    song_id = a_id.split('=')[-1]
    print(song_id)
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute("title")
    print(song_name)
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name
    driver.quit()
    song_load(item)

def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    os.makedirs('music', exist_ok=True)
    path = 'music\{}.mp3'.format(song_name)
    text.insert(END, '歌曲: {},正在下载...'.format(song_name))
    text.see(END)
    text.update()
    urlretrieve(song_url, path)
    text.insert(END, '下载完毕: {}.'.format(song_name))
    text.see(END)
    text.update()

root = Tk()
root.title('网易云音乐下载器v0.1')
root.geometry('840x420')
# 标签控件
label = Label(root, text='请输入歌曲名称(不支持VIP歌曲):', font=('宋体', 20))
# 标签定位
label.grid()
# 输入框
entry = Entry(root, font=('宋体', 20), width=25)
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=('宋体', 16), width=75, heigh=15)
text.grid(row=1, columnspan=2)
# 开始按钮
button = Button(root, text='开始下载', font=('宋体', 15), command=get_music_name)
button.grid(row=2, column=0, sticky=W)
# 退出按钮
button1 = Button(root, text='退出程序', font=('宋体', 15), command=root.quit)
button1.grid(row=2, column=1, sticky=E)
root.mainloop()
