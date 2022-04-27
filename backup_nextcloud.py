# backup nextcloud data
# copy user data over, compress it


import datetime
import shutil
import subprocess
from pathlib import Path

USERS = ["Anja", "Benno", "Julian", "Leti", "Sarah", "hendrik"]
time_format = "%Y_%m_%d_%H_%M_%S_%f"
datatime_str = datetime.datetime.now().strftime(time_format)

remote_nextcloud_dir = Path('/mnt/mybook/nextcloud_data')
backup_dir = Path("/mnt/mybook2/backups/nextcloud")

# get last backups
last_backup_dirs = [datetime.datetime.strptime(e.name, time_format) for e in backup_dir.glob('202*')]
if last_backup_dirs:
    last_backup_dir = backup_dir / max(last_backup_dirs).strftime(time_format)

# create final dir
final_dir = Path(backup_dir / f'{datatime_str}')
final_dir.mkdir()

for user in USERS:
    # uncompress last user backup
    if last_backup_dirs:
        last_user_backup_fn = last_backup_dir / f"{user}.tar.bz2"
        if last_user_backup_fn.exists():
            uncompress_command = f'tar -xf {last_user_backup_fn} -C {backup_dir}'
            print(uncompress_command)
            subprocess.run(uncompress_command.split(' '), check=True)

            # delete old user backup
            last_user_backup_fn.unlink()

    remote_user_dir = remote_nextcloud_dir / user

    # copy remote files over
    rsync_command = f'rsync -rAHXv --exclude={{".DS_Store","cache","files_trashbin"}} --delete --delete-excluded rheajimmy:{remote_user_dir} {backup_dir}'
    print(rsync_command)
    subprocess.run(rsync_command.split(' '), check=True)

    # compress user dir
    tar_command = f"tar -jcvf {backup_dir / user}.tar.bz2 --directory={backup_dir} {user}"
    print(tar_command)
    subprocess.run(tar_command.split(' '), check=True)

    # remove uncompressed dir
    shutil.rmtree(backup_dir / user)

    # move compressed dir to final dir
    shutil.move(f"{backup_dir / user}.tar.bz2", final_dir)

# compress final dir
# tar_command = f"tar -jcvf {final_dir}.tar.bz2 {final_dir}"
# print(tar_command)
# os.system(tar_command)

# remove uncompressed final dir
# shutil.rmtree(final_dir)
