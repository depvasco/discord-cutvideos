#DEPENDENCIES
import discord
from discord import app_commands
from moviepy.editor import *

#INSERT THE BOT TOKEN HERE
bot_tk = ''

#STARTING THE BOT
class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

#SYNC TO AVOID BUGS
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 1055071610463334470))
            self.synced = True
        print(f'Discord bot logged on {self.user} as sucesseful!')

client = MyClient()
tree = app_commands.CommandTree(client)

#CUTVIDEO SLASH COMMAND SCRUTURE
#ps: you need to change the guild id so then you can see at commands list
@tree.command(name='cutvideo', description='Cuts a determinated space of a video.', guild = discord.Object(id= INSERT YOUR GUILD ID HERE))
async def self(interaction: discord.Interaction, video_url: str, start: int = None, ends: int = None):
#SIMPLE VERIFICATION IF IT ENDS WITH .mp4 or .wav EXT.
    if video_url.endswith('.mp4' or '.wav'):
        await interaction.response.defer()
#MAKING THE VIDEO (USES YOUR CPU)
        videobefore = VideoFileClip(video_url)
        newvideo = videobefore.subclip(t_start= start, t_end= ends)
        newvideo.write_videofile(filename='produced.mp4')
#IT WILL GO TO THE SOURCE FOLDER, AND WILL BE UPLOADED TO DISCORD
        await interaction.followup.send(file=discord.File('produced.mp4'))   
    else:
        await interaction.response.send_message('We cant indentify this file as a MP4 or WAV file.')

#RUNS THE BOT.
client.run(bot_tk)

