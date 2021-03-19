import json
import yaml

class SiteConfig:

    def __init__(self, source_dir, out_filename):
        self.config = {}

        self.source_dir = source_dir
        self.out_filename = out_filename

    def load_from_file(self, filename):
        with open(filename) as fp:
            self.config = yaml.safe_load(fp)


