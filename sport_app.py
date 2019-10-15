from load import *
from tkinter import *
from tkinter import messagebox
from time import *
from datetime import datetime

time_var = None

window = None
row_dict = {}


def update_time():
    time_var.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+", "+str_current_day)
    timer = window.after(1000, update_time)

def next_class_message ():
    now = datetime.now()
    print("weekday: "+str(now.weekday()))
    print ("hour: "+str(now.hour))
    for record in data_records:
        if record.getDay() == current_weekday and record.getHour() > now.hour:
            messagebox.showinfo("NOW!", record.getName() + " starts at "+ time_am_pm (record.getHour(), record.getMinute()))
            #print (record.getName())
            #print ("starts at "+ time_am_pm (record.getHour(), record.getMinute()))
            return
    messagebox.showwarning("No more exercise classes today!")

load_data()
current_weekday = datetime.now().weekday()
str_current_day = weekdays[current_weekday]


window = Tk()
window.title("Exercise now!")
time_var = StringVar()

frame = Frame (window, bg='white', border=5, relief=RIDGE)


#fill in days of week
colid = 1
for day in days_of_week:
    Label(frame, text=day,borderwidth=2,relief=GROOVE,fg='lightyellow',bg='darkblue',height=2,font=("Helvetica", 16)).grid (row=0, column = colid,  sticky='EW')
    colid +=1

r=1
for time_record in distinct_times:
    txt = time_am_pm(time_record.getHour(), time_record.getMinute())

    Label(frame, text=txt, borderwidth=2,relief=GROOVE,fg='lightyellow',bg='darkblue',height=2,font=("Helvetica", 16)).grid(row=r, column=0, sticky='EW')
    row_dict [time_record] = r
    r += 1

for record in data_records:
    c = record.getDay()+1
    timeRecord = Time24(record.getHour(), record.getMinute())
    r = row_dict [timeRecord]

    Label (frame, text = record.getName()[0:14], borderwidth=2,relief=RAISED,bg='white',font = "Verdana 14 italic").grid(row=r, column = c, sticky='EW')

frame.pack()

#last row - current time, and find next exercise
(Label(window,text="       ", height=2,font=("Helvetica", 16))).pack(side="right")
b = Button(window, text="Next Class!", command=next_class_message, fg='lightyellow', bg='darkred',height=1,font=("Helvetica", 16))
b.pack(side="right")
(Label(window,text="       ", height=2,font=("Helvetica", 16))).pack(side="right")
time_label = Label(window,textvariable=time_var, height=2,font=("Helvetica", 16))
time_label.pack(side="right")
(Label(window,text="Today: ", height=2,font=("Helvetica", 16))).pack(side="right")
update_time ()
window.mainloop()






#print (data_records)

#print (distinct_times)

#print (schedule)