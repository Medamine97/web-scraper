from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import pandas as pd
import os
import re
import random
import string

#URL

url_= "https://bl.ocks.org/alfmoh"



def getPassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))
#import list 
mylist=[]
data_file = 'url_des_présentation_final.xlsx'
df = pd.read_excel(data_file)
mylist = df["Url"].tolist()

path_chromedriver ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"

#test
mylist_test = mylist[920:975]
#the chromedriver path

# Au cas il ya une duplication entre deux noms de blog du meme auteur
def getPassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))

##for --------------------------


j=1
limit=0
list_length=len(mylist_test)

for url in mylist_test:
    print(url)
    j +=1
    print(j)
    #url = "http://bl.ocks.org/maptastik/c30137e4e8663debbf9987a40e8e62dc"
    cutting_url = re.split('http://bl.ocks.org/|/',url)
    driver = webdriver.Chrome(path_chromedriver)
    driver.get(url)
    owner = cutting_url[1]
    description= driver.title
    #description = description.replace(" " , '_')
    description = re.sub('[^a-zA-Z0-9 \n\.]', '', description)
    description = description.replace('  bl.ocks.org', '')
    sub_dir = "./data_collected/" + owner +"/"+description
    if os.path.exists(sub_dir):
        sub_dir = "./data_collected/" + owner +"/"+description+"---"+ getPassword(3)

    os.makedirs( sub_dir )

    #print('***get code source*********************')
    #print(driver.page_source)

    try:
        main = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"gist-sources"))
            )
        headers = main.find_elements_by_tag_name("h2")
        codes = main.find_elements_by_tag_name("code")

        for i in range(0 ,len(codes)):
            header =headers[i].text
            header = header.replace("\n#", '')            
            code =codes[i].text
            text_file_name = header
            #text_file = open(text_file_name, "wt")
            #n = text_file.write(code)
            #text_file.close()
            path = sub_dir
            if not os.path.exists(path):
                os.makedirs(path)
            filename =text_file_name
            with open(os.path.join(path, filename), 'wt') as temp_file:
                temp_file.write(code)
    except:
        pass
    finally:
        driver.quit()

