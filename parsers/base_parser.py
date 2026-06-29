from abc import ABC, abstractmethod
from models.candidate import Candidate

class BaseParser(ABC):
    @abstractmethod
    def parse(self, data: str) -> Candidate:
        pass