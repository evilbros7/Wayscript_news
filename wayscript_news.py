import requests
from bs4 import BeautifulSoup
import telebot # pyTelegramBotAPI library

bot_token = "1350155603:AAHMFnGH2UxzsMIjsm66Gs8moi5BkjM9GuA"
chat_tag = "@premiumcoursesdrive"
msg = "𝗝𝗼𝗶𝗻 @premiumcoursesdrive 𝗙𝗼𝗿 𝗗𝗮𝗶𝗹𝘆 𝗧𝗲𝗰𝗵 𝗡𝗲𝘄𝘀..!"
lastNews = variables["lastNews"]
NewNews = []

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

	return List

def getNews():
        print("Getting news from inshorts public api!")
        global NewNews
        url = 'https://inshorts.vercel.app/technology'
        page = requests.get(url)
        dict = eval(page.text)

        List = []
        count=0
        for title in dict["articles"]:
                heading = title["title"][6:-4]
                if heading[-1]=='?':
                        continue

                if heading in lastNews:
                    continue

                count+=1
                if count==15:
                    break
                #if count==11:
                    #List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
                List.append("\n\n🌐")

                List.append(heading)
                NewNews.append(heading)
            
        if count >= 10:
            return List
        else:
            print("\nNOT ENOUGH NEW NEWS IN INSHORTS !!!\nTRYING NDTV GADGETS!\n\n")
            return ndtv()


bot = telebot.TeleBot(token=bot_token)

List=getNews()
List.insert(0,'☆☆☆☆💥 𝗧𝗲𝗰𝗵 𝗡𝗲𝘄𝘀 𝗕𝘆 𝗘𝗩𝗜𝗟𝗭𝗢𝗡𝗘  💥☆☆☆☆')
#print(List)
# variables["lastNews"]=List[2] #saving last news
# print("Last news is "+lastNews)
variables["lastNews"] = NewNews
# print(lastNews)

List.append("\n\n"+msg)

text = " ".join(List)
#print(text)

try:
    bot.send_message(chat_tag,text)
    print("\nTECH NEWS POSTED :) !!")
except:
    print("\nSOMETHING IS WRONG ! PROPBABLY TOKEN OR CHAT ID IS NOT")
