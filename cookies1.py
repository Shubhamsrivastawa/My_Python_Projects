from selenium import webdriver
import pandas as pd
import time

# Initialize the driver only once
driver = webdriver.Chrome()

# Get URL from user input
url = input("Enter the URL: ")

# Visit the website first
driver.get(url)

# Wait for the page to load (can be adjusted or replaced with WebDriverWait for dynamic pages)
time.sleep(2)

# Function to add cookies and retrieve them
def get_all_cookies():
    # Adds multiple cookies
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    
    # Retrieve all cookies from the browser
    cookies = driver.get_cookies()
    return cookies  # Return the cookies

def same_side_cookie_attr():
    # Adds cookies with SameSite attribute
    driver.add_cookie({"name": "foo", "value": "value", "sameSite": "Strict"})
    driver.add_cookie({"name": "foo1", "value": "value", "sameSite": "Lax"})
    
    # Retrieve specific cookies
    cookie1 = driver.get_cookie("foo")
    cookie2 = driver.get_cookie("foo1")
    
    # Print the cookies (or you can return them)
    print("SameSite cookie 'Strict':", cookie1)
    print("SameSite cookie 'Lax':", cookie2)
    
    # Returning the cookies as a list
    return [cookie1, cookie2]

# Collect all cookies and store in a DataFrame
all_cookies = get_all_cookies()
df_cookies = pd.DataFrame(all_cookies)

# Display the cookies in DataFrame format
print("\nAll Cookies DataFrame:")
print(df_cookies)

# Collect cookies with SameSite attribute and store in a DataFrame
same_site_cookies = same_side_cookie_attr()
df_same_site_cookies = pd.DataFrame(same_site_cookies)

# Display the SameSite cookies in DataFrame format
print("\nSameSite Cookies DataFrame:")
print(df_same_site_cookies)


