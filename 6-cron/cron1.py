#Cron Linuxiin
from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python kirjoita_aika.py')
job.minute.every(1)

cron.write()

print(job.is_valid())