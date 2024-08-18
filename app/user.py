
from typing import List, Sequence
from dataclasses import dataclass


@dataclass
class Role:
    """Authorization Role"""

    name: str
    


@dataclass
class User:
    """User"""

    id: str
    name: str
    passwd: str
    roles: Sequence[Role]

    def passwd_valid(self, passwd: str):
        """Checks the password"""
        if self.passwd == passwd:
            return True

        return False
