# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:00:04 2018

@author: admin2
"""


#importing libs
import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from pprint import pprint
import numpy as np
import pandas as pd
import numpy
from numpy import vstack
from numpy import hstack
import re

###########################
#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://www.flywire.com/"
driver.get(urls)


payment_method = []
pt_amount = []
country = []
institute_name = []

countries = []





elem_9 = driver.find_elements_by_class_name("Heading")
for e in elem_9:
    institute = (e.text)
        
elem_2 = driver.find_element_by_id("sender_country")
elem_2.send_keys(Keys.ENTER)
elem_1 = driver.find_elements_by_xpath("//li [@class='Autocomplete-option']")

for i in elem_1:
    countries.append(i.text)
 
countries = ['Afghanistan',	'Albania',	'Algeria',	'Angola',	'Argentina',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'Brunei Darussalam',	'Bulgaria',	'Burundi',	'Cambodia',	'Cameroon',	'Canada',	'Central African Republic',	'Chad',	'Chile',	'China',	'Colombia',	'Congo',	'Costa Rica',		'Croatia',	'Cyprus',	'Czech Republic',	'Denmark',	'Dominican Republic',	'Ecuador',	'Egypt',	'El Salvador',	'Estonia',	'Ethiopia',	'Fiji',	'Finland',	'France',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Gibraltar',	'Greece',	'Grenada',	'Guatemala',	'Guinea',	'Guyana',	'Haiti',	'Honduras',	'Hong Kong',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iraq',	'Ireland',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jordan',	'Kazakhstan',	'Kenya',	'Korea, Republic of',	'Kuwait',	'Kyrgyzstan',	'Latvia',	'Lebanon',	'Lithuania',	'Madagascar',	'Malaysia',	'Maldives',	'Malta',	'Mauritius',	'Mexico',	'Moldova, Republic of',	'Monaco',	'Mongolia',	'Montenegro',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nepal',	'Netherlands',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'Norway',	'Oman',	'Pakistan',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Poland',	'Portugal',	'Puerto Rico',	'Qatar',	'Reunion',	'Romania',	'Russian Federation',	'Rwanda',	'Saint Vincent and the Grenadines',	'Saudi Arabia',	'Senegal',	'Serbia',	'Seychelles',	'Singapore',	'Slovakia',	'Slovenia',	'Somalia',	'South Africa',	'Spain',	'Sri Lanka',	'Suriname',	'Sweden',	'Switzerland',	'Syrian Arab Republic',	'Taiwan',	'Tajikistan',	'Tanzania, United Republic of',	'Thailand',	'Trinidad and Tobago',	'Tunisia',	'Turkey',	'Turkmenistan',	'Uganda',	'Ukraine',	'United Arab Emirates',	'United Kingdom',	'United States',	'Uruguay',	'Uzbekistan',	'Venezuela',	'Vietnam',	'Western Sahara',	'Yemen',	'Zambia',	'Zimbabwe']
                    
    
    
for j in range(0,len(countries)) :
    elem_9 = driver.find_elements_by_class_name("Heading")
    while(elem_9 == []):
        driver.back()
        driver.forward()
        j = j+1
        elem_9 = driver.find_elements_by_class_name("Heading")
    c = countries[j]
    elem_9 = driver.find_elements_by_class_name("Heading")
    for e in elem_9:
        institute = (e.text)
    elem_5 = driver.find_element_by_id("sender_country")
    elem_5.send_keys(c)
    elem_5.send_keys(Keys.ENTER)
    elem_6  = driver.find_element_by_id("amount")
    elem_6.clear()
    elem_6.send_keys('10000.00')
    time.sleep(3)
    elem_7 = driver.find_element_by_class_name("Navigation-slider")
    elem_7.click()
    time.sleep(5)
    try:
        elem_9 = driver.find_element_by_class_name("PaymentOptions-showMore")
        elem_9.click()
        time.sleep(2)
    except:
        a=5
    elem_7 = driver.find_elements_by_class_name("Offer-name")
    elem_8 = driver.find_elements_by_class_name("Offer-price")
    for e in elem_7:
        payment_method.append(e.text)
        country.append(c)  
    for e in elem_8:
        pt_amount.append(e.text) 
        institute_name.append("Indiana University")
    time.sleep(3)
    driver.back()
    time.sleep(3)
    res__21 = vstack((payment_method,pt_amount, country, institute_name)) 






########    

my_df__21 = pd.DataFrame(res__21)
my_df__21
my_df__21.to_csv('file_indiana 10000 full.csv', index=False, header=True)

