from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class TestCaseTaoKipThi(unittest.TestCase):

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
        driver.find_element_by_xpath("//span[contains(.,'Phiên bản trường')]").click()

    def test_3_Danhsachkipthi(self):
        driver = self.driver
        time.sleep(0.5)
        driver.find_element_by_xpath("//li[6]/div").click()
        # lỗi cần sửa vì lúc nào cũng bị nhảy menu
        driver.find_element_by_xpath("//a[contains(text(),'Danh sách kíp thi')]").click()
        a = driver.find_element_by_xpath("//*[@id='root']/section/section/main/div[2]/div/div/div/div/h3").text
        print(a)

    def test_4_TaoKipThi(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='root']/section/section/main/div[2]/div/div/div/div/h3/a").click()
        driver.find_element_by_xpath("//*[@id='text-input']").click()
        driver.find_element_by_xpath("//*[@id='text-input']").send_keys("python auto test")
        driver.find_element_by_xpath("//div[@id='react-select-2--value']/div").click()
        time.sleep(0.3)
        driver.find_element_by_xpath("//div[@id='react-select-2--value']/div/input").send_keys("FFDQHU - Gói đề test -Auto - vui lòng không sử dụng")
        driver.find_element_by_xpath("//div[@id='react-select-2--value']/div/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[@id='react-select-3--value']/div").click()
        time.sleep(0.3)
        driver.find_element_by_xpath("//div[@id='react-select-3--value']/div/input").send_keys("Lớp test _auto_Vui long không sử dụng")
        driver.find_element_by_xpath("//div[@id='react-select-3--value']/div/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='root']/section/section/main/div[2]/div/div/div/div/form/div[8]/div[2]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[@id='root']/section/section/main/div[2]/div/div/div/div/form/div[8]/div[2]/textarea").send_keys("testok")
        # thời gian hoạt động của kíp thi không cần chỉnh sửa vì tự động điền thông tin
        driver.find_element_by_name("time_limit").click()
        driver.find_element_by_name("time_limit").clear()
        driver.find_element_by_name("time_limit").send_keys("60")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_xpath("/html/body/div[2]/section/section/main/div[2]/div/div/div/div/form/div[19]/div/button").click()


    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")