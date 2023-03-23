import discord
from discord.ext import commands
import coc
from coc import utils
import asyncio
import links
from emojis import *
from config import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='jpa ', intents=intents)

coc_client = coc.login(COC_EMAIL, COC_PASSWORD)

@bot.event
async def on_ready():
    print(bot.user, 'is ready')

@bot.command()
async def hi(ctx):
    await ctx.send('hey jpa')

@bot.command()
async def player(ctx, tag: str):
    tag = utils.correct_tag(tag)
    try:
        player = await ctx.bot.coc_client.get_player(tag)
    except:
        await ctx.send('invalid player tag')
        return

    tag = player.tag
    name = player.name
    th = player.town_hall
    exp = player.exp_level
    league = player.league
    share_link = player.share_link
    clan = player.clan
    role = str(player.role)
    trophies = player.trophies
    best_trophies = player.best_trophies
    versus_trophies = player.versus_trophies
    donations = player.donations
    received = player.received
    attack_wins = player.attack_wins
    defense_wins = player.defense_wins
    war_stars = player.war_stars
    town_hall_weapon = player.town_hall_weapon
    bh = player.builder_hall
    # capital_contribution = player.clan_capital_contribution
    heroes = player.heroes
    troops_donated = player.get_achievement('Friend in Need').value 
    games_point = player.get_achievement('Games Champion').value
    capital_gold_looted = player.get_achievement('Aggressive Capitalism').value
    capital_gold_donated = player.get_achievement('Most Valuable Clanmate').value
    league_stars = player.get_achievement('War League Legend').value
    th_emoji = get_townhall_emoji(th)
    bh_emoji = get_builderhall_emoji(bh)
    league_icon_url = league.icon.url
    clashofstats_link = f'https://www.clashofstats.com/players/{tag[1:]}'
    chocolateclash_link = f'https://fwa.chocolateclash.com/cc_n/member.php?tag={tag[1:]}'

   
    description = f'''
    {tdot_emoji} **Profile Info** {tdot_emoji}
    Tag: **{tag}**
    Clan: **{clan}**({role})
    {th_emoji} **{th}({town_hall_weapon})** <:exp:1039734151382843482> **{exp}** <:warstar:1039734175739170848> **{war_stars}**
    {lines_emoji}
    {tdot_emoji} **Season Stats** {tdot_emoji}
    {dot_emoji}__Attacks__
    <:trophy:1039734188166877204> Trophies: **{trophies}**
    <:sw:1057308422401437808> Attack Wins: **{attack_wins}**
    <:Defense:1088096954300498081> Defense Wins: **{defense_wins}**
    {lines_emoji}
    {dot_emoji}__Donations__
    <:uparrow:1087992391266480158> Donated: **{donations}**
    <:downarrow:1087993616087122000> Received: **{received}**
    {lines_emoji}
    {tdot_emoji} **Acheivement Stats** {tdot_emoji}
    <:cc:943188177970155620> Troops Donated: **{troops_donated}**
    <:ClanGames:1088110992380149810> Clan Games: **{games_point}**
    <:trophy:1039734188166877204> Best Trophies: **{best_trophies}**
    <:starsuccess:1039734184941469707> League Stars: **{league_stars}**
    <:sw:1057308422401437808> CG Looted: **{capital_gold_looted}**
    <:capitalgold:1039734136816025682> CG Donated: **{capital_gold_donated}**
    {lines_emoji}

    <a:fwa:1037968348828409866> [Chocolate Clash Link]({chocolateclash_link})
    {tdot_emoji} [Clash Of Stats]({clashofstats_link})
    '''

    embed = discord.Embed(title=name, description=description,  color=discord.Color.random())
    embed.url = share_link
    embed.set_thumbnail(url=league_icon_url)
    embed.set_footer(text='◤JPA◢ - 💎FWA💎', icon_url='https://cdn.discordapp.com/attachments/810354680198725643/1087414621385789490/IMG_20230320_220658.png')
    await ctx.send(embed=embed)

