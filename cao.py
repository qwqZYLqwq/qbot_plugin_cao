from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from random import *

people=['摸鱼佬','摸鱼只因','菜诺BaKa','闰土','恶龙君','xiaolu']
word=on_keyword({"/草我"})

@word.handle()
async def _():
    img_name = ("cao.jpg")
    img = img_path / img_name
    await word.send(Message([MessageSegment.text(f'你被{choice(people)}狠狠地来了一发'), MessageSegment.image(img)]))
