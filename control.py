from fan_util import fan_util
from cpu_util import cpu_util
import time


class control():
    fan_util_ins = fan_util()
    cpu_util_ins = cpu_util()

    def run(self):
        while True:
            temp = self.cpu_util_ins.get_temp()
            useage = self.cpu_util_ins.get_useage()
            is_on = self.fan_util_ins.get_stat()
            if is_on == 1:
                if temp <= 55 and useage <= 30:
                    self.fan_util_ins.invert()
            else:
                if temp >= 65 and useage >= 60:
                    self.fan_util_ins.invert()
            #print("temp %.1f, uesage %.1f, fan %s" % (temp, useage, self.fan_util_ins.get_stat()))
            time.sleep(3)

    def clean(self):
        self.fan_util_ins.set_stat(False)
