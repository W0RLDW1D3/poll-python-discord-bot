import discord
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='/')

# Command: /poll
@bot.command()
async def poll(ctx, *, question_and_options):
    # Extracting the poll question and options from the command
    args = question_and_options.split('|')
    question = args[0].strip()
    options = [option.strip() for option in args[1:]]

    # Checking if the command has the correct format
    if not question or len(options) < 2:
        await ctx.send('Please provide a question and at least two options for the poll.')
        return

    # Constructing the poll message
    poll_message = f'**{question}**\n\n'
    for index, option in enumerate(options):
        poll_message += f'{index + 1}. {option}\n'

    # Sending the poll message
    sent_message = await ctx.send(poll_message)

    # Adding reaction emojis as options to the poll message
    number_emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    for i in range(len(options)):
        await sent_message.add_reaction(number_emojis[i])

# Run the bot
bot.run('YOUR_BOT_TOKEN')
                                      
