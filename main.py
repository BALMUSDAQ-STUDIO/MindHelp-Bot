import pathlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import  Text
from aiogram.dispatcher.filters.state import StatesGroup,State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold,hlink
import json
import time
import io
from gtts import gTTS
from tempfile import TemporaryFile
import speech_recognition as sr
from pydub import AudioSegment
import g4f
import pathlib
import assets

storage=MemoryStorage()
API_TOKEN='7616147154:AAFnzbyYccP_JZpuTSbIAkEy6Fyuavw4Kuk'
bot= Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot=bot,storage=storage)
ai_role=assets.AI_ROLE
class ClientStatesGroup(StatesGroup):
    ask_ai=State()
    tips=State()


def ai_message(message):
    try:
        print(123)
        completion = g4f.ChatCompletion.create(
            model = g4f.models.gpt_4o,
            messages = [
                {"role": "system", "content": ai_role},
                {"role": "user", "content": f"{message}"}
            ]
        )
        res_message = completion
        print(res_message)
        return res_message

    except Exception as e:
        return f"An error occurred: {str(e)}"

bt_ask=KeyboardButton('Start chat')
bt_tips = KeyboardButton('Tips')
bt_back = KeyboardButton('Back')

def markup(bts):
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    print(bts)
    for i in bts:
        markup.add(i)
    return markup

def text_to_speech(message):
    text = message
    tts = gTTS(text = text)
    audio_file = TemporaryFile()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    audio = AudioSegment.from_file(audio_file, format = "mp3")
    ogg_file = TemporaryFile()
    audio.export(ogg_file, format = "ogg")
    ogg_file.seek(0)
    return ogg_file

@dp.message_handler(commands='start')
async def start(message:types.Message):
    photo=open("main.jpg","rb")
    await message.answer_photo(photo,caption = assets.HELLO_MESSAGE, reply_markup=markup([bt_ask,bt_tips]))


@dp.message_handler(Text('Start chat'))
async def cancel(message:types.Message,state:FSMContext):
    await ClientStatesGroup.ask_ai.set()
    await message.answer("Let's talk. Tell me something😉", reply_markup=markup([bt_back]))

@dp.message_handler(Text('Back'),state=ClientStatesGroup.ask_ai)
async def ask_ai(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Choose option",reply_markup = markup([bt_ask,bt_tips]))


@dp.message_handler(Text('Back'),state=ClientStatesGroup.tips)
async def ask_ai(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Choose option",reply_markup = markup([bt_ask,bt_tips]))

@dp.message_handler(state=ClientStatesGroup.ask_ai)
async def ask_ai(message:types.Message,state:FSMContext):
    res=ai_message(message)
    await message.answer_chat_action("typing")
    await message.answer_voice(text_to_speech(res),reply_markup = markup([bt_back]))
    await message.answer(res,reply_markup = markup([bt_back]))


@dp.message_handler(Text('Tips'))
async def cancel(message:types.Message,state:FSMContext):
    await ClientStatesGroup.tips.set()
    await message.answer("Here are tips on how to improve your mental state☺️", reply_markup = markup([KeyboardButton('Food'),KeyboardButton('Sleep'),KeyboardButton('Physical activity'),bt_back]))


@dp.message_handler(Text("Sleep"),state=ClientStatesGroup.tips)
async def tips_sleep(message:types.Message,state:FSMContext):
    await message.answer_chat_action("typing")
    await message.answer(assets.SLEEP_TIP,reply_markup = markup([KeyboardButton('Food'),KeyboardButton('Sleep'),KeyboardButton('Physical activity'),bt_back]))

@dp.message_handler(Text("Physical activity"),state=ClientStatesGroup.tips)
async def tips_sleep(message:types.Message,state:FSMContext):
    await message.answer_chat_action("typing")
    await message.answer(assets.ACTIVITY_TIP,reply_markup = markup([KeyboardButton('Food'),KeyboardButton('Sleep'),KeyboardButton('Physical activity'),bt_back]))

@dp.message_handler(Text("Food"),state=ClientStatesGroup.tips)
async def tips_sleep(message:types.Message,state:FSMContext):
    await message.answer_chat_action("typing")
    await message.answer(assets.FOOD_TIP,reply_markup = markup([KeyboardButton('Food'),KeyboardButton('Sleep'),KeyboardButton('Physical activity'),bt_back]))

executor.start_polling(dp,skip_updates=True)








