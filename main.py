from random import choice, randrange
from aiogram import Bot, Dispatcher, types, executor

import config as cfg
import dict as bd

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=bd.make_good)
async def command_handler(message: types.Message):
    await message.reply(f"*сделала хорошо {choice(bd.yuri_fun_reaction)}*")


@dp.message_handler()
async def yuri(message: types.Message):
    text = message.text.lower()
    name = message["from"]["first_name"]
    if "обнял" in text:
        if "юри" in text or "yuri" in text:
            if "обняла" in text:
                await message.reply(f"*{choice(bd.hugs_mode_female)} обнимашки*")
            else:
                await message.reply(f"*{choice(bd.hugs_mode_male)} обнимашки*")
        else:
            rand = randrange(0, 17)
            if rand % 3 == 0:
                if rand % 2 == 0:
                    await message.reply(
                        f"{choice(bd.hugs_reaction_fun).replace('%name%', name)} {choice(bd.yuri_fun_reaction)}"
                    )
                else:
                    await message.reply(
                        f"{choice(bd.hugs_reaction)} {choice(bd.yuri_fun_reaction)}"
                    )

    if ":0" in text:
        await message.reply(choice(bd.king_0))

    if "бля" in text:
        barray = text.split('бля')
        if len(barray) > 3:
            await message.reply(f"Блямит превышен! {choice(bd.yuri_bad_reaction)}")

    if ("жена" in text and "кош" in text) or ("стран" in text and "горд" in text):
        await message.reply(f"{choice(bd.com_pa)} {choice(bd.yuri_fun_reaction)}")

    if "ррр" in text:
        await message.reply(f"Тррр... тррр... тррр...")

    if "сошёл" in text and "ума" in text:
        await message.reply(f"Придется позвонить туда... {choice(bd.yuri_bad_reaction)}")

    if "nuxs" in text or "нукс" in text:
        await message.reply(f"ping @Nuxssss")

    if "cum" in text or "кам" in text or "come" in text or "kam" in text or "кум" in text:
        await message.reply(f"nice cum bro {choice(bd.yuri_fun_reaction)}")

    for word in bd.gachi_words:
        if word in text:
            await message.reply(f"{choice(bd.gachi_phase)} {choice(bd.yuri_fun_reaction)}")

    for word in bd.it_words:
        if word in text:
            await message.reply(f"Обнаружен айтишник!!!!")


if __name__ == "__main__":
    executor.start_polling(dp)
