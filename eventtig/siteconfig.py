import yaml


class SiteConfig:
    def __init__(self, source_dir):
        self.config = {}

        self.source_dir = source_dir

    def load_from_file(self, filename):
        with open(filename) as fp:
            self.config = yaml.safe_load(fp)

    def get_tags_extra_fields(self):
        return self.config.get("tags", {}).get("extra_fields", {})
