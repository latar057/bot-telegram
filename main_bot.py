import requests
import pars_main
import constants

last_update_id = 0 # Прошлое сообщение
last_pars = '' # Прошлый анекдот


def get_updates():
    '''json полученного ботом сообщения'''
    url = f'{constants.TG_API_URL}getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    '''Словарь с id чата и содержанием сообщения'''
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = data['result'][-1]['message']['text']

        message = {'chat_id': chat_id, 'message_text': message_text}
        return message
    return None

def send_message(chat_id, text='Подождите секундочку, пожалуйста ...'):
    '''Отправка сообщения'''
    url = f'{constants.TG_API_URL}sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)


def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['message_text']

    if text == '/start':
        send_message(chat_id, 'Введите "j", чтобы получить анекдот.')
        
    while True:
        answer = get_message()

        if answer != None:
            joke = pars_main.pars()[0]
            chat_id = answer['chat_id']
            text = answer['message_text']

            global last_pars
            if last_pars != joke and (text == 'j' or text == 'J'):
                last_pars = joke
                send_message(chat_id, joke)
            else:
                send_message(chat_id, 'Введите, пожалуйста, "j".')
                continue
        else:
            continue


if __name__ == '__main__':
    main()
