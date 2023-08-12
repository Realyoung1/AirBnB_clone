#!/usr/bin/python3

"""
    This func defines the classes of BaseModel.
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Representingss the BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initializingss the new BaseModel"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(
                            val, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, val)

    def __str__(self):
        """Returningss the strings representationss of the class"""

        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )

    def save(self):
        """Updatingss a date fieldss"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returningss the dictionary representationss of the instancssse"""

        rep = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        dict_copy = self.__dict__.copy()
        dict_copy.update(rep)
        return dict_copy
