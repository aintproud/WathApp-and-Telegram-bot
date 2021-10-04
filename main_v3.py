from seleniumwire import webdriver
from time import sleep
import json

dictionary = {}

driver = webdriver.Chrome(
    executable_path=r'driwer path')

driver.get("https://web.whatsapp.com/")
sleep(15)



def first_dict():
    chat_check = []
    muted_chats = []
    i = 0
    while True:
        sleep(5)
        block = driver.find_element_by_xpath("//*[@id='pane-side']")
        print('block is fine')
        chats = block.find_elements_by_xpath(".//div[@class='zoWT4']")
        print('parsing...')
        i = i + 1
        if i > 3:
            i = 0
            print('refresh page...')
            driver.refresh()
            print('end!!!')
            break
        else:
            sleep(2)
            for chat in chats:
                if chat.text in chat_check:
                    continue
                elif chat.text in muted_chats:
                    print(f'{chat.text} замучен)))')
                    
                    continue
                else:
                    chat_check.append(chat.text)
                    sleep(1)
                    i = 0
                    print(chat.text)
                    chat.click()
                    print(len(chat_check))
                    sleep(5)
                    massage_box = driver.find_element_by_class_name(
                        'y8WcF')
                    massages = massage_box.find_elements_by_class_name('_22Msk')

                    for message in massages:
                        try:
                            send_by = message.find_element_by_class_name('_1BUvv')
                            send = send_by.text
                            if send in dictionary:
                                print(f'{send}false')
                                continue
                            else:
                                print(send)
                                message_text = message.find_element_by_class_name('_1Gy50')
                                print(message_text.text)
                                dictionary[send] = message_text.text
                                sleep(1)
                        except Exception:
                            print('gap!!!')
                            continue
        
        with open('ws3.json', 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)


def new_messages():
    with open('ws3.json', encoding='utf-8') as file:
        dictionary = json.load(file)
    muted_chats = []
    chat_check = []
    fresh_messages = {}
    i = 0
    while True:
        sleep(5)
        block = driver.find_element_by_xpath("//*[@id='pane-side']")
        print('block is fine')
        chats = block.find_elements_by_xpath(".//div[@class='zoWT4']")
        print('searching for new messages...')
        i = i + 1
        if i > 3:
            i = 0
            print('refresh page...')
            driver.refresh()
            print('end!!!')
            break
        else:
            sleep(2)
            for chat in chats:
                if chat.text in chat_check:
                    continue
                elif chat.text in muted_chats:
                    print(f'{chat.text} замучен)))')

                    continue
                else:
                    chat_check.append(chat.text)
                    sleep(1)
                    i = 0
                    print(chat.text)
                    chat.click()
                    print(len(chat_check))
                    sleep(5)
                    massage_box = driver.find_element_by_class_name(
                        'y8WcF')
                    massages = massage_box.find_elements_by_class_name(
                        '_22Msk')

                    for message in massages:
                        try:
                            send_by = message.find_element_by_class_name(
                                '_1BUvv')
                            send = send_by.text
                            if send in dictionary:
                                print(f'{send}false')
                                continue
                            else:
                                print(send)
                                message_text = message.find_element_by_class_name(
                                    '_1Gy50')
                                print(message_text.text)
                                dictionary[send] = message_text.text
                                fresh_messages[send] = message_text.text
                                sleep(1)
                        except Exception:
                            print('gap!!')
                            continue
        
    with open('ws3.json', 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)
    print(fresh_messages)
    return fresh_messages
