# =======================[PPING]=======================

@idk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ydk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@wdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@sdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@adk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@bdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@cdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@edk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@hdk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ddk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@vkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@kkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@lkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@mkk.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@sid.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@shy.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@aan.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ake.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@eel.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@khu.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@shi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@yaa.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@dav.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@raj.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@put.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tsi.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tsf.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@teg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tth.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ton.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ttw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ttr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tfr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tfv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@tsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ttg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ttn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@fft.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ffo.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ftw.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ftr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ffr.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@ffv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@fsx.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@fsv.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@feg.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@fnn.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))
@fvt.on(events.NewMessage(incoming=True, pattern=f"\\{HNDLR}pping$"))

# @bot.on(man_cmd(outgoing=True, pattern=r"pping$"))
async def _(pping):
    if pping.sender_id in SMEX_USERS:
        """For .ping command, ping the userbot from any chat."""
        uptime = await get_readable_time((time.time() - StartTime))
        start = datetime.now()
        await ping.reply("**✣**")
        await ping.edit("**✣✣**")
        await ping.edit("**✣✣✣**")
        await ping.edit("**✣✣✣✣**")
        end = datetime.now()
        duration = (end - start).microseconds / 1000
        user = await bot.get_me()
        await ping.edit(
            f"**PONG!!🔥**"
        )