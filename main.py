#import pymysql
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

def main():
    """con = pymysql.connect(host='localhost',
                                 user='root',
                                 password='2012-2020',
                                 db='new_schema',)
    print("connect successful!!")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Student")
        rows = cur.fetchall()

        for row in rows:
            print(row)
        con.commit()"""

    vk_session = vk_api.VkApi(token='b24c75efd7a985cbeed15f42c275927b5061a99d8a6e89e2ef850bfc8eea6f874125ea9c2c319225b273a')
    longpoll = VkBotLongPoll(vk_session, '202850434')
    vk = vk_session.get_api()

    InputLogin = False
    InputPassword = False
    AllRight = False

    listLogPas=[]
    listRows=[["vlad", "vlad"], ["dany", "dany"]]

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and InputLogin==False:
            vk.messages.send(
                user_id=event.obj.from_id,
                random_id=get_random_id(),
                message=("Введите свой логин")
            )
            InputLogin=True

        elif event.type == VkBotEventType.MESSAGE_NEW and InputLogin==True and InputPassword==False:
            listLogPas.append(event.obj.text)
            vk.messages.send(
                user_id=event.obj.from_id,
                random_id=get_random_id(),
                message=("Введи свой пароль")
            )
            InputPassword=True

        elif event.type == VkBotEventType.MESSAGE_NEW and InputLogin==True and InputPassword==True and AllRight==False:
            listLogPas.append(event.obj.text)
            if listLogPas in listRows:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=("Все верно")
                )
                AllRight=True
                listLogPas.clear()
            else:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=("Что то неверно")
                )
                listLogPas.clear()
                InputLogin=False
                InputPassword=False

if __name__ == '__main__':
    main()