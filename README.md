# Osiris
EN-US: Password recovery tool (class) for python
EN-US: Version 1.0

PT-BR: Aplicação (classe) de recuperação de senhas
PT-BR: Versão 1.0
# Example usage / Exemplo de usagem
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
        return getattr(self, 'credentials', Opera().get)

    @opera.setter
    def opera(self, credentials):
        self.credentials = credentials
        
c = Credentials()
chrome = c.get
firefox = c.get
opera = c.get
```
# Working on these browsers / Funcionandos nesses navegadores
* Google Chrome   > (45.0.2454)
* Mozilla Firefox > (42.0.0.5780)
* Opera           > (33.0.1990.115)
