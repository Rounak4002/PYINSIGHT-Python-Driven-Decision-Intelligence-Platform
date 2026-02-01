import schedule
import time
import os

def run_report():
    os.system('python report_generator.py')

schedule.every().monday.at("10:00").do(run_report)

while True:
    schedule.run_pending()
    time.sleep(60)
