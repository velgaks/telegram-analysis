from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
import pickle

foldertosavecookie="S:\\Users\Oleh\..."
options = Options()
options.add_argument("--no-sandbox")
dr = webdriver.Chrome('C:\\pathtodriver\chromedriver.exe',
                      options=options)
dr.get("https://yoursiteforlogin.com")
# Do all login stuff manually.
# Then:
with open(os.path.join(foldertosavecookie,"CookesFilename.pkl"), "wb") as cook:
    pickle.dump(dr.get_cookies(), cook)
dr.quit()