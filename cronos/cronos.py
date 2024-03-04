"""Creates 3 tasks for Cronos to show Fibonacci numbers.
First schedules task every 3 hours.
Second schedules to 15:15 every day.
Third schedules every sunday at 00:00.
"""

from crontab import CronTab

# first task for cron every 3 hours
cron = CronTab(user=True)
first_job = cron.new(command='python lesson_2/main.py')
first_job.hour.every(3)
cron.write()

# second task for cron at 15:15 every day
cron = CronTab(user=True)
second_job = cron.new(command='python lesson_2/main.py')
second_job.hour.on(15)
second_job.minute.also.on(15)
cron.write()

# third task for cron every sunday at 00:00
cron = CronTab(user=True)
third_job = cron.new(command='python lesson_2/main.py')
third_job.dow.on('SUN')
third_job.hour.also.on(0)
third_job.minute.also.on(0)
cron.write()
