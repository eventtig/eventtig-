import os
import shutil
import sys
import tempfile

from .reader import Reader
from .siteconfig import SiteConfig
from .sqlite import DataStoreSQLite
from .staticsite.builder import StaticSiteBuilder


def build(source_dir, source_config, args):

    temp_dir = None

    sqlitefilename = args.sqlite
    if not sqlitefilename:
        temp_dir = tempfile.mkdtemp()
        sqlitefilename = os.path.join(temp_dir, "database.sqlite")

    config = SiteConfig(source_dir)
    config.load_from_file(source_config)

    datastore = DataStoreSQLite(config, sqlitefilename)

    reader = Reader(config, datastore)
    had_errors = reader.go()

    if args.staticsite:
        builder = StaticSiteBuilder(config, datastore, args.staticsite)
        builder.go()

    if temp_dir:
        shutil.rmtree(temp_dir)

    if had_errors:
        print("ERRORS OCCURRED- See Above")
        sys.exit(-1)
    else:
        sys.exit(0)


def check(source_dir, source_config):

    temp_dir = tempfile.mkdtemp()
    sqlitefilename = os.path.join(temp_dir, "database.sqlite")

    config = SiteConfig(source_dir)
    config.load_from_file(source_config)

    datastore = DataStoreSQLite(config, sqlitefilename)

    reader = Reader(config, datastore)
    had_errors = reader.go()

    shutil.rmtree(temp_dir)

    if had_errors:
        print("ERRORS OCCURRED- See Above")
        sys.exit(-1)
    else:
        sys.exit(0)
