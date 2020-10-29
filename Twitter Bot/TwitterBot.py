from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import tkinter as tk
#root = tk.Tk()
#canvas1 = tk.Canvas(root, width = 400, height = 300)
#canvas1.pack()
#entry1 = tk.Entry (root)
#canvas1.create_window(200, 140, window=entry1)

class TwitterBot:
    def __init__(self, username, password, ):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        # password.send_keys(keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        #hashtag = entry1.get()
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=tycd')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            #tweet = bot.find_element_by_class_name('css-1dbjc4n')
            #links = [elem.get_attribute('data-permalink-path') for elem in tweet]
            #print(links)

            tweetLinks = [i.get_attribute('href')
                          for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep(30)

            #for link in filteredLinks:

                #bot.get('https://twitter.com/' + link)
                #try:
                    #bot.find_element_by_class_name('HeartAnimation').click()
                    #time.sleep(5)
                #except Exception:
                    #time.sleep(60)
    #button1 = tk.Button(text='Get the Square Root', command=login)
    #canvas1.create_window(200, 180, window=button1)
   # root.mainloop()

hritik = TwitterBot('iamhritikpawar', 'pawar2700')
hritik.login()
hritik.like_tweet('python')

