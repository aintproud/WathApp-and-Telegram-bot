from aiogram import Bot, Dispatcher, executor, types
from main_v3 import new_messages, first_dict, dictionary
import asyncio
from time import sleep

bot = Bot(token='ur bot token')
dp = Dispatcher(bot)

first_dict()

async def get_fresh_messages(id, wait): 
    await bot.send_message(id , 'first list')
    for number, text in dictionary.items():
       await bot.send_message(id, f'{number}: {text}')
    await bot.send_message(id, '/first list')
    sleep(5)
    
    while True:
        fresh_messages = new_messages()

        if len(fresh_messages) >= 1:
            for number, text in fresh_messages.items():
                message = f'new message for u:{number}/  {text}'
            await bot.send_message(id, message)

        else:
            await bot.send_message(id, 'no new messages')

        await asyncio.sleep(wait)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(get_fresh_messages('ur telegram id', 30))
    executor.start_polling(dp)