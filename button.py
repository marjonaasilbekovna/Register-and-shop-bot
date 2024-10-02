from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Computers"), KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"), KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Quyidagi tugmalardan birini tanlang..."
)

computers = [
    "Mackbook",
    "Lenovo",
    "HP",
    "ASUS",
    "Victus",
    "Aser",
    "Samsung"
]

computers_info = {
    "Mackbook": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAKRMPXH8t_i6eUEWK6Ls2u5JcQINi2Lavu601fRzzdIH3HiCd16RB-VxwR9Ri49DoqFY&usqp=CAU", "narxi": 1200, "rangi": "kulrang"},
    "Lenovo": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMjrvsIyKJGcpWQ5QSXDbPrcCxnf4I6DdrTUOBH2zeV4UWUNZJifidUlsKX3e5WMTvM-A&usqp=CAU", "narxi": 500, "rangi": "qora"},
    "HP": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYtdrnpMtAm43cI9iykbFnUNJCyqj2nK8VlHji82Sg1m3WZ3aumU4E6L5WKT1qOJhjIq8&usqp=CAU", "narxi": 650, "rangi": "kulrang"},
    "ASUS": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZDkMClzhFmrC0HAjERMnK9hgAE2LVknI2n5i4OjX609Gt9S78ERysjf4n10dwDUkxOvA&usqp=CAU", "narxi": 360, "rangi": "qora"},
    "Victus": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYN_YfrfnrK-g_tF-QXqn6y3Xizwc0EeOGMaZM3XsGzPP9oVPNFfsOFKiq8oMb1yvP2RI&usqp=CAU", "narxi": 850, "rangi": "qora"},
    "Acer": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQmXH0pa2uCbHAnpMQf9plHLWUCaSBKfN6nsvAVjPES17NaXvJ01jfbQgMYz_I8bGgOqQ&usqp=CAU", "narxi": 700, "rangi": "oq"},
    "Samsung": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0tG_yiOJPF7JnCws3bldd2BoNL3iS5vORQct5wpXlRDa8fQb3UD-lO30G_qUT273OkkU&usqp=CAU", "narxi": 1250, "rangi": "oq"}
}

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_keyboard = computer_button.as_markup(resize_keyboard=True, input_field_placeholder="Computerni tanlang...")

phones = [
    "samsung",
    "Redmi",
    "Iphone",
    "Honor",
    "Infinx"
]
phones_info = {
    "samsung": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKb_NEXPpyND3Fs1s1w9qqxu76ozaUr3bJSSx6vKDxXmvkZW9nhdZnQ51CNq1gLNIoSFE&usqp=CAU","narxi": 350,"rangi": "qora va yana 3 xil"},
    "Redmi": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdYsS0hM2KlQKUi3K6ZtxFcaFzqBTUXCZGJbEadRFO8s_tfl_KEuCpCjn6Da3tiUuvjek&usqp=CAU","narxi": 230,"rangi": "oq va yana 3 xil"},
    "Iphone": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_KFxsv_262Yxb0t-CRY_FjIGkNx_Jm3h8SK17-DrPcxW9CMYSwug7kcCFypLiHCeHcXg&usqp=CAU","narxi": 955,"rangi": "oq va yana 3 xil"},
    "Honor": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHWDTehwb6IlNvgRmX_41c30nsGde4NQDg31qW_5cIGUGdB70MFCz90-w-tbi06p_xNig&usqp=CAU","narxi": 180,"rangi": "ko'k va yana 3 xil"},
    "Infinix": {"rasm": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAe8DJdzVWgbHtmM88pFAdJxKtBRxofUBXZgUMM08RGRgsbOlTxUw3-JJUc3ytzbEoEdc&usqp=CAU","narxi": 150,"rangi": "pushti va yana 3 xil"}
}

phones_button = ReplyKeyboardBuilder()

for phone in phones:
    phones_button.add(KeyboardButton(text=phone))

phone_keyboard = phones_button.as_markup(resize_keyboard=True, input_field_placeholder="Telefonni tanlang...")
