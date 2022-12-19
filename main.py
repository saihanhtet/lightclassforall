import webview
import threading
from subprocess import Popen,PIPE,STARTUPINFO,STARTF_USESHOWWINDOW
from signal import CTRL_BREAK_EVENT

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        global p
        p = Popen(['python', 'C:\\light\\lightclassforall\\manage.py', 'runserver'],startupinfo=startupinfo,stderr=PIPE, stdout=PIPE)
        
    
    def stop(self):
        print ("Exiting server")
        p.send_signal(CTRL_BREAK_EVENT)
        p.wait()    

thread = myThread()
thread.start()
try:
    webview.create_window('Light Class For All', 'http://127.0.0.1:8000/',width=1200, height=700, resizable=True, fullscreen=False, background_color='#2b2b2b')  
    webview.start()
except:
    print('error ocurred')

# start the process

thread.stop()
# now stop the process

