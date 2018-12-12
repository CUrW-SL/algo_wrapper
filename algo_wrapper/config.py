import json


class Config:
    def __init__(self, configs):
        if isinstance(configs, dict):
            self.algo_config = configs['algo_config']
            self.input_config = configs['input_config']
            self.output_config = configs['output_config']
        else:
            with open(configs) as f:
                json_config = json.load(f)
                self.algo_config = json_config['algo_config']
                self.input_config = json_config['input_config']
                self.output_config = json_config['output_config']

    def get_algo_config(self):
        return self.algo_config

    def get_input_config(self):
        return self.input_config

    def get_output_config(self):
        return self.output_config

    def get_config(self):
        return {
            'algo_config': self.algo_config,
            'input_config': self.input_config,
            'output_config': self.algo_config
        }
