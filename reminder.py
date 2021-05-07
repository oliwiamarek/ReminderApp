#%% IMPORTS
import time
import datetime
import tkinter as tk
from tkinter import messagebox as mb
import winsound 
print("Start reminder application")

#%% ############################################################
# VARIABLES ####################################################
################################################################

# Editable
time_interval = 3600 # in seconds
activity_title = 'stretching'
activity_check = 'stretch'
total_breaks = 3

break_count = 0
now = datetime.datetime.now()
start_of_day = now.replace(hour=8, minute=30, second=0, microsecond=0)
end_of_day =  now.replace(hour=17, minute=00, second=0, microsecond=0)
force_exit_time =  now.replace(hour=19, minute=00, second=0, microsecond=0)
root= tk.Tk()
print("variables created")

#%% ############################################################
# FUNCTIONS ####################################################
################################################################
def create_canvas(root):
    root.title("Did you do your {}?".format(activity_title))
    # Gets the requested values of the height and widht.
    window_width = 400#root.winfo_reqwidth()
    window_height = 40#root.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    
    # Positions the window in the center of the page.
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, position_right, position_down))

def get_miliseconds_as_string():
    seconds=int(time_interval)%60
    minutes=int(time_interval/60)%60
    hours=int(time_interval/(60*60))%24
    final_string = ""
    if hours > 0:
        final_string += "%d hours" % (hours)
    if minutes > 0:
        final_string += "%d minutes" % (minutes)
    if seconds > 0:
        final_string += "%d seconds" % (seconds)
    return final_string

def callback():
    global break_count
    activity_done = mb.askyesno('Hmmmm....', 'Did you REALLY {}?'.format(activity_check))

    if activity_done:
        time_string = get_miliseconds_as_string()
        hi = mb.showinfo('Actually moved your butt!', 'Good job! See you in {}.'.format(time_string))
        root.destroy()
    elif break_count > total_breaks:
        mb.showerror('Ok, that is enough!', 'You cancelled too many times. Do it right now!')
        return
    else:
        mb.showerror('What!', 'You are so lazy! Do it right now!')
        break_count = break_count + 1
    
def too_early():
    tk().withdraw() # we don't want a full root, so keep the root window from appearing
    mb.showinfo('Too early', 'Why are you working already? Go back to sleep.')

def too_late():
    tk().withdraw() # we don't want a full root, so keep the root window from appearing
    mb.showinfo('End of the day', 'Go and do non-work-related stuff!') 

print("defs setup")

#%% ############################################################
# MAIN LOOP ####################################################
################################################################
while(now < force_exit_time):
    break_count = 0
    now = datetime.datetime.now()
    
    if now < start_of_day:
        too_early()
    elif now > end_of_day:
        too_late()
    else:
        root= tk.Tk()
        create_canvas(root)
        mb.showwarning('HEY!', 'It is time for your reminder again!')
        tk.Button(text='Done.', command=callback).pack(fill=tk.X)
        tk.mainloop()
    
    time.sleep(time_interval)

# Close dialog if it's very late
root.destroy()  
