from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager



class SelectionOfRows(unittest.TestCase):
     def  test_to_find_row_of_siblings(self):
          driver = webdriver.Chrome(ChromeDriverManager().install())
          driver.get("http://the-internet.herokuapp.com/large")
          selecting_class= driver.find_element_by_class_name("example")
          selecting_tag= selecting_class.find_elements_by_tag_name("h4")
          self.assertEqual(selecting_tag[1].text, 'Siblings') 
    
     def  test_to_find_given_row2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://the-internet.herokuapp.com/large")
        find_row= driver.find_element_by_id("sibling-1.3")
        self.assertEqual(find_row.text, '1.3') 
    
     def  test_to_find_given_row3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://the-internet.herokuapp.com/large")
        find_row= driver.find_element_by_id("sibling-13.2")
        self.assertEqual(find_row.text, '13.2') 

if __name__ == '__main__':
    unittest.main()   



