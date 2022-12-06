import os
from hoshino import Service, priv
from nonebot import MessageSegment
from .config import FortuneThemesDict
from .data_source import fortune_manager

sv = Service('今日运势', enable_on_default=True, visible=True)

__fortune_version__ = "v0.4.9"
__fortune_usage__ = f'''
[今日运势/抽签/运势] 一般抽签
[xx抽签]     指定主题抽签
[设置xx签] 设置群抽签主题
[重置主题] 重置群抽签主题
[主题列表] 查看可选的抽签主题
[查看主题] 查看群抽签主题'''.strip()

@sv.on_rex(r"^查看(抽签)?主题$")
async def _(bot, ev):
    gid: str = str(ev.group_id)
    theme: str = fortune_manager.get_group_theme(gid)
    await bot.finish(ev, f"当前群抽签主题：{FortuneThemesDict[theme][0]}")

@sv.on_fullmatch("主题列表")
async def theme_list(bot, ev):
    msg: str = fortune_manager.get_main_theme_list()
    await bot.finish(ev, msg)

@sv.on_prefix('运势','今日运势')
async def portune(bot, ev):
    arg: str = ev.message.extract_plain_text()

    if "帮助" in arg:
        await bot.finish(ev, __fortune_usage__)
    
    gid: str = str(ev.group_id)
    uid: str = str(ev.user_id)
    nickname: str = ev.sender["card"] if ev.sender["card"] else ev.sender["nickname"]
    
    is_first, image_file = fortune_manager.divine(gid, uid, nickname, None, None)
    if not image_file:
        await bot.finish(ev, "今日运势生成出错……") 

    if not is_first:
        msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(f'file:///{os.path.abspath(image_file)}')
    else:
        msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(f'file:///{os.path.abspath(image_file)}')
    
    await bot.send(ev, msg, at_sender=True)        

@sv.on_rex(r"^[^/]\S+(抽签|运势)$")
async def _(bot, ev):
    for theme in FortuneThemesDict:
        if ev["match"].group(0)[:-2] in FortuneThemesDict[theme]:
            if not fortune_manager.theme_enable_check(theme):
                await bot.finish(ev,"该抽签主题未启用~")
            else:
                gid: str = str(ev.group_id)
                uid: str = str(ev.user_id)
                nickname: str = ev.sender["card"] if ev.sender["card"] else ev.sender["nickname"]
                
                is_first, image_file = fortune_manager.divine(gid, uid, nickname, theme, None)
                if not image_file:
                    await bot.finish(ev,"今日运势生成出错……") 
        
                if not is_first:
                    msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(f'file:///{os.path.abspath(image_file)}')
                else:
                    msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(f'file:///{os.path.abspath(image_file)}')
            
            await bot.finish(ev, msg, at_sender=True)

    await bot.finish(ev, "还没有这种抽签主题哦~")
        
@sv.on_rex(r"^设置(.*?)签$")
async def theme_setting(bot, ev):
    gid: str = str(ev.group_id)
    for theme in FortuneThemesDict:
        if ev["match"].group(0)[2:-1] in FortuneThemesDict[theme]:
            if not fortune_manager.divination_setting(theme, gid):
                await bot.finish(ev, "该抽签主题未启用~")
            else:
                await bot.finish(ev, "已设置当前群抽签主题~")

    await bot.finish(ev, "还没有这种抽签主题哦~")

@sv.on_rex(r"^重置(抽签)?主题$")
async def reset(bot, ev):
    if priv.check_priv(ev, priv.ADMIN):
        gid: str = str(ev.group_id)
        if not fortune_manager.divination_setting("random", gid):
            await bot.finish(ev,"重置群抽签主题失败！")
        await bot.finish(ev, "已重置当前群抽签主题为随机~")
    else:
        await bot.finish(ev,"权限不足")

@sv.on_fullmatch("刷新抽签")
async def refresh(bot,ev):
    if priv.check_priv(ev, priv.SUPERUSER):
        fortune_manager.reset_fortune()
        await bot.finish(ev,"今日运势已刷新!")
    else:
        await bot.finish(ev,"权限不足")

# 重置每日占卜
@sv.scheduled_job("cron", hour=0, minute=0, misfire_grace_time=60)
async def reset_fortune():
    fortune_manager.reset_fortune()