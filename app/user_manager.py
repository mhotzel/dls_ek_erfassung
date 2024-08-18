from typing import Protocol

from .user import Role, User


class UserManager(Protocol):
    """Manages Users"""

    def get_user_by_id(self, user_id: str) -> User:
        """Retrieves a User by its Name"""


class TestUserManager:

    def __init__(self) -> None:
        self.user = {
            'matthias': User('matthias', 'Matthias Hotzel', 'wurst', roles=[Role('admin'), Role('user')]),
            'sandra': User('sandra', 'Sandra', 'wurst', roles=[Role('user')]),
        }

    """Simple User Manager - only for testing"""

    def get_user_by_id(self, user_id: str) -> User:
        """Retrieves a User by its Name"""
        return self.user.get(user_id)
