import qbittorrentapi
from pathlib import Path
import shutil
import pprint
from dotenv import dotenv_values

config = dotenv_values(".env")

client = qbittorrentapi.Client(host=config.get("QBIT_URL"))

qbit_appdata_path = Path(config.get("QBIT_APPDATA_PATH"))
bt_backup_path = qbit_appdata_path / 'BT_backup'
torrents_backup_path = qbit_appdata_path / 'torrents'

torrents_backup_path.mkdir(parents=True, exist_ok=True)

try:
    client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

checking_torrents = [torrent for torrent in client.torrents_info() if torrent.state_enum.is_checking or torrent.state_enum.is_errored]
for torrent in checking_torrents:
    # List of dictionary values returned from torrents_info()
    #pprint.pprint(dict(torrent), indent=4)

    torrent_path = torrents_backup_path / f"{torrent.hash}.torrent"
    shutil.copy(bt_backup_path / f"{torrent.hash}.torrent", torrent_path)
    client.torrents_delete(torrent_hashes=torrent.hash)
    client.torrents_add(
            torrent_files=str(torrent_path),
            save_path=torrent.save_path,
            category=torrent.category,
            is_skip_checking=True,
            rename=torrent.name,
            upload_limit=torrent.up_limit,
            download_limit=torrent.dl_limit,
            use_auto_torrent_management=torrent.auto_tmm,
            is_sequential_download=torrent.seq_dl,
            is_first_last_piece_priority=torrent.f_l_piece_prio,
            tags=torrent.tags,
            ratio_limit=torrent.ratio_limit,
            seeding_time_limits=torrent.seeding_time_limit
    )
