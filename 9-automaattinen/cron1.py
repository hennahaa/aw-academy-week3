from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python ilmoitus.py')

#CRON-jobin pienin mahdollinen intervalli on 1 minuutti, joten näitä jobeja pitäisi olla pyörimässä 4?
#Mutta ne pitää vain ajastaa 15 sekunnin väleihin toisistaan
job.minute.every(1)

cron.write()

print(job.is_valid())