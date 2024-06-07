from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inlane():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline2 = InlineKeyboardButton('Рецепты бургеров', url='https://eda.ru/recepty/burgery')
    keyboard_inline.add(but_inline2)
    return keyboard_inline


def get_keyboard_inlane2():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Рецепты пиццы', url='https://eda.ru/recepty/vypechka-deserty/domashnyaya-picca-34388')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inlane3():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Суш', url='https://www.russianfood.com/recipes/bytype/?fid=685')
    keyboard_inline.add(but_inline)
    return keyboard_inline