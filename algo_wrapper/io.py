from abc import ABC, abstractmethod
from .config import Config


class IOProcessor(ABC):
    def __init__(self, config):
        if not isinstance(config, Config):
            raise TypeError
        self.input_config = config.get_input_config()
        self.output_config = config.get_output_config()

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def push_output(self, algo_output):
        pass
