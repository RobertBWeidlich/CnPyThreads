import sys, io, time
import threading

from cn_py_thread import CnPyThread

if __name__ == '__main__':
    def main():
        count = 0
        #iterations = 10
        #INTERVAL = 15.0
        iterations = 60
        INTERVAL = 5.0

        #
        # stop on clean intervals -- for example, if INTERVAL is 10.0, then
        # stop at the top of the minute, 10 seconds after the minute,
        # 20 seconds after the minute, etc
        #
        t_now = time.time()
        t_wakeup = float(int(t_now) - (int(t_now) % INTERVAL) + INTERVAL)
        t_sleep = t_wakeup - t_now

        logmutex = threading.Lock()
        while count < iterations:
            time.sleep(t_sleep)

            # do something
            print "awake:        " + str(time.time())
            thread = CnPyThread(logmutex, "rbw-thr-" + str(count), 15.0, 5.0)
            thread.start()

            #
            # calculate time before next event
            #
            time.sleep(t_sleep/16.0)  # bump up the clock
            t_now = time.time()
            t_wakeup = float(int(t_now) - (int(t_now) % INTERVAL) + INTERVAL)
            t_sleep = t_wakeup - t_now

            count += 1

        print "finished launching threads -- waiting for them all to complete"
        #
        # todo: how do we catch terminating threads?
        #
        time.sleep(60.00)
        print "terminationg process"


if __name__ == "__main__":
    main();
    sys.exit(0)
