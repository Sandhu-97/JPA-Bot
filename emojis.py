lines_emoji = '<a:lines:1049699649411362836>'*8
dot_emoji = '<a:SC_Point:1051709557157658644>'
tdot_emoji = '<a:tdot:1039755764295798824>'

def get_townhall_emoji(th):
    if th == 1:
        return '<:TH1:1087804411176288356>'
    elif th == 2:
        return '<:TH2:1087804502779891752>'
    elif th == 3:
        return '<:th3:943183925197561926>'
    elif th == 4:
        return '<:th4:943183925356953700>'
    elif th == 5:
        return '<:th5:943183926967545896>'
    elif th == 6:
        return '<:th6:943183926426476584>'
    elif th == 7:
        return '<:th7:943183926267109458>'
    elif th == 8:
        return '<:th8:943183926376157224>'
    elif th == 9:
        return '<:th9:943183926925623308>'
    elif th == 10:
        return '<:th10:943183926954967040>'
    elif th == 11:
        return '<:th11:943183925889601578>'
    elif th == 12:
        return '<:th12:943183926506172466>'
    elif th == 13:
        return '<:th13:943183926468444180>'
    elif th == 14:
        return '<:th14:943183926925606933>/'
    elif th == 15:
        return '<:TH15:1087806502728912987>'
    else:
        return '🏚️'

def get_builderhall_emoji(bh):
    if bh == 1:
        return '<:bb01:701598219536433254>'
    elif bh == 2:
        return "<:bb02:701598220048007298>" 
    elif bh == 3:
        return "<:bb03:701598219909595206>"
    elif bh == 4:
        return "<:bb04:701598220018778112>"
    elif bh == 5:
        return "<:bb05:701598219796348969>"
    elif bh == 6:
        return "<:bb06:701598220089819197>"
    elif bh == 7:
        return "<:bb07:701598220421431316>"
    elif bh == 8:
        return "<:bb08:701598220366774383>"
    elif bh == 9:
        return "<:bb09:759066347811766272>"
    else:
        return '🛖'
    
def get_warleague_emoji(wl):
    if wl == 'Bronze League III':
        return '<:BronzeLeagueIII:774314462629986304>'
    elif wl == 'Bronze League II':
        return '<:BronzeLeagueII:774314462161272864>'
    elif wl == 'Bronze League I':
        return '<:BronzeLeagueI:774314462789369876>'
    elif wl == 'Silver League III':
        return '<:SilverLeagueIII:774314463204999208>'
    elif wl == 'Silver League II':
        return '<:SilverLeagueII:774314463091884042>'
    elif wl == 'Silver League I':
        return '<:SilverLeagueI:774314463054266398>'
    elif wl == 'Gold League III':
        return '<:GoldLeagueIII:774314463045091378>'
    elif wl == 'Gold League II':
        return '<:GoldLeagueII:774314462974443540>'
    elif wl == 'Gold League I':
        return '<:GoldLeagueI:774314462664327189>'
    elif wl == 'Crystal League III':
        return '<:CrystalLeagueIII:774314462995284019>'
    elif wl == 'Crystal League II':
        return '<:CrystalLeagueII:774314462534041642>'
    elif wl == 'Crystal League I':
        return '<:CrystalLeagueI:774314462895013978>'
    elif wl == 'Master League III':
        return '<:MasterLeagueIII:774314463116656660>'
    elif wl == 'Master League II':
        return '<:MasterLeagueII:774314463263719425>'
    elif wl == 'Master Leageu I':
        return '<:MasterLeagueI:774314463049285662>'
    elif wl == 'Champion League III':
        return '<:ChampionLeagueIII:774314462693425183>'
    elif wl == 'Champion League II':
        return '<:ChampionLeagueII:774314462605082684>'
    elif wl == 'Champion League I':
        return '<:ChampionLeagueI:774314462693949490>'


