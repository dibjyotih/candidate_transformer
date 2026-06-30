from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from models.candidate import Candidate


class BaseParser(ABC):
    """
    Base class for all parsers.
    Every parser must implement:
        - supports()
        - parse()
    """

    @abstractmethod
    def supports(self, file_path: Path) -> bool:
        """
        Returns True if this parser can parse the given file.
        """
        pass

    @abstractmethod
    def parse(self, file_path: Path) -> List[Candidate]:
        """
        Reads the file and returns one or more Candidate objects.
        """
        pass