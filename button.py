from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Computers"),KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"),KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")]

    ],
    resize_keyboard=True,
    input_field_placeholder="Choise button..."
)

computers = [
    "Mackbook",
    "Lenovo"
]

computers_info = {
    "Mackbook":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":1200,"color":"Black"},
    "Lenovo":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},
#    "HP":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},
#    "ASUS":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},
#    "Victus":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},
#    "ACER":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},
#    "Samsung":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":500,"color":"Blue"},

}

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.adjust(2,repeat=True)
computer_button = computer_button.as_markup(resize_keyboard=True,input_field_placeholder="Choise computer...")
