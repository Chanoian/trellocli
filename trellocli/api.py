import requests
import click

TRELLO_API_URL = 'https://api.trello.com/1/'
ANSI_RED = '\033[31m'

# [a-z][0-9]{32}
# [a-z][0-9]{64}

def _parse_ctx(ctx):
    """
    """
    try:
        api_key = ctx.obj['api_key']
        server_token = ctx.obj['server_token']
    except TypeError:
        raise click.ClickException(message='Please make sure to run ***trellocli config*** to provide API_KEY and SERVER_TOKEN')
    return (api_key, server_token)


def _get_list_of_available_labels_within_board(board_id, api_key, server_token):
    url = TRELLO_API_URL + 'boards/{}/labels'.format(board_id)
    querystring = {"key": api_key, "token": server_token}
    response = requests.get(url, params=querystring)
    data = response.json()
    labels_list = list()
    for id in data:
        labels_list.append(id['color'])
    return labels_list


def _get_board_id(board, api_key, server_token):
    """
    """
    url = TRELLO_API_URL + 'members/me/boards'
    querystring = {"key": api_key, "token": server_token}
    response = requests.get(url, params=querystring)
    data = response.json()
    for brd in data:
        if brd['name'] == board:
            return brd['shortLink']
    return click.echo(ANSI_RED + 'The Board {} Might Not Exist'.format(board))


def _get_list_id_within_board(board_id, list, api_key, server_token):
    url = TRELLO_API_URL + 'boards/{}/lists'.format(board_id)
    querystring = {"key": api_key, "token": server_token}
    response = requests.get(url, params=querystring)
    data = response.json()
    for lst in data:
        if lst['name'] == list:
            return lst['id']
    return click.echo(ANSI_RED + 'The List {} Might Not Exist'.format(list))


def _create_card(list_id, title, label, comment, api_key, server_token):
    url = TRELLO_API_URL + 'cards'
    querystring = {"idList": list_id, "key": api_key, "token": server_token, "name": title}
    try:
        response = requests.post(url, params=querystring)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return click.echo(ANSI_RED + 'Something Went Wrong !!')
    click.echo('The Card Created Successfully !!!')
    return response.json()['id']


def _add_comment_to_card(card_id, comment, api_key, server_token):
    url = TRELLO_API_URL + '/cards/{}/actions/comments'.format(card_id)
    querystring = {"key": api_key, "token": server_token, "text": comment}
    try:
        response = requests.post(url, params=querystring)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return click.echo(ANSI_RED + 'Adding the commend failed !!')
    return click.echo('The Comment Added Successfully !!!')


def _add_label_to_card(card_id, label, api_key, server_token):
    url = TRELLO_API_URL + '/cards/{}/labels'.format(card_id)
    querystring = {"key": api_key, "token": server_token, "color": label}
    try:
        response = requests.post(url, params=querystring)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return click.echo(ANSI_RED + 'Adding The label failed !!')
    click.echo('The Label Added Successfully !!!')


def api_create_board(ctx, name):
    api_key, server_token = _parse_ctx(ctx)
    url = TRELLO_API_URL + 'boards'
    querystring = {"name": name, "key": api_key, "token": server_token}
    try:
        response = requests.post(url, params=querystring)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return click.echo(ANSI_RED + 'Something Went Wrong !!')
    return click.echo('The Board {} Created Successfully !!!'.format(name))


def api_create_card(ctx, board, list, title, label, comment):
    api_key, server_token = _parse_ctx(ctx)
    board_id = _get_board_id(board, api_key, server_token)
    list_id = _get_list_id_within_board(board_id, list, api_key, server_token)
    card_id = _create_card(list_id, title, label, comment, api_key, server_token)
    if label:
        available_labels = _get_list_of_available_labels_within_board(board_id, api_key, server_token)
        if label not in available_labels:
            click.echo(ANSI_RED + 'The Label {} Not Found in this board'.format(label))
        else:
            _add_label_to_card(card_id, label, api_key, server_token)
    if comment:
        _add_comment_to_card(card_id, comment, api_key, server_token)
