from os import environ as env, access, sep, listdir, X_OK
from os.path import exists, normpath
from sys import platform
from time import sleep
from freetempmail.cloudscraper import create_scraper
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def getChrome():
	global version
	candidates = set()
	for item in map(
	    env.get, ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA")
	):
	    for subitem in (
	        "Google/Chrome/Application",
	        "Google/Chrome Beta/Application",
	        "Google/Chrome Canary/Application",
	    ):
	        try:
	        	candidates.add(sep.join((item, subitem, "chrome.exe")))
	        except:
	        	pass
	for candidate in candidates:
	    if exists(candidate) and access(candidate, X_OK):
	        path = normpath(candidate)
	        version = int(listdir(path.split('Application')[0] + 'Application')[0].split('.')[0])
	        return path

def generateMail(ver=None):
	global authHeaders, s
	options = ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox')
	options.add_argument('--no-first-run')
	options.add_argument('--no-service-autorun')
	if 'win' in platform:
		options.binary_location = getChrome()
		ver = version
	driver = Chrome(options=options, version_main=ver)
	driver.get('https://temp-mail.org/')
	for cookie in driver.get_cookies():
		if cookie['name'] == 'token':
			driver.quit()
			authHeaders = {'Authorization': 'Bearer ' + cookie['value']}
			s = create_scraper()

def getEmail():
	return s.get('https://web2.temp-mail.org/mailbox', headers=authHeaders).json()['mailbox']

def getMessages():
	return s.get('https://web2.temp-mail.org/messages', headers=authHeaders).json()['messages']

def getMessage(id):
	return s.get(f'https://web2.temp-mail.org/messages/{id}', headers=authHeaders).json()

def waitMessage():
	messages = getMessages()
	i = len(messages)
	while len(messages) <= i:
		messages = getMessages()
		sleep(5)
	return getMessage(messages[i]['_id'])