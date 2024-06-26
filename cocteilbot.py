import requests
import os
import telebot 

from dotenv import load_dotenv

load_dotenv()


bot=telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def  send_welcome(message):
    bot.reply_to(message," Привет ! Введиет название коктейля  чтобы получить информацижю о нем")


@bot.message_handler(func=lambda message : True)
def  search_cocteil(message):
    coctail_name=message.text
    url=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={coctail_name}"


    responce=requests.get(url)

    data=responce.json()

    if data["drinks"]:
        cocteil= data["drinks"][0]
        reply=(
            f"Название: {cocteil['strDrink']}\n"
            f"Категория: {cocteil['strCategory']}\n"
            f"Тип:{cocteil['strAlcoholic']}\n"
            f"Стекло:{cocteil['strGlass']}\n"
            f"Инструкции :{cocteil['strInstructions']}\n"
            f"Ингредиенты: \n"
        )

        for i in range(1,16):
            ingredient=cocteil.get(f'strIngredient{i}')
            if ingredient == None :
                pass
            measure=cocteil.get(f'strMeasure{i}')
            if ingredient:
                reply+= f"- {ingredient} {measure}\n"

    else:
        reply=" Извините коктейл не найден "
    
    bot.reply_to(message, reply)

bot.polling()




