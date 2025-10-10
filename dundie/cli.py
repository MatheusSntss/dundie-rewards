import json
from importlib.metadata import version

import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.TEXT_MARKUP = True
click.rich_click.TEXT_MARKUP = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.OPTIONS_TABLE_COLUMN_TYPES = [
    "required",
    "opt_short",
    "opt_long",
    "help",
]
click.rich_click.OPTIONS_TABLE_HELP_SECTIONS = [
    "help",
    "deprecated",
    "envvar",
    "default",
    "required",
    "metavar",
]


@click.group()
@click.version_option(version("dundie"))
def main():
    """Dunder Mifflin Rewards System
    this CLI application controls DM rewards.
    """


@main.command
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database."""
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "created", "e-mail"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Show information about users"""
    result = core.read(**query)
    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))
    if not result:
        print("Noting to show")
    table = Table(title="Dunder Mifflin Associates")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")
    for person in result:
        table.add_row(*[str(value) for value in person.values()])
    console = Console()
    console.print(table)


@main.command
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Add point to the user or dept"""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def remove(ctx, value, **query):
    """Remove point to the user or dept"""
    core.add(-value, **query)
    ctx.invoke(show, **query)
