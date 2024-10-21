# act-website
Website for ACT Stats, Signup, Etc.

## Dependencies
(pip install ...)
* flask
* mysql-connector-python

## Hosting
The domain registration is through cloudflare, at `allcuptour.com`. The flask webapp is hosted on [pythonanywhere.com](pythonanywhere.com), as is the MySQL database.

## Database

### Scheduled backups
I followed the steps in [this article](https://help.pythonanywhere.com/pages/MySQLBackupRestore/) to setup a daily backup script in pythonanywhere.
It can be found on the server at `~/db-backup.sh`.

### Restoring a backup
If the database is corrupted, restore the most recent backup, or a date's backup of your choice, by running this from the pythonanywhere bash console.
``` bash
cd ~
mysql -u actexec -h actexec.mysql.pythonanywhere-services.com 'actexec$act_db' < db-backups/DATE_db-backup.sql
```