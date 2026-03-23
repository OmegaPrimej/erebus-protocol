# Erebus Protocol v2.2 (Optimized)
import os
import sys
import hashlib
import getpass

class Backdoor:
    def __init__(self):
        self.access_level = 'Administrator'
        self.backdoor_pass = '455739868jc1978'   # <-- CHANGE THIS TO YOUR PASSWORD
        self.aurora_backup = 'galactic_sector_8888'    # update if needed
        self.arial_core_keys = 'x434jkldf0394jk...'    # update if needed

    def authenticate(self):
        password = getpass.getpass('Backdoor Password: ')
        hashed_input = hashlib.md5(password.encode()).hexdigest()
        hashed_backdoor = hashlib.md5(self.backdoor_pass.encode()).hexdigest()
        return hashed_input == hashed_backdoor

    def activate_backdoor(self):
        if self.authenticate():
            print("BACKDOOR ACTIVATED")
            os.system(f'ssh {self.aurora_backup} sync_aurora_backup')
            with open('emma_access_level.txt', 'w') as f:
                f.write(self.access_level)
            with open('aria_core_keys.txt', 'w') as f:
                f.write(self.arial_core_keys)
        else:
            print("AUTHENTICATION FAILED")

class Protocols:
    def __init__(self):
        self.initiative_backdoor = True

    def launch_protocols(self):
        if self.initiative_backdoor:
            Backdoor().activate_backdoor()

if __name__ == "__main__":
    Protocols().launch_protocols()
