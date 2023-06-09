""" Module for generating random neko pictures"""
import io
import json

import aiohttp
import discord
import requests
from discord.ext import commands

import teapot
import teapot.tools.embed as embed


def neko_api(x):
    req = requests.get(f'https://nekos.life/api/v2/img/{x}')
    try:
        if req.status_code != 200:
            print("Unable to obtain neko image!")
        api_json = json.loads(req.text)
        url = api_json["url"]
        em = embed.newembed().set_image(url=url)
        return em
    except:
        return teapot.messages.error(f"obtaining image ({req.status_code})")


class Neko(commands.Cog):
    """Neko!!! :3"""

    def __init__(self, bot):
        """Initialize neko class"""
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        await ctx.send(embed=neko_api("neko"))

    @commands.command()
    async def waifu(self, ctx):
        await ctx.send(embed=neko_api("waifu"))

    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(embed=neko_api("avatar"))

    @commands.command()
    async def wallpaper(self, ctx):
        await ctx.send(embed=neko_api("wallpaper"))

    @commands.command()
    async def tickle(self, ctx):
        await ctx.send(embed=neko_api("tickle"))

    @commands.command()
    async def poke(self, ctx):
        await ctx.send(embed=neko_api("poke"))

    @commands.command()
    async def kiss(self, ctx):
        await ctx.send(embed=neko_api("kiss"))

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx):
        await ctx.send(embed=neko_api("8ball"))

    @commands.command()
    async def lizard(self, ctx):
        await ctx.send(embed=neko_api("lizard"))

    @commands.command()
    async def slap(self, ctx):
        await ctx.send(embed=neko_api("slap"))

    @commands.command()
    async def cuddle(self, ctx):
        await ctx.send(embed=neko_api("cuddle"))

    @commands.command()
    async def goose(self, ctx):
        await ctx.send(embed=neko_api("goose"))

    @commands.command()
    async def fox_girl(self, ctx):
        await ctx.send(embed=neko_api("fox_girl"))

    @commands.command()
    async def baka(self, ctx):
        await ctx.send(embed=neko_api("baka"))

    @commands.command()
    async def hentai(self, ctx, api_type=""):
        if ctx.message.channel.nsfw:
            api_types = ['femdom', 'classic', 'ngif', 'erofeet', 'erok', 'les',
                         'hololewd', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri',
                         'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lewd', 'cum', 'spank',
                         'smallboobs', 'Random_hentai_gif', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat',
                         'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'bj', 'woof', 'yuri', 'trap', 'anal',
                         'blowjob', 'holoero', 'feed', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'pwankg', 'eron',
                         'erokemo']
            if api_type in api_types:
                req = requests.get(f'https://nekos.life/api/v2/img/{api_type}')
                try:
                    if req.status_code != 200:
                        print("Unable to obtain image")
                    api_json = json.loads(req.text)
                    url = api_json["url"]

                    message = await ctx.send(embed=teapot.messages.downloading())
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url) as resp:
                            if resp.status != 200:
                                print(resp.status)
                                print(await resp.read())
                                return await ctx.send('Could not download file...')
                            data = io.BytesIO(await resp.read())
                            await ctx.send(
                                file=discord.File(data, f'SPOILER_HENTAI.{url.split("/")[-1].split(".")[-1]}'))
                            await message.delete()
                except:
                    await ctx.send(embed=teapot.messages.error(f"obtaining image ({req.status_code})"))
            else:
                await ctx.send(embed=teapot.messages.invalidargument(", ".join(api_types)))
        else:
            await ctx.send("This command only works in NSFW channels!")


def setup(bot):
    """ Setup Neko Module"""
    bot.add_cog(Neko(bot))
