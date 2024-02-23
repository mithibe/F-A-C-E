from screeninfo import get_monitors

def get_screen_size():
    monitors = get_monitors()
    if monitors:
        monitor = monitors[0]
        width = monitor.width
        height = monitor.height
        return width, height
    else:
        return None
    
screen_size = get_screen_size()
if screen_size:
    print("Screen Width: ", screen_size[0])
    print("Screen Height: ", screen_size[1])
else:
    print("Screen size not available.")

screen_width = screen_size[0]
screen_height = screen_size[1]