@bot.command()
async def approve(ctx, member: discord.Member):
    guild = ctx.message.guild
    channel_id = 1084806577942437949
    approved_role = guild.get_role(1084754624885555200)
    unapproved_role = guild.get_role(1084815867877007382)
    approved_channel = bot.get_channel(channel_id)
    if unapproved_role in member.roles:
        await member.remove_roles(unapproved_role)
    await member.add_roles(approved_role)
    await ctx.send('role added')
    await approved_channel.send('Welcome to your channel')

@bot.command()
async def unapprove(ctx, member: discord.Member):
    guild = ctx.message.guild
    channel_id = 1084815818145153024
    unapproved_role = guild.get_role(1084815867877007382)
    approved_role = guild.get_role(1084754624885555200)
    unapproved_channel = bot.get_channel(channel_id)

    if approved_role in member.roles:
        await member.remove_roles(approved_role)
    await member.add_roles(unapproved_role)
    await unapproved_channel.send(f'you have been unapproved {member.display_name}')
    await ctx.send('member has been unapproved')


@bot.command()
async def link(ctx, tag, member: discord.Member = None):
    tag = utils.correct_tag(tag)
    if not member:
        member = ctx.author
    try:
        player = await ctx.bot.coc_client.get_player(tag)
    except:
        await ctx.send('invalid player tag')
        return
    
    new_id, res = links.add_link(member.id, player.tag)

    try:
        new_member = bot.get_user(int(new_id))
    except:
        await ctx.send('user is invalid')
        return
    
    # await ctx.send(f'{player.name} has been linked to {member.name}')
    await ctx.send(res.format(player.name, new_member.name))

