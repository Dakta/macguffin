from __future__ import print_function, unicode_literals, division, absolute_import
import os, sys

from configparser import SafeConfigParser

cfg_file = SafeConfigParser()
cfg_name = 'macguffin.cfg'
path_to_cfg = os.path.abspath(os.path.dirname(sys.argv[0]))
path_to_cfg = os.path.join(path_to_cfg, cfg_name)
cfg_file.read(path_to_cfg)

# Accounts
TC_USERNAME = cfg_file.get('tehconnection', 'username')
TC_PASSWORD = cfg_file.get('tehconnection', 'password')
TC_PASSKEY = cfg_file.get('tehconnection', 'passkey')

TL_USERNAME = cfg_file.get('torrentleech', 'username')
TL_PASSWORD = cfg_file.get('torrentleech', 'password')
TL_PASSKEY = cfg_file.get('torrentleech', 'passkey')

TMDB_API_KEY = cfg_file.get('utils', 'tmdb_api_key')

IMGBAM_USERNAME = cfg_file.get('utils', 'imgbam_username')
IMGBAM_PASSWORD = cfg_file.get('utils', 'imgbam_password')

# System
# Set this to your rtorrent watch folder path to automatically seed new torrents
WATCH_DIR = cfg_file.get('system', 'watch_dir')

# Logs will be written to this directory, as {Release.Name}.log
# NOTE: Existing logs will be overwritten.
LOG_DIR = cfg_file.get('system', 'log_dir')

# All tracker cookies will be saved here
COOKIE_DIR = cfg_file.get('system', 'cookie_dir')

# Paths to various binaries on your system (in case they are not on the system path)
MEDIAINFO_PATH = 'mediainfo'
FFMPEG_PATH = 'ffmpeg'
FFPROBE_PATH = 'ffprobe'
UNRAR_PATH = 'unrar'

# Set this to True if you want to delete files that don't make it into the uploaded torrent.
# NOTE: If you want to cross-seed, this might not be a good idea.
DELETE_UNWANTED_FILES = False

# How many screenshots to upload by default
NUM_SCREENSHOTS = 4
DELETE_SCREENS_AFTER_UPLOAD = True

####################################################
##  End user-edited sections                      ##
####################################################

# Expand paths
if WATCH_DIR is not None:
    WATCH_DIR = os.path.expanduser(WATCH_DIR)
if LOG_DIR is not None:
    LOG_DIR = os.path.expanduser(LOG_DIR)
if COOKIE_DIR is not None:
    COOKIE_DIR = os.path.expanduser(COOKIE_DIR)