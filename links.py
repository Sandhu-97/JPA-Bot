import gspread
import logging

logging.basicConfig(level=logging.WARNING, filename='errors.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

gc = gspread.service_account(filename='credentials.json')
mastersheet = gc.open('player links')
linkssheet = mastersheet.get_worksheet(0)

sortedsheet = mastersheet.get_worksheet(1)

def add_link(id, tag):
    tags = linkssheet.col_values(2)
    ids = linkssheet.col_values(1)
    if tag in tags:
        index = tags.index(tag)
        id = ids[index]
        is_linked = True
        return id, '**{}** is already linked with **{}**'
    try:
        id = str(id)
        linkssheet.append_row([id, tag])
        return id, '**{}** has been linked with **{}**'

    except:
        logging.exception('add_link')


def get_links(id):
    try:
        row = sortedsheet.find(id, None, 1).row
        if row:
            tags = sortedsheet.row_values(row)[1:]
            return tags
        return None
 
    except:
        logging.exception('get_links')

def del_link(tag):
    try:
        row = linkssheet.find(tag, None, 2).row
        linkssheet.update_cell(row, 1, '') # deleting link from the ids col
        linkssheet.update_cell(row, 2, '') # deleting link from tags col

    except:
        logging.exception('del_link')

def get_link_by_tag(tag):
    try:
        row = linkssheet.find(tag, None, 2).row
        id = linkssheet.cell(row, 1).value
    except:
        logging.exception('get_link_by_tag')
    else:
        return id
    
roles_dic = {
    'JOHN CENA': 1035222919225286736,
    'playyboys♥': 1035223069637226607,
    'AvengerS.': 1035223181419626579,
    '#1 Elite': 1049743057563680829,
    'Member': 1030004174148087878,
    'Elder': 1030004173535711242,
    'Co-Leader': 1030004172952711178,
    'Leader': 1030004171975442443
}