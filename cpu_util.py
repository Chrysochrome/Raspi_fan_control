import os
import time


class cpu_util():
    def get_temp(self):
        file = open("/sys/class/thermal/thermal_zone0/temp")
        temp = float(file.read()) / 1000
        file.close()
        return temp

    def get_useage(self):
        time1 = os.popen('cat /proc/stat').readline().split()[1:5]
        time.sleep(0.2)
        time2 = os.popen('cat /proc/stat').readline().split()[1:5]
        deltaUsed = int(time2[0])-int(time1[0])+int(time2[2])-int(time1[2])
        deltaTotal = deltaUsed + int(time2[3])-int(time1[3])
        cpuUsage = float(deltaUsed)/float(deltaTotal)*100
        return cpuUsage
