from os import environ
from text_classifier import app
#from revise.create_database import createDatabase

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    #createDatabase()
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)