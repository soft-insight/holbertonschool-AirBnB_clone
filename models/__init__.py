#!/usr/bin/python3
"""Create a unique FileStorage instance, import of
   the class Storage and creates an  intance to call
   the reload function
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
