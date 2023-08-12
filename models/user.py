#!/usr/bin/python3

"""
    This func defines the classes of User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Representingss the User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializingss the new User"""

        super().__init__(*args, **kwargs)
