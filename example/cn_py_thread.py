import sys, os
import time
import threading
import random

def get_duration():
    r = random.gauss(25.0, 10.0)
    return r


class CnPyThread(threading.Thread):
    def __init__(self, logmutex_arg, name_arg, mu_arg, sigma_arg):
        self.logmutex = logmutex_arg
        self.t_name = name_arg
        self.mu = mu_arg
        self.sigma = sigma_arg

        threading.Thread.__init__(self)

    def run(self):
        #self.logmutex.aquire()
        #print "thread " + t_name + " starting"
        #self.logmutex.release()
        #time.sleep(3.1415)
        #self.logmutex.aquire()
        #print "thread " + t_name + " ending"
        #self.logmutex.release()

        #
        # TODO:
        #   1. times for all events
        #   2. print times relative to start
        #
        dur = get_duration();
        with self.logmutex:
            print "thread " + self.t_name + " starting, running for " + str(dur) + " seconds"
            ct = threading.current_thread
            #print "thread " + self.t_name + " starting " + str(ct)
        time.sleep(dur)
        with self.logmutex:
            print "thread " + self.t_name + " ending"


