#FB Love Message Comment Spammer
#Comments automatically with the love messages found in http://www.romanticlovemessages.com/ into your crush's or GF's post
#some posts does not work for the script (even in the Facebook Graph API Explorer) as those posts have got privacy issues. So try with different posts.


###############################
#  Created by Anuran Barman   #
#         1/10/2017           #
###############################

#uses beautifulsoup4 , requests and facebook-sdk python module. Pip install all of them.

import bs4,requests
import facebook
token="#Your FB Token"
graph=facebook.GraphAPI(access_token=token,version='2.3') #use version 2.3 for 100% success
res=requests.get('http://www.romanticlovemessages.com/cat/romantic1.htm')
res2=requests.get('http://www.romanticlovemessages.com/cat/romantic2.htm')
res.raise_for_status()
res2.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'html.parser')
soup2=bs4.BeautifulSoup(res2.text,'html.parser')
list=soup.find_all('div',{'id':'mbox'})
list2=soup2.find_all('div',{'id':'mbox'})
for line in list:
   soupTemp=bs4.BeautifulSoup(str(line),'html.parser')
   div=soupTemp.img
   if div.string is None:
       if graph.put_comment(object_id='#victims post id', message='#your default message if returned string is None'):
           print("success")
       else:
           print("error")
   else:
       if graph.put_comment(object_id='#victims post id', message=div.string+''):
           print("success")
       else:
           print("error")
for line in list2:
   soupTemp=bs4.BeautifulSoup(str(line),'html.parser')
   div=soupTemp.img
   if div.string is None:
       if graph.put_comment(object_id='#victims post id', message='#your default message if returned string is None'):
           print("success")
       else:
           print("error")
   else:
       if graph.put_comment(object_id='#victims post id', message=div.string+''):
           print("success")
       else:
           print("error")

