# Osiris
password recovery tool (class) for python
version 1.0
# Example Usage
```py
from osiris import *

class Credentials(object):
    @property
    def chrome(self):
        return getattr(self, 'credentials', Chrome().get)

    @chrome.setter
    def chrome(self, credentials):
        self.credentials = credentials
        
    @property
    def firefox(self):
        return getattr(self, 'credentials', Firefox().get)

    @firefox.setter
    def firefox(self, credentials):
        self.credentials = credentials
        
    @property
    def opera(self):
        return getattr(self, 'credentials', Chrome().get)

    @opera.setter
    def opera(self, credentials):
        self.credentials = credentials
        
c = Credentials()
chrome = c.get
firefox = c.get
opera = c.get
```
# Recovers passwords for the following browsers
* Google Chrome   > (45.0.2454)
* Mozilla Firefox > (42.0.0.5780)
* Opera           > (33.0.1990.115)
