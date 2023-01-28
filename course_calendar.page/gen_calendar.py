# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:18:29 2022

@author: WESTMR
"""
from bs4 import BeautifulSoup

with open('source.md','r') as current_calendar:
    html_source = current_calendar.read()
    
soup = BeautifulSoup(html_source,'html.parser')
table_body = soup.table.tbody
table_body.clear()

with open('basic_schedule.md','r') as list_form:
    calendar_details = list_form.read().split('\n')

import datetime
first = datetime.date(2023,1,30)
last = datetime.date(2023,5,12)
spring_break = datetime.date(2023,3,20)
two_days = datetime.timedelta(days=2)
seven_days = datetime.timedelta(days=7)

mon = first
week_number = 1
ii = 0


while mon < last:
    wed = mon + two_days
    fri = wed + two_days
    
    
    new_tr = soup.new_tag("tr")
    new_th = soup.new_tag('th')
    if mon == spring_break:
        new_th.string = "Break"
    else:
        new_th.string = f"Week {week_number}"
        week_number += 1
    new_tr.append(new_th)
    
    for day in [mon,wed,fri]:
        new_td = soup.new_tag('td')
        if new_th.string == "Break":
            content = "No Class"
        elif ii < len(calendar_details):
            content = calendar_details[ii]
            ii += 1
        else:
            content = ''
        new_td.string = f"{day.month}/{day.day} - {content}"
        new_tr.append(new_td)
    table_body.append(new_tr)
    
    
    mon = mon+seven_days

with open('source.md','w') as current_calendar:
    current_calendar.write(soup.prettify())