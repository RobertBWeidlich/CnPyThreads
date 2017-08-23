import sys, io, time
import threading

if __name__ == '__main__':
    def main():
        count = 0
        #iterations = 10
        #INTERVAL = 15.0
        iterations = 60
        INTERVAL = 1.0

        #
        # stop on clean intervals -- for example, if INTERVAL is 10.0, then
        # stop at the top of the minute, 10 seconds after the minute,
        # 20 seconds after the minute, etc
        #
        t_now = time.time()
        t_wakeup = float(int(t_now) - (int(t_now) % INTERVAL) + INTERVAL)
        t_sleep = t_wakeup - t_now

        while count < iterations:
            time.sleep(t_sleep)

            # do something
            print "awake:        " + str(time.time())

            time.sleep(t_sleep/16.0)  # bump up the clock
            t_now = time.time()
            t_wakeup = float(int(t_now) - (int(t_now) % INTERVAL) + INTERVAL)
            t_sleep = t_wakeup - t_now

            count += 1

        print "finished"

if __name__ == "__main__":
    main();
    sys.exit(0)