@bot.command()
async def whois(ctx, member: discord.Member= None):
    if not member:
        member = ctx.author
    id = str(member.id)
    tags = links.get_links(id)
    if not tags:
        await ctx.send(f'{member.name} is not linked with any account')
        return
    for tag in tags:
        try:
            player = await ctx.bot.coc_client.get_player(tag)
        except:
            await ctx.send('internal server error')
            break
        
        name = player.name
        th = player.town_hall
        exp = player.exp_level
        league = player.league
        embed = discord.Embed(title=name, description=f'Tag: {tag}\nTH: {th}\nXP: {exp}\nLeague:{league}',  color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

@bot.command()
async def unlink(ctx, tag):
    tag = utils.correct_tag(tag)
    # if tag in links.tags:
    #     await ctx.send(f'{tag} is not linked with anyone')
    #     return
    try:
        links.del_link(tag)
    except:
        await ctx.send('internal server error')
    else:
        await ctx.send(f'{tag} has been unlinked')

@bot.command()
async def clan(ctx, tag: str):
    tag = utils.correct_tag(tag)
    try:
        clan = await ctx.bot.coc_client.get_clan(tag)
    except:
        await ctx.send('invalid clan tag')
        return
    
    tag = clan.tag
    name = clan.name
    location = clan.location
    desc = clan.description
    wins = clan.war_wins
    ties = clan.war_ties
    lose = clan.war_losses
    member_count = clan.member_count
    badge = clan.badge.url
    trophies = clan.points
    versus_trophies = clan.versus_points
    share_link = clan.share_link
    frequency:str = clan.war_frequency
    streak = clan.war_win_streak
    leader = clan.get_member_by(role=coc.Role.leader)
    is_public = clan.public_war_log
    required_trophies = clan.required_trophies
    require_townhall = clan.required_townhall
    requirement:str = clan.type
    war_league = clan.war_league.name
    war_league_emoji = get_warleague_emoji(war_league)
    clash_of_stats_link = f'https://www.clashofstats.com/clans/{tag[1:]}/summary'
    if is_public:
        war_log = '🔓Public'
    else:
        war_log ='🔒Private'
    if requirement == 'inviteOnly':
        requirement = 'Invite Only'

    th_emoji = get_townhall_emoji(require_townhall)
    description = f'''
    {lines_emoji}
    <:members:1062979463660449812> **{member_count}** <:trophy:1039734188166877204> **{trophies}** 🏆 **{versus_trophies}**
    {lines_emoji}
    {desc}
    {lines_emoji}
    {dot_emoji}Leader: <:crown2:1087809487936684144>**{leader}**
    {lines_emoji}
    {dot_emoji}Location: **{location}**
    {lines_emoji}
    {dot_emoji}**Requirements** ⚙️{requirement.capitalize()} <:trophy:1039734188166877204> {required_trophies} {th_emoji} {require_townhall}
    {lines_emoji}
    {dot_emoji}War Log: **{war_log}**
    {lines_emoji}
    {dot_emoji}War Frequency: ⌛**{frequency.capitalize()}**
    {lines_emoji}
    {dot_emoji}War Performance: **<:greentick:943188177856901240> {wins} Won <:redtick:943188177798201354> {lose} Lost ❕{ties} Tied**
    {lines_emoji}
    {dot_emoji}War Win Streak: 🎖️**{streak}**
    {lines_emoji}
    <a:fwa:1037968348828409866> [Chocolate Clash Link](https://fwa.chocolateclash.com/cc_n/clan.php?tag={tag[1:]})
    {tdot_emoji} [Clash Of Stats]({clash_of_stats_link})
    '''
    description = f'''
    <:members:1062979463660449812> **{member_count}** <:trophy:1039734188166877204> **{trophies}** 🏆 **{versus_trophies}**
    {lines_emoji}
    {desc}
    {lines_emoji}
    {tdot_emoji} **Clan Info** {tdot_emoji}
    {dot_emoji}Location: **{location}**
    {dot_emoji}Leader: <:crown2:1087809487936684144>**{leader}**
    {dot_emoji}War Log: **{war_log}**
    {lines_emoji}
    {tdot_emoji} **Requirements** {tdot_emoji}
    <a:arrow1:1051709278907535380> {requirement.capitalize()}
    <a:arrow1:1051709278907535380> {th_emoji} Required
    <a:arrow1:1051709278907535380> {required_trophies} Required
    {lines_emoji}
    {tdot_emoji} **Wars** {tdot_emoji}
    {dot_emoji}Performance: **<:greentick:943188177856901240> {wins} Won <:redtick:943188177798201354> {lose} Lost❕{ties} Tied**
    {dot_emoji}Streak: 🎖️**{streak}**
    {dot_emoji}League: {war_league_emoji}**{war_league}**
    <a:fwa:1037968348828409866> [Chocolate Clash Link](https://fwa.chocolateclash.com/cc_n/clan.php?tag={tag[1:]})
    {tdot_emoji} [Clash Of Stats]({clash_of_stats_link})
    '''
    
    embed = discord.Embed(title=f'{tdot_emoji}{name}{tdot_emoji}', description=description, color=discord.Colour.random())
    embed.url = share_link
    embed.set_footer(text='◤JPA◢ - 💎FWA💎', icon_url='https://cdn.discordapp.com/attachments/810354680198725643/1087414621385789490/IMG_20230320_220658.png')
    embed.set_thumbnail(url=badge)
    await ctx.send(embed=embed)

@bot.command()
async def assign(ctx, tag):
    tag = utils.correct_tag(tag)
    try:
        player = ctx.bot.coc_client.get_player(tag)
    except:
        await ctx.send('invalid player tag')
        return    
    
def get_heroes_levels(heroes):
    bklevel, aqlevel, gwlevel, rclevel = 0, 0, 0, 0
    for hero in heroes:
        if hero.name == 'Barbarian King':
            bklevel = hero.level
        elif hero.name == 'Archer Queen':
            aqlevel = hero.level
        elif hero.name == 'Grand Warden':
            gwlevel = hero.level
        elif hero.name == 'Royal Champion':
            rclevel = hero.level
        

    # if rclevel:
    #     return bk

        
@bot.command()
async def load(ctx:commands.Context, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded extension: {extension}')

@bot.command()
async def reload(ctx:commands.Context, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded extension: {extension}')

    
async def main():

    async with coc.Client() as coc_client:
        # Attempt to log into CoC API using your credentials.
        try:
            await coc_client.login(COC_EMAIL, COC_PASSWORD)
        except coc.InvalidCredentials as error:
            exit(error)

        # Add the client session to the bot
        bot.coc_client = coc_client
        await bot.start('NzY4NTAxMDY0NjM4MDA1MzAw.GLLgND.vQK_mVGtxGBLubN8ULm0DKCdO_yUW5ZWShpmyk')

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass