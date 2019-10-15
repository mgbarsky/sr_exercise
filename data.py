from utils import *

class Exercise(object):

    def __init__(self, name="", day=0, hour=0, minute=0):
        self.name = name
        self.day = day
        self.hour = hour
        self.minute = minute

    def getName(self):
        return self.name

    def getDay(self):
        return self.day

    def getHour(self):
        return self.hour

    def getMinute (self):
        return self.minute

    def setName(self, name):
        self.name = name

    def setDay(self, day):
        self.day = day

    def setHour(self, hour):
        self.hour = hour

    def setMinute (self, minute):
        self.minute = minute

    def __str__(self):
        return "%s: starts on %s at %s:%s" % (self.name, days_of_week[self.day], self.hour, self.minute)

    def __repr__(self):
        return (str(self))


class Time24 :
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def getHour(self):
        return self.hour

    def getMinute (self):
        return self.minute

    def __hash__(self):
        return hash((self.hour, self.minute))

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self):
        return "%s:%s" % (str(self.hour), str(self.minute))

    def __repr__(self):
        return (str(self))

def data_label (record):
    day = days_of_week[record.getDay()]
    hour_min = time_am_pm(record.getHour(), record.getMinute())
    return day + " " + hour_min

if __name__ == '__main__':
    #print("This only executes when %s is executed rather than imported" % __file__)
    records = []
    for i in range(5):
        e = Exercise ("exercise"+str(i), i, i, i+1)
        records.append(e)

    print(records)
    #strrecords = [ str(x) for x in records ]
    print ([ str(x) for x in records ])

