import time
# import logging
from aiogram import Bot, Dispatcher, executor, types
from data_base import *

TOKEN = "5922210478:AAEotfkZYRL1Qyn6kL5leYAr1ibQYAo01Vs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply("Список команд:\n"
                        "/help - список команд бота\n"
                        "/calc мат.выражение - калькулятор\n"
                        "Работа со справочником:\n"
                        "/base_add ФИО:тел.номер:коментарий - добавить данные\n"
                        "/base_show - выводит весь справочник на экран\n"
                        "/base_find искомое - поиск по справочнику: по имени, фамилии, телефону\n"
                        "/base_del искомое - поиск и удаление из справочника: удаляет все совпадения")

@dp.message_handler(commands=['hello'])
async def hello_handler(message: types.Message):
    # logging.info(f'{message.from_user.id} {message.from_user.full_name} {time.asctime()}')
    await message.reply(f"Привет, {message.from_user.first_name}")
    for i in range(3):
        time.sleep(2)
        await bot.send_message(message.from_user.id, "Что будем делать {}?".format(message.from_user.first_name))

@dp.message_handler(commands=['calc'])
async def calc_handler(message: types.Message):
    exp = message.text[5:]
    exp = eval(exp.replace("^", "**"))
    await message.reply(exp)

@dp.message_handler(commands=['base_add'])
async def base_add(message: types.Message):
    data = message.text[9:].lstrip().split(':')
    data_write(data[0], data[1], data[2])
    await message.reply("Запись в справочник добавлена")

@dp.message_handler(commands=['base_show'])
async def base_show(message: types.Message):
    data = data_read_base()
    for i in data:
        await message.reply(f"{i[0]}, тел. {i[1]}, {i[2]}")

@dp.message_handler(commands=['base_find'])
async def base_find(message: types.Message):
    text = message.text[10:].lstrip()
    finded = find_data(text)
    await message.reply("Найдены записи:")
    for i in finded:
        await message.reply(f"{i[0]}, тел. {i[1]}, {i[2]}")

@dp.message_handler(commands=['base_del'])
async def base_del(message: types.Message):
    text = message.text[9:].lstrip()
    finded = find_data(text)
    for i in finded:
        await message.reply(f"Удалена запись: {i[0]}, тел. {i[1]}, {i[2]}")
    delete_data(finded)


if __name__ == "__main__":
    executor.start_polling(dp)
