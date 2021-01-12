import requests
from bs4 import BeautifulSoup
import telebot # pyTelegramBotAPI library

bot_token = "paste token here"
chat_tag = "@pvxtechnews"
msg = "join @pvxtechnews for daily tech news!"
#variables={"lastNews":"Google at Odds With US Over Protective Order for Firms Tied to Lawsuit"}

lastNews=variables["lastNews"]

# def beebom():
#     print("Getting news from beebom!")
#     url = 'https://beebom.com/category/news/'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     headings = soup.findAll("div",class_='item-details')

#     count=0
#     List = []
	
#     count=0 #to get only top 14 news
#     for heading in headings:
#         news=heading.a.text

#         if news[:4]=="This" or news[:4]=="Here" or news[:3]=="How" or news[:4]=="What" or news[:5]=="These" or news[-3:]=="..." or news[0].isdigit() == True: #filter heading that start with This,These and which end with ...
#             continue
	
#         count+=1

#         if count==15:
#             break
#         #if count==11:
# 			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
        
#         List.append("\n\n🌐")
#         List.append(news)
	
#     return List

def getNews():
        print("Getting news from inshorts public api!")
        url = 'https://inshorts.vercel.app/technology'
        page = requests.get(url)
        dict = eval(page.text)

        List = []
        count=0
        for title in dict["articles"]:
                heading = title["title"][6:-4]
                if heading[-1]=='?':
                        continue
                count+=1

                if count==15:
                    break
                #if count==11:
                    #List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
                List.append("\n\n🌐")

                List.append(heading)

        return List


def ndtv():
	print("Getting news from gadgets ndtv!")
	url = 'https://gadgets.ndtv.com/news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	headings = soup.findAll(class_='news_listing')
	
	List = []
	count=0 #to get only top 14 news
	for heading in headings:
		count=count+1
      
		if count==15:
			break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		headline=heading.text

		if headline[-23:]==": Price, Specifications": #cropping headings having this text in the end
			List.append(headline[:-23])
		else:
			List.append(headline)
		
		if List[-1]==lastNews:
			List.pop()
			List.pop()
			break
	
	if count >= 10:
		return List
	
	print("\n!!!!!! NOT ENOUGH NEW NEWS IN GADGETS NDTV !!!!!!!!!! \n")
	
	return getNews()

	#previous code below
	# return beebom()

bot = telebot.TeleBot(token=bot_token)

List=ndtv()
List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')
#print(List)
variables["lastNews"]=List[2] #saving last news
print("Last news is "+lastNews)

List.append("\n\n"+msg)

text = " ".join(List)
#print(text)

try:
        bot.send_message(chat_tag,text)
        print("\nTECH NEWS POSTED :) !!")
except:
        print("chat tag or bot token or text message is incorrect!")
