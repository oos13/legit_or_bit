import json
import trafilatura as tra
from gensim.summarization import summarize
from string import punctuation as pun
import spacy
# import numpy as np
# import pandas as pd
# from os import environ
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import validators
import os
from dotenv import load_dotenv


#----------Define Google Query Length | Load Spacy | declare API keys----------
global count #how many terms I want to search
count=6

nlp=spacy.load("en_core_web_sm")

def configure():
    load_dotenv()

#----------API code for ClaimBusters----------
api_base_url = "https://idir.uta.edu/claimbuster/api/v2/"
single_endpoint = "score/text/"
multiple_endpoint = "score/text/sentences/"
request_headers = {"x-api-key": os.getenv('claimBusters_api_key')}




#________________________________CLAIM BUSTERS________________________________
#Send & Recive Query to Claim Busters
#Input: String, Single or MultiLine
#output: Json Results
def submit_to_claimbust(userQuery):
    #for line in userQuery.splitlines():
        if '\n' in userQuery:
            api_endpoint = api_base_url + multiple_endpoint + userQuery
            response = requests.get(url=api_endpoint, headers=request_headers)
            res_body = response.json()
            pretty_res_body=json.dumps(res_body,indent=4)
            return pretty_res_body
        else:
            api_endpoint = api_base_url + single_endpoint + userQuery
            response = requests.get(url=api_endpoint, headers=request_headers)
            res_body = response.json()
            pretty_res_body=json.dumps(res_body,indent=4)
            return pretty_res_body

#________________________________GOOGLE________________________________

#check if user input is a url- for google fact checker
#input: string can be text or webiste w/ or w/o https\\:
#output: original string is it not a sign even with modification, or if url w/ or w/o modification

def check_if_site(url):
    http='https://'
    updated_url=''
    if len(url) > 2048:
        return url
    else:
        if url[0:8]== http:
            return url
        else:
            updated_url=http+url
            if not(validators.url(updated_url)):
                return url
            else:
                return updated_url
    #Remove Stop words and convert to Lemmas
    #Input: Any String
    #Output: List of Lemmas
def clean_process_txt(txt):
    result=[]
    pos_tag = ['PROPN', 'VERB', 'ADJ', 'NOUN','NUM']    #part of speech tag 
    wrds=nlp(txt.lower())           # make it all lowercase
    for char in wrds:
        if (char.text in nlp.Defaults.stop_words or char.text in pun):
         continue                    #skip all stopping words and punctuation
        elif(char.pos_ in pos_tag):
         result.append(char.lemma_)  #create list of tokens (lemmas only )
    return result

    #Find count of occurences in doc
    #Input:List of Lemmas
    #Output:Dictonary {Lemma : count}
def tf(cln_txt):
    result={}
    for wrds in cln_txt:
        if wrds not in result:
            result[wrds]=1
        elif wrds in result:
            result[wrds]+=1
    return result 

#input: String (should be in format of comma separated words with space after comma eg. i, am, input)
#output : dictionary of similar documents with meta data (from google API)
def submit(userQuery):
    try:
        # attemt call to Google's fact check API 
        factCheckService = build("factchecktools", "v1alpha1", developerKey=os.getenv('google_api_key'))
       
        request = factCheckService.claims().search(query=userQuery)
        response = request.execute()
        # print(type(response))
        return response

        # TODO more specifically handle problems with Google's API
    except HttpError as err:
        print (err)


#input: String: Full text that will be submited by url pull, TODO: make useable to text entries(NON URL) might build function to check and call accordingly
#Output: Json made with function submit: dictionary of similar documents with meta data (from google API)
def submit_to_google(user_input):
    textsub=''
    urlsub=''

    userQuery = check_if_site(user_input)#Check and modify Query if its a site
    if validators.url(userQuery):
        google_responce=submit(userQuery)#if its a full URL, send to google
        print(google_responce)
        if len(google_responce)!=0:
            print('Query is: ', userQuery)
            return google_responce #if it returns "something" return to user
    # else:                       #if no responce, treat as text submission
    site_tra=tra.fetch_url(user_input)
    extarcted_article=tra.extract(site_tra)
    if extarcted_article== None:
        textsub=userQuery
    
    cleaned=clean_process_txt(extarcted_article) #output list of lemmas
    dict_clean=tf(cleaned)#output : dict {lemma:count}
    #define variables
    submit_dict={}
    submit_list=[]
    submit_str=''
    submit_dict= dict(sorted(dict_clean.items(), key=lambda item:item[1],reverse=True))# sort the dictionary greast to least
    submit_list=list(submit_dict.keys())[0: count]# make list of n wanted terms 
    submit_str=', '.join(submit_list)# format to string for query entry
    print("query is: ",submit_str)
    google_responce=submit(submit_str)#Nothing was found
    if len(google_responce) !=0:
        pretty_google_responce=json.dumps(google_responce,indent=4)
        return pretty_google_responce
    return "We are sorry, but no similar articles or reading material has been found"


#--------------------Function Calls--------------------
#----------Set Url and Query information----------
# url='https://www.nydailynews.com/news/politics/new-york-elections-government/ny-election-2022-nyc-early-voting-numbers-hochul-zeldin-20221031-pitbdklq2jaxlbqm6pv2br3y4q-story.html'
# url='https://www.foxnews.com/politics/abortions-since-roe-v-wade'
url='gigafact.org/fact-briefs/does-gender-affirming-health-care-have-positive-outcomes-for-transgender-youths'
site_tra=tra.fetch_url(url)
userQuery=tra.extract(site_tra)
busters_userQuery=summarize(userQuery)



configure()
print(submit_to_claimbust(busters_userQuery))
print("_____________________Possible Similar Article(s)________________________________")
print('Count is: ',count)
print(submit_to_google(url))






