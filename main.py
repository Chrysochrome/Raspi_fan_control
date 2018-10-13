from control import control
import atexit

ctrl = control()
def main():
    ctrl.run()

def done():
    ctrl.clean()

if __name__ == "__main__":
    atexit.register(done)
    main()
