from abc import ABC, abstractmethod
from .io import IOProcessor
from .config import Config


class Algorithm(ABC):
    def __init__(self, io_processor, config):
        if not isinstance(io_processor, IOProcessor):
            raise TypeError
        if not isinstance(config, Config):
            raise TypeError
        self.algo_config = config.get_algo_config()
        self.io = io_processor

    def execute(self, **dynamic_args):
        algo_input = self.io.get_input(**dynamic_args)
        algo_output = self.algo(algo_input, **dynamic_args)
        self.io.push_output(algo_output, **dynamic_args)

    @abstractmethod
    def algo(self, algo_input, **dynamic_args):
        pass
