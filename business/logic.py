import os
from dotenv import load_dotenv

load_dotenv()

def checkUserPass(user,pwd):
    if user == "gferrari" and pwd == os.getenv("PWD"):
        return True
    else:
        return False