import click
import os
import yaml
import re
from .api import api_create_board, api_create_card

VERSION = '0.0.1'
CONFIG_FILE = '.trello.cfg'


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.pass_context
@click.version_option(version=VERSION)
def trellocli(ctx):
    "Welcome to trellocli !!!"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as cfg:
            data = yaml.safe_load(cfg)
            api_key = data['api_key']
            server_token = data['server_token']
            ctx.obj = {
                'api_key': api_key,
                'server_token': server_token
            }


@trellocli.command()
@click.pass_context
def config(ctx):
    api_key = click.prompt("Please enter your API key")
    # Make sure that the api_key has 32 digits
    if not re.match("[\da-z]{32}", api_key):
        raise click.BadOptionUsage(api_key, message='API Key Should be with length 32 numerical digit')
    server_token = click.prompt("Please enter your Server Token")
    # Make sure that the server_token has 64 digits
    if not re.match("[\da-z]{64}", server_token):
        raise click.BadOptionUsage(server_token, message='Server Token Should be with length 64 numerical digit')
    with open(CONFIG_FILE, 'w+') as cfg:
        data = {'api_key': api_key, 'server_token': server_token}
        yaml.dump(data, cfg)


@trellocli.command()
@click.pass_context
@click.option('--name', '-n', help='This is the board name', required=True)
def create_board(ctx, name):
    api_create_board(ctx, name)


@trellocli.command()
@click.pass_context
@click.option('--board', help='Which Board you want to create the card with in', required=True)
@click.option('--list', help='Which List you want to create the card with in', required=True)
@click.option('--title', help='Card Title', required=True)
@click.option('--label', help='Card Label ')
@click.option('--comment', help='Card Comment')
def create_card(ctx, board, list, title, label, comment):
    api_create_card(ctx, board, list, title, label, comment)


if __name__ == "__main__":
    trellocli()