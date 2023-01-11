
# Shutdown_or_restart_your_device using Python
# https://teamerror.net

import os
import platform
# Power manager Class
class PowerManager():
    # Shutdown Function
    def shutdown(self):
        if platform.system() == "Windows":
            os.system('shutdown -s')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("shutdown -h now")
        else:
            print("Os not supported!")
    # Restart Function
    def restart(self):
        if platform.system() == "Windows":
            os.system("shutdown -t 0 -r -f")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system('reboot now')
        else:
            print("Os not supported!")
# Server start Function
def runserver():
    command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()
    task =PowerManager()
    if command == "r":
        task.restart()
    elif command == "s":
        task.shutdown()
    else:
        print("Wrong letter")

runserver()

