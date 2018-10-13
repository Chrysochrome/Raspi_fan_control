from fan_util import fan_util
from cpu_util import cpu_util
import time
import atexit

fan_util_ins = fan_util()
cpu_util_ins = cpu_util()

# def main():
#     while True:
#         fan_util_ins.set_stat(True)
#         time.sleep(7)
#         fan_util_ins.set_stat(False)
#         time.sleep(7)

# def done():
#     fan_util_ins.set_stat(False)
#     # fan_util_ins.cleanup()
#     print("Fan stopped.")

# if __name__ == "__main__":
#     atexit.register(done)
#     main()

while True:
    print(cpu_util_ins.get_temp(), cpu_util_ins.get_useage())
    time.sleep(3)
