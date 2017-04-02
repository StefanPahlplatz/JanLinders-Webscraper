import progressbar as p
import time

for i in range(0, 100):
    p.Progressbar.print_progress(i, 100, "Progress", "Complete", bar_length=50)
    time.sleep(.2)
