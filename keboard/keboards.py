from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Отправить фото пиццы'),
        KeyboardButton('Перейти на следующую клавиатуру')
    ]
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Отправить фото бургера'),
        KeyboardButton('Перейти назад')
    ]
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_inlane():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Перейти назад')
    ]
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_inlane2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Перейти назад')
    ]
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_inlane3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Перейти назад')
    ]
    keyboard.add(*buttons)
    return keyboard
