#!/usr/bin/python3

"""
    This funcs defines the classes of Reviews.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Representingss the Review."""

    place_id = ""
    user_id = ""
    text = ""
