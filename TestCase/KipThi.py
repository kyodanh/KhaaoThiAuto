from selenium import webdriver
import unittest
import time

class TestCaseKipThi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\pythonProject\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_OpenWeb(self):
        driver = self.driver
        driver.get("https://a.khaothi.online/login")  # openwweb
        driver.set_page_load_timeout(20)
        time.sleep(0.3)

    def test_2_Login(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='basic_email']").click()
        driver.find_element_by_xpath("//*[@id='basic_email']").send_keys("fis@xcbt.online")
        driver.find_element_by_xpath("//*[@id='basic_password']").click()
        driver.find_element_by_xpath("//*[@id='basic_password']").send_keys("Abc@123")
        driver.find_element_by_xpath("//*[@id='basic']/div[3]/div/div/div/button").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/button[1]").click()

    def test_3_Danhsachkipthi(self):
        driver = self.driver
        driver.find_element_by_xpath("//li[6]/div").click()
        # time.sleep(0.5)
        driver.find_element_by_xpath("//a[contains(text(),'Danh sách kíp thi')]").click()










    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")