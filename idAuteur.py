from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import re

req = Request('https://bl.ocks.org', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
bsObj = BeautifulSoup(webpage.read())
element= str(bsObj)
element1 ='aa"owner":{"login":"WilliamQLiu"},"description":"D3 Mouse Events"aaa'
element2 = '{"id":"76ae20060e19bf42d774","sha":"0f3e6be9aba19730d04a39606548b9fd0c3bf944","owner":{"login":"WilliamQLiu"},"description":"D3 Mouse Events"},{"id":"'
z = re.match('("id":")+(.)+(","sha":")+(.)+(","owner":\{"login":")+(.)+("\},"description":")+(.)+("\},\{"id":")', element)
result = re.split('\{"id":"|","sha":"|","owner":\{"login":"|"\},"description":"|"\},|"\}\]\)',element)
Liste_id=[]
Liste_Sha=[]
Liste_Owner=[]
Liste_Description=[]
Liste_Adress=[]
for i in range (1,len(result),5):
    Liste_id.append(result[i])
for i in range (2,len(result),5):
    Liste_Sha.append(result[i])
for i in range (3,len(result),5):
    Liste_Owner.append(result[i])
for i in range (4,len(result),5):
    Liste_Description.append(result[i])

#    print(result[i])

print(len(Liste_id),len(Liste_Sha),len(Liste_Owner),len(Liste_Description))
for i in range (len(Liste_id)) : 
    Liste_Adress.append('https://bl.ocks.org/'+Liste_Owner[i]+'/'+Liste_id[i]+'/')

#Exemple_Adress='https://bl.ocks.org/rpgove/0060ff3b656618e9136b'
#html = urlopen(Exemple_Adress)
#bsObj = BeautifulSoup(html)
Liste_Nom_Auteur=[]
for Exemple_Adress in Liste_Adress :
    req1 = Request(Exemple_Adress, headers={'User-Agent': 'Mozilla/5.0'})
    webpage_sample = urlopen(req1)
    bsObj_sample = BeautifulSoup(webpage_sample.read())
    element_sample= str(bsObj_sample)
    #element00 = 'content="Nate Vack’s Block'
    z_sample = re.match('(content=")+(.)+(’s Block)', element_sample)
    result_sample = re.split('(content="|’s Block)',element_sample)
    print(result_sample[12])
    Liste_Nom_Auteur.append(result_sample[12]) 


print(result_sample[2])






# DF TO CSV
import pandas
df = pandas.DataFrame(data={"id": Liste_id, "sha": Liste_Sha, "login": Liste_Owner,"Nom auteur": Liste_Nom_Auteur, "Description": Liste_Description})
df.to_csv("./data_extracted.csv")



