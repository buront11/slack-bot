from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import datetime

@respond_to('担当')
def mention_func(message):
    now = datetime.date.today()
    if int(now.day) % 5 ==0:
        message.reply("今日の担当は阿部です")
    elif int(now.day) % 5 ==1:
        message.reply("今日の担当は石崎です")
    elif int(now.day) % 5 ==2:
        message.reply("今日の担当は栗山です")
    elif int(now.day) % 5 ==3:
        message.reply("今日の担当は佐藤です")
    elif int(now.day) % 5 ==4:
        message.reply("今日の担当は佐野です")