import asyncio
import time
import pyppeteer
from cloudscraper import create_scraper

class FreeTempMail:
    """A class to interact with temporary email services."""

    def __init__(self, proxy=None):
        """Initialize with optional proxy settings."""
        self.proxy = proxy
        self.scraper = None
        self.auth_headers = None
        self.loop = asyncio.get_event_loop()
        if not isinstance(proxy, (type(None), str)):
            raise TypeError("Proxy must be a string or None")

    async def _launch_browser(self):
        """Launch a headless browser with optional proxy."""
        browser_args = {
            'headless': True,
            'args': [
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--no-first-run',
                '--no-service-autorun',
                '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'
            ]
        }

        if self.proxy:
            browser_args['args'].append(f'--proxy-server={self.proxy}')

        browser = await pyppeteer.launch(browser_args)
        return browser

    async def _get_cookie(self, browser):
        """Fetch a 'token' cookie from temp-mail.org."""
        page = await browser.newPage()
        await page.goto('https://temp-mail.org/')
        cookie = [cookie for cookie in await page.cookies() if cookie['name'] == 'token']
        await browser.close()
        if not cookie:
            raise ValueError("Could not fetch 'token' cookie")
        return cookie[0]['value']

    def _create_scraper(self, token):
        """Create a scraper instance with auth headers."""
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self.auth_headers = {'Authorization': 'Bearer ' + token}        
        self.scraper = create_scraper()

    async def generate_mail(self):
        """Generate a temporary email by launching a browser and fetching a token."""
        browser = await self._launch_browser()
        token = await self._get_cookie(browser)
        self._create_scraper(token)

    def get_email(self):
        """Fetch mailbox info."""
        if not self.auth_headers:
            raise RuntimeError("Must call generate_mail() before fetching email info")
        return self.scraper.get('https://web2.temp-mail.org/mailbox', headers=self.auth_headers).json()['mailbox']

    def get_messages(self):
        """Fetch messages in mailbox."""
        if not self.auth_headers:
            raise RuntimeError("Must call generate_mail() before fetching messages")
        return self.scraper.get('https://web2.temp-mail.org/messages', headers=self.auth_headers).json()['messages']

    def get_message(self, id):
        """Fetch a specific message by ID."""
        if not isinstance(id, str):
            raise TypeError("ID must be a string")
        if not self.auth_headers:
            raise RuntimeError("Must call generate_mail() before fetching a message")
        return self.scraper.get(f'https://web2.temp-mail.org/messages/{id}', headers=self.auth_headers).json()

    def wait_message(self):
        """Wait for a message to arrive in mailbox."""
        messages = self.get_messages()        
        while not messages:
            messages = self.get_messages()
            time.sleep(5)
        return self.get_message(messages[-1]['_id'])