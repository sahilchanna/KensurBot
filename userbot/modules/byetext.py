import asyncio

@cmd(pattern="bye")
async def bye(ult):
	await ult.edit("Guys I Gotta Go!")
	await asyncio.sleep(1)
	await ult.edit("""
	
┏━━┳┓╋╋┏┳━━━┓
┃┏┓┃┗┓┏┛┃┏━━┛
┃┗┛┗┓┗┛┏┫┗━━┓
┃┏━┓┣┓┏┛┃┏━━┛
┃┗━┛┃┃┃╋┃┗━━┓
┗━━━┛┗┛╋┗━━━┛
""")
