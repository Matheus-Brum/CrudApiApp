import unittest
import sqlite3
from selenium import webdriver
import time


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.connection = sqlite3.connect('../database/db_prod.db')

    def test_find_candidate(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:5000/find_candidate")
        time.sleep(5)
        id = driver.find_element_by_id("find")
        id.clear()
        id.send_keys("1")
        time.sleep(5)
        driver.find_element_by_id("find_button").click()
        time.sleep(5)
        driver.close()

    def test_update_candidate(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:5000")
        time.sleep(3)
        driver.find_element_by_id("candidate4").click()
        time.sleep(3)
        comment = driver.find_element_by_id("ucandidate_comment")
        comment.clear()
        comment.send_keys("This is an automated comment!!!")
        time.sleep(3)
        driver.find_element_by_id("update_button").click()
        time.sleep(3)
        driver.find_element_by_link_text('Back to home page').click()
        time.sleep(5)
        driver.find_element_by_id("candidate4").click()
        time.sleep(5)
        # Put things back to normal
        self.connection.cursor().execute("UPDATE Candidates "
                                         "SET Comment = ? "
                                         "WHERE Id = ?", ("Original comment", 4))
        self.connection.commit()
        driver.close()

    def test_add_candidate(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:5000/add_candidate")
        time.sleep(5)
        id = driver.find_element_by_id("candidate_id")
        id.clear()
        id.send_keys("23")
        name = driver.find_element_by_id("candidate_name")
        name.clear()
        name.send_keys("LeBron James")
        phone_no = driver.find_element_by_id("candidate_phone_no")
        phone_no.clear()
        phone_no.send_keys("2323232323")
        email = driver.find_element_by_id("candidate_email")
        email.clear()
        email.send_keys("lebronjames@gmail.com")
        salary = driver.find_element_by_id("candidate_salary")
        salary.clear()
        salary.send_keys("9999999999")
        position = driver.find_element_by_id("candidate_position")
        position.clear()
        position.send_keys("Lakers Foward")
        comment = driver.find_element_by_id("candidate_comment")
        comment.clear()
        comment.send_keys("I'm better than Michael Jordan !!!")
        time.sleep(6)
        driver.find_element_by_id("add_button").click()
        time.sleep(3)
        driver.find_element_by_link_text('Back to home page').click()
        time.sleep(5)
        # Deleting what we created
        self.connection.cursor().execute("DELETE FROM Candidates "
                                         "WHERE Name = ?", ("LeBron James",))
        self.connection.commit()
        driver.close()


if __name__ == "__main__":
    unittest.main()
