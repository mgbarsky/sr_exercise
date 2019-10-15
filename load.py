# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

from data import *
from utils import *

data_records =[]
schedule = {}
distinct_hours_dict = set()
distinct_times = []

def load_data():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://simons-rock.edu/student-life/campus-experience/kilpatrick-athletic-center/adult-programs/adult-yoga-and-fitness.php" #input('Enter - ')
    html = urlopen(url, context=ctx).read()

    # html.parser is the HTML parser included in the standard Python 3 library.
    # information on other HTML parsers is here:
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of th2 and b
    tags = soup.find_all(["h2","h2 strong","strong"])

    record = None
    for tag in tags:

        txt = str(tag.get_text())

        txt_split = txt.split(',', 2)
        first_2 = txt_split[0][0:2]

        if tag.name[:2] == "h2": #name tag
            record = Exercise()
            record.setName(txt)
        elif first_2 in days_dictionary:
            d = txt
            # Thursdays, 11:00 a.m.-12:00 p.m.
            # can be more than one
            if record and record.getHour() > 0:
                same_name = record.getName()
                record = Exercise()
                record.setName(same_name)

            info = d.split(',', 2)
            day = info[0][0:2]

            if len(info)>1:
                record.setDay(days_dictionary[day])

                time_info = info[1].strip()
                # print(time_info)

                # extract hours, minutes, am-pm
                start_time = time_info.split('-')[0]
                hour_min = start_time.split()[0]
                # print(hour_min)
                hour = (int)(((hour_min.split(':'))[0]).strip())
                minute = (int)(((hour_min.split(':'))[1]).strip())
                am_pm = 'a'
                if len(start_time.split()) > 1:
                    am_pm = start_time.split()[1][0]
                else:
                    am_pm = time_info.split()[len(time_info.split()) - 1][0]
                # print (am_pm)
                # hour_to_24(hour, am_pm)
                record.setHour(hour_to_24(hour, am_pm))
                record.setMinute(minute)
                data_records.append(record)

    data_records.sort(key=lambda r: (r.getDay(), r.getHour(), r.getMinute()))

    for record in data_records:

        #add all distinct times
        time_obj = Time24(record.getHour(), record.getMinute())
        distinct_hours_dict.add (time_obj)

        # check if there are records for this day and time and add them to the list
        key = data_label(record)
        if key in schedule:
            #retrieve this entry (list)
            entry = schedule [key]
        else:
            entry = []
        entry.append(record.getName())
        schedule [key] =entry

    for t in distinct_hours_dict:
        distinct_times.append(t)

    distinct_times.sort(key=lambda t: (t.getHour(), t.getMinute()))
