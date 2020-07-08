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



#import list 
mylist=[]
data_file = ("./data_type.xlsx")
df = pd.read_excel(data_file)
mylist = df["Url"].tolist()
print(len(mylist))
'''
listofzeros = [0] * len(mylist)

df['nb des fichiers csv '] =listofzeros
df['nb des fichiers json '] =listofzeros
df['nb des fichiers JavaScript '] =listofzeros
df['nb des fichiers html '] =listofzeros
df['nb des fichiers css '] =listofzeros
df['nb total des fichiers '] =listofzeros '''

#df[1]['nb des fichiers csv '] = 10
#df.set_value('1', 'nb des fichiers csv ', 10)
#df.at['1', 'nb des fichiers csv '] = 10



path_chromedriver ="C:/Users/benfa/OneDrive/Bureau/web Scraping/chromedriver.exe"

#test
start=801 
end = 1601
mylist_test = mylist[start:end]
#the chromedriver path

# Au cas il ya une duplication entre deux noms de blog du meme auteur
def getPassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))

##for --------------------------


j=0
limit=0



for indice_url  in range (start,end):
    print(mylist_test[j])
    
    driver = webdriver.Chrome(path_chromedriver)
    driver.get(mylist_test[j])  
    j +=1
    print(j)


    try:
        main = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"gist-sources"))
            )
        headers = main.find_elements_by_tag_name("h2")
        codes = main.find_elements_by_tag_name("code")
        nb_csv = 0 
        nb_json = 0 
        nb_html = 0 
        nb_javaScript = 0 
        nb_css = 0 
        for i in range(0 ,len(codes)):
            header =headers[i].text
            header = header.replace("\n#", '')            
            code =codes[i].text
            text_file_name = header
            if "sv"  in text_file_name[-2:]: 
                nb_csv += 1 
            if "json"  in text_file_name: 
                nb_json += 1
            if "js"  in text_file_name[-2:]: 
                nb_javaScript += 1
            if "html"  in text_file_name: 
                nb_html += 1
            if "css"  in text_file_name: 
                nb_css += 1
        
        df.loc[indice_url, 'nb des fichiers csv '] = nb_csv
        df.loc[indice_url, 'nb des fichiers css '] = nb_css
        df.loc[indice_url, 'nb des fichiers json '] = nb_json
        df.loc[indice_url, 'nb des fichiers JavaScript '] = nb_javaScript
        df.loc[indice_url, 'nb des fichiers html '] = nb_html
        df.loc[indice_url, 'nb total des fichiers '] = nb_csv + nb_json +nb_javaScript +nb_html + nb_css
            
    except:
        pass
    finally:
        driver.quit()


# DF TO CSV
import pandas
df.to_csv("./data_800_1600.csv")