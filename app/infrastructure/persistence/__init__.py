from os import getenv
from app.infrastructure.persistence.fileStorage import FileStorage
from app.infrastructure.persistence.mySQL import MySql

storageType = getenv('STORAGE_TYPE') or 'fileStorage'

storage = None

if storageType == 'fileStorage':
    storage = FileStorage()

if storageType == 'dbStorage':
    storage = MySql()
