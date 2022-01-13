import click
from yesc.data.install import install


@click.group()
def cli():
    pass


cli.add_command(install)

if __name__ == '__main__':
    cli()
