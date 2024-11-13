#!/usr/bin/env python3
""" Main 0
"""
import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User
import base64

# """ Create a user test """
# user_email = "bob@hbtn.io"
# user_clear_pwd = "H0lbertonSchool98!"
# user = User()
# user.email = user_email
# user.password = user_clear_pwd
# print("New user: {} / {}".format(user.id, user.display_name()))
# user.save()

# basic_clear = "{}:{}".format(user_email, user_clear_pwd)
# print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
