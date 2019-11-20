import unittest
from selenium import webdriver
class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit() 
    
    def test_home_page(self):
        # User hears about the blog app and visits        
        self.browser.get('http://127.0.0.1:8000/blog')

        # She sees the title and header mention to-do list        
        self.assertIn('Blog', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Blogss   ', header.text)


        # She 



if __name__ == "__main__":
    unittest.main()