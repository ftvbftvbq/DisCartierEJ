#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Deal with multi devices
    @ Author Juan
    @ data 2017.05.31
    @ Modifier:
"""

import Queue
import logging
import os
import subprocess
import threading

from conftest import disconnect_remote_session

logger = logging.getLogger(__name__)
q = Queue.Queue(0)
NUM_WORKERS = 3


class MyThread(threading.Thread):
    """
        A worker thread.
    """

    def __init__(self, input):
        self._jobq = input
        threading.Thread.__init__(self)

    def run(self):
        """
            Get a job and process it.
            Stop when there's no more jobs
        """
        while True:
            if self._jobq.qsize() > 0:
                job = self._jobq.get()
                serial = job["serial"]
                file = job["file"]
                self._process_job(file, serial)
            else:
                break

    def _process_job(self, file, serial):
        """
            Do useful work here.
        """
        logger.info(self.name + "\t begin to run " + serial)
        thread_name = self.name
        do_job(thread_name, file, serial)


def do_job(thread_name, file, serial):
    """
        Do work function 1
    """
    logger.info(thread_name + " begin to do job and the docker_compose address is " + file)
    os.chdir(file)
    if os.path.isdir(file):
        dc_files = os.listdir(file)
        for temp in dc_files:
            if temp.endswith(".yml"):
                try:
                    subprocess.call(["docker-compose up"], shell=True)
                except Exception as err:
                    logger.error(err)
                    disconnect_remote_session(serial)
                    logger.info(thread_name + " release session.")
                else:
                    logger.info(thread_name + " normal run!")
            else:
                pass
    else:
        os.system(thread_name + " this is not directory and cannot find docker_compose.yml to up! ")


def put_jobs(base_path=None):
    """
        put jobs in queue
    """
    logger.info("Begin to put jobs in queue......")
    base_path = os.path.abspath(base_path)
    files = os.listdir(base_path)
    for f in files:
        serial = f
        f = os.path.join(base_path, f)
        d = {"file": f, "serial": serial}
        q.put(d)
    logger.info("Put " + str(q.qsize()) + " job.....")
    return q


if __name__ == '__main__':
    print "begin..."
    # put some work to q
    # q = put_jobs(docker_composes_files_path)
    # # print total job q's size
    # print "job q'size", q.qsize()
    # # start threads to work
    # for x in range(NUM_WORKERS):
    #     MyThread(q).start()
