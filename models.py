class users:
    def __init__(self, username="", password=""):
        self._id = -1
        self.username = username
        self._hashed_password = hashed_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    pass


class messages:
    pass