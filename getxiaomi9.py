from selenium import webdriver
import time


class xiaomi():
    lurl = 'https://account.xiaomi.com/'
    burl = 'https://item.mi.com/product/10000134.html'
    atime = 1552960800

    #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def isElementExist(self,element):
        flag=True
        browser=self.b
        try:
            browser.find_element_by_css_selector(element)
            return flag

        except:
            flag=False
            return flag

    def __init__(self, usernme, pwd):
        self.username = usernme
        self.pwd = pwd
        self.b = webdriver.Firefox(executable_path='./geckodriver')

    def login(self):
        print('正在登陆...\n')
        self.b.get(self.lurl)
        self.b.find_element_by_id('username').send_keys(self.username)
        self.b.find_element_by_id('pwd').send_keys(self.pwd)
        self.b.find_element_by_id('login-button').click()

    def check_phone(self):
        time.sleep(1.5)
        sreach_window=self.b.current_window_handle
        if self.isElementExist('.btn_tip.btn_commom.verify-sendbtn'):
            self.b.find_element_by_css_selector('.btn_tip.btn_commom.verify-sendbtn').click()
            sms_code = input('code：\n')
            self.b.find_element_by_name("ticket").send_keys(sms_code)
            self.b.find_element_by_css_selector('.btn_tip.btn_commom.btn-submit').click()

    def buy(self):
        print('进入米9秒杀页面...\n')
        self.b.get(self.burl)
        print('正在选择型号配件...\n')
        self.b.find_element_by_xpath('//*[@id="J_list"]/div[1]/ul/li[2]').click()
        self.b.find_element_by_xpath('//*[@id="J_list"]/div[2]/ul/li[2]').click()
        self.b.find_element_by_xpath('//*[@id="J_list"]/div[3]/ul/li[1]').click()

        try:
            self.b.find_element_by_xpath('//*[@id="J_buyBox"]/div/div[1]/div/a[1]').click()
            self.b.find_element_by_xpath('//*[@id="J_agreeModal"]/div[3]/div/button[2]').click()
            time.sleep(3)
            self.b.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li[1]').click()
        except:
            pass

        while True:
            if time.time() > self.atime:
                try:
                    self.b.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li[1]').click()
                    print('开始抢购...\n')
                except:
                    print('异常，退出抢购')
                    break
            else:
                print('\n\n', '还未到达抢购时间\n', '当前时间是：', time.time(), '\n', '抢购时间是：', self.atime, '\n\n')


if __name__ == '__main__':
    username = input('username：\n')
    pwd = input('pwd：\n')

    a = xiaomi(usernme=username, pwd=pwd)
    a.login()
    a.check_phone()
    a.buy()
