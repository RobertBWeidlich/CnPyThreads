import sys, io, time
import threading
import random

from cn_py_thread import CnPyThread

if __name__ == '__main__':
    def main():
        count = 0
        iterations = 10
        INTERVAL = 5.0
        MU = 25.0
        SIGMA = 10.0

        if True:
            print "iterations: " + str(iterations)
            print "intervals:  " + str(INTERVAL)
            print "mu:         " + str(MU)
            print "sigma:      " + str(SIGMA)

        random.seed()
        if False:
            for i in range(0, 100):
                #r = random.gauss(100.0, 1.0)
                r = random.gauss(0.0, 1.0)
                print r
            sys.exit(0)

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
            #print "awake:        " + str(time.time())
            thread = CnPyThread(logmutex, "thr-" + str(count+1), MU, SIGMA)
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
        # todo: catch terminating threads, exit when last one is finished
        #
        time.sleep(MU * 4.0)
        print "terminationg process"


if __name__ == "__main__":
    main();
    sys.exit(0)
