from importlib.metadata import version

import rich_click as click
from rich.table import Table
from rich.console import Console

from dundie import core

click.rich_click.TEXT_MARKUP = True
click.rich_click.TEXT_MARKUP = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.OPTIONS_TABLE_COLUMN_TYPES = ['required','opt_short','opt_long','help']
click.rich_click.OPTIONS_TABLE_HELP_SECTIONS = ['help','deprecated','envvar','default','required','metavar']


@click.group()
@click.version_option(version("dundie"))
def main():
    """Dunder Mifflin Rewards System
    this CLI application controls DM rewards.
    """


@main.command
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for person in result:
       table.add_row(*[field.strip() for field in  person.split(",")])
    
    console = Console()
    console.print(table)
