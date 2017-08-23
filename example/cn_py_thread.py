import sys, os
import time
import threading


class CnPyThread(threading.Thread):
    def __init__(self, logmutex_arg, name_arg, mu_arg, sigma_arg):
        self.logmutex = logmutex_arg
        #self.name = name_arg
        #self.mu = mu_arg
        #self.sigma = signa_arg

        threading.Thread.__init__(self)

    def run(self):
        #self.logmutex.aquire()
        #print "thread " + name + " starting"
        #self.logmutex.release()
        #time.sleep(3.1415)
        #self.logmutex.aquire()
        #print "thread " + name + " ending"
        #self.logmutex.release()

        #
        # TODO:
        #   1. times for all events
        #   2. print times relative to start
        #
        with self.logmutex:
            print "thread " + self.name + " starting"
        time.sleep(3.1415)
        with self.logmutex:
            print "thread " + self.name + " ending"


