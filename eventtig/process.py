from .siteconfig import SiteConfig
from .reader import Reader
from .sqlite import DataStoreSQLite
from .staticsite.builder import StaticSiteBuilder
import tempfile
import os
import shutil

def go(source_dir, source_config, args):

    temp_dir = None

    sqlitefilename = args.sqlite
    if not sqlitefilename:
        temp_dir = tempfile.mkdtemp()
        sqlitefilename = os.path.join(temp_dir, "database.sqlite")

    config = SiteConfig(source_dir)
    config.load_from_file(source_config)

    datastore = DataStoreSQLite(config, sqlitefilename)

    reader = Reader(config, datastore)
    reader.go()

    if args.staticsite:
        builder = StaticSiteBuilder(config, datastore, args.staticsite)
        builder.go()

    if temp_dir:
        shutil.rmtree(temp_dir)
