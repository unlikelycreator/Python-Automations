import random
import parser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request, urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

page = 'https://www.wallpaperflare.com/'
req = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page, 'lxml').encode("utf-8")
soup = urlopen(req).read()
for image in soup.findAll('img'):
    # print image source
    print(image['src'])
    # print alternate text
    print(image['alt'])
# downloaded = False
# while False:
no = random.randint(3, 20)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.wallpaperflare.com/")
searchbox = driver.find_element_by_xpath('//*[@id="portal_input"]')
searchbox.send_keys('Minimal wallpapers')
searchbutton = driver.find_element_by_xpath('//*[@id="portal_sub"]')
searchbutton.click()
# searchwallpaper = driver.find_element_by_xpath('//*[@id="gallery"]/li[2]/figure/a/img')
searchwallpaper = driver.find_element_by_tag_name('a')
for link in searchwallpaper:
    downloadbutton = driver.find_element_by_css_selector('img.lazy.loaded')
    downloadbutton.click()
# Set Wallpaper
# //*[@id="gallery"]/li[2]/figure/a
# gallery > li:nth-child(2) > figure > a
# gallery > li:nth-child(4) > figure > a:nth-child(7)
# gallery > li:nth-child(4) > figure > a:nth-child(7) > img
# SPI_SETDESKWALLPAPER = 20
# ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'your image path', 3)


# gallery > li:nth-child(5)
# gallery > li:nth-child(6)
# gallery > li:nth-child(7) > figure > a:nth-child(7) > img
