# Osiris
EN-US:
Password recovery tool (class) for python
 / Version 1.0


PT-BR:
Aplicação (classe) de recuperação de senhas
 / Versão 1.0
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
chrome = c.chrome
firefox = c.firefox
opera = c.opera

print("Chrome: " + str(chrome))
print("Firefox: " + str(firefox))
print("Opera: " + str(opera))
```
# Warning / Aviso
EN-US:
Osiris is still in version 1.0 so it may contain some bugs, please be patient.


PT-BR:
O Osiris ainda está na versão 1.0 então pode conter alguns bugs, por favor tenha paciência.
# Working on these browsers / Funcionandos nesses navegadores
* Google Chrome   > 45.0.x
* Mozilla Firefox > 42.0.0.x
* Opera           > 33.0.1990.x
