# Qbit Utils
This program is used to stop torrents from rechecking in Qbittorrent, which can take a long time

# Python dependencies:
- python-dotenv
- qbittorrent-api

# Usage:
- Git clone this repository
- Install Python 3 and place it in your PATH environment variable
- Install the python dependencies
- Copy .env.example to .env
- Replace values with actual values to reflect your system's settings
    - QBIT_URL: Go to Qbittorrent > Settings > Web UI > Port. The value to use in .env is "localhost:&lt;portnumber&gt;"
    - QBIT_APPDATA_PATH: https://github.com/qbittorrent/qBittorrent/wiki/Frequently-Asked-Questions#Where_does_qBittorrent_save_its_settings
- Run main.py with python 3