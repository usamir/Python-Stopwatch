# template for "Stopwatch"

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
interval = 100
tenth_of_second = 0
width = 300
height = 200
formatted_time = ""
wins = 0
totals = 0
count_stop = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    m_sec = t % 10
    m_sec = str(m_sec)
    secs = t // 10
    mins = secs // 60
    secs2mins = secs - mins * 60
    secs = str(secs2mins)
    mins = str(mins)

    if(secs2mins < 10):
        secs = "0" + secs
   
    return mins + ":" + secs + "." + m_sec 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_stopwatch():
    global count_stop
    count_stop = 0
    timer.start()
    
def stop_stopwatch():
    timer.stop()
    
    global totals, wins, count_stop
    if(count_stop == 0):
        totals += 1
        if (tenth_of_second % 10 == 0):
            wins +=  1
        count_stop += 1
    
def reset_stopwatch():
    global tenth_of_second, wins, totals, count_stop
    tenth_of_second = wins = totals = count_stop = 0
    
    global formatted_time
    formatted_time = format(tenth_of_second)
    timer.stop()
   
# define event handler for timer with 0.1 sec interval
def tick():
    global tenth_of_second
    tenth_of_second += 1
    
    global formatted_time
    formatted_time = format(tenth_of_second)

# define draw handler
def draw(canvas):
    global formatted_time, wins, totals
    canvas.draw_text(formatted_time, [20, 120], 40, "Red")
    game_info = str(wins) + "/" + str(totals)
    canvas.draw_text(game_info, [150, 20], 15, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)

# register draw handler    
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, tick)

frame.add_button("Start", start_stopwatch, 100)
frame.add_button("Stop", stop_stopwatch, 100)
frame.add_button("Reset", reset_stopwatch, 100)

# start timer and frame

frame.start()
