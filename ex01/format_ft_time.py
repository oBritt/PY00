import time
from datetime import datetime

def run():
    time_sec = time.time()
    # time_nano = time.time_ns()

    # time_sec =  time_sec
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    formated = '{:,.4f}'.format(time_sec)
    formated_s = '{:.2e}'.format(time_sec)
    print("Seconds since January 1, 1970: ", formated, " or ", formated_s, " in scientific notation", sep="")
    months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print(months[current_month - 1], current_day, current_year)
    # print("%.4f" % formated)

run()