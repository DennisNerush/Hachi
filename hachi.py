import datetime

from BotHandler import BotHandler
from HachiStatuses import StarvingState, HyperactiveState, SatisfiedState
from HachiStatus import HachiStatus
hachi = HachiStatus()


greet_bot = BotHandler("562742113:AAFzvPJQMsmrYe2K0tdQvViFSqV3R3T1Krw")
greetings = ('hello', 'hi', 'greetings', 'sup')
status = ('status', 'hachi')
ateKeys = ('ate')
walkedKeys = ('walked, kaki')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in status:
            hachi.state
            greet_bot.send_message(last_chat_id, hachi.get_status())
            today += 1

        if last_chat_text.lower() in ateKeys:
            HachiStatus.on_event(hachi, ateKeys[0])
            greet_bot.send_message(last_chat_id, hachi.get_status())
            today += 1

        if last_chat_text.lower() in walkedKeys:
            HachiStatus.on_event(hachi, walkedKeys[0])
            greet_bot.send_message(last_chat_id, hachi.get_status())
            today += 1


        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
