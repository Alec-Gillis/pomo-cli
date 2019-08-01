'''
Pomodoro Technique CLI
'''
import click
import sqlite3
from sqlite3 import Error


@click.group()
def db_commands():
    pass

def init():
    create_connection("./pomodoro.db")

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        print("Initializing database...")
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print("Could not create database!")
        print(e)
    finally:
        conn.close()
        print("Database created successfully")
        
    
#@click.option('--init')
#@click.option('--list'
#@click.option('--add')
#@click.option('--remove')
#@click.option('--start')

if __name__ == '__main__':
    print('in main')
    init()


#@click.option("--count", default=1, help="Number of greetings.")
#@click.option("--name", prompt="Your name",
#              help="The person to greet.")
#def hello(count, name):
#    """Simple program that greets NAME for a total of COUNT times."""
#    for _ in range(count):
#        click.echo("Hello, %s!" % name)


