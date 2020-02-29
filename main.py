# 网易云音乐下载器 v0.1
import os
from urllib.request import urlretrieve
from selenium import webdriver

def get_music_name():
    print("Enter the name of the song what you need to download.")
    name = input()
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
    path = 'music/{}.mp3'.format(song_name)
    print('歌曲: {} 正在下载.'.format(song_name))
    urlretrieve(song_url, path, download_speed)
    print('歌曲: {} 下载完成.'.format(song_name))

def download_speed(a, b, c):
    per = 100.0 * a * b / c
    if per > 100.0:
        per = 100.0
    print('%.2f%%' % per)

get_music_name()
