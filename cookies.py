from selenium import webdriver
import time

# Initialize the driver only once
driver = webdriver.Chrome()

# Get URL from user input
url = input("Enter the URL: ")

# Visit the website first
driver.get(url)

# Wait for the page to load (can be adjusted or replaced with WebDriverWait for dynamic pages)
time.sleep(2)

def add_cookie():
    # Adds the cookie into the current browser context
    driver.add_cookie({"name": "key", "value": "value"})
    print("Cookie added:", driver.get_cookie("key"))

def get_named_cookie():
    # Adds another cookie and then retrieves it by name
    driver.add_cookie({"name": "foo", "value": "bar"})
    print("Named cookie 'foo':", driver.get_cookie("foo"))

def get_all_cookies():
    # Adds multiple cookies and retrieves all cookies
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    print("All cookies:", driver.get_cookies())

def delete_cookie():
    # Adds cookies and deletes a specific one
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    driver.delete_cookie("test1")
    print("Cookie 'test1' deleted.")

def delete_all_cookies():
    # Adds cookies and deletes all of them
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    driver.delete_all_cookies()
    print("All cookies deleted.")

def same_side_cookie_attr():
    # Adds cookies with SameSite attribute and retrieves them
    driver.add_cookie({"name": "foo", "value": "value", "sameSite": "Strict"})
    driver.add_cookie({"name": "foo1", "value": "value", "sameSite": "Lax"})
    cookie1 = driver.get_cookie("foo")
    cookie2 = driver.get_cookie("foo1")
    print("SameSite cookie 'Strict':", cookie1)
    print("SameSite cookie 'Lax':", cookie2)

# Run functions as needed
add_cookie()
get_named_cookie()
get_all_cookies()
delete_cookie()
delete_all_cookies()
same_side_cookie_attr()

