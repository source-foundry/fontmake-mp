#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ================================================================
#  fmp.py
#    Parallel fontmake font builds from UFO source
#
#   Copyright 2017 Christopher Simpkins
#   MIT License
# ================================================================

import sys
import os
import traceback

from multiprocessing import Lock, Pool, cpu_count
from fontmake.font_project import FontProject

PROCESSES = 0
build_file_type = ('ttf', 'otf')

lock = Lock()


def main(argv):
    processes = PROCESSES

    source_path_list = argv

    # Command line error handling
    if len(source_path_list) == 0:
        sys.stderr.write("[ERROR] Please include one or more paths to UFO source directories as " 
                         "arguments to the script." + os.linesep)
        sys.exit(1)

    # TODO: add .ufo file extension check + confirmation that directory path exists

    print(" ")
    print("[*] Beginning compile...")

    if len(source_path_list) == 1:
        # there is only one source compile necessary, skip spawning of processes and just build it
        print("[*] Single font compile requested. Concurrency is not necessary.  No additional processes spawned...")
        print(" ")
        build_fonts(source_path_list[0])
        sys.exit(0)
    else:
        # if not defined by user, start by defining spawned processes as number of available cores
        if processes == 0:
            processes = cpu_count()
            print("[*] Detected " + str(cpu_count()) + " cores...")
        else:
            print("[*] User request to spawn " + str(processes) + " processes for compilation...")

        # if total cores available is greater than number of font compiles requested, limit to the latter number
        if processes > len(source_path_list):
            processes = len(source_path_list)
            print("[*] Limiting spawned process number to the number of font compiles "
                  "(" + str(processes) + ")...")

        print("[*] Output from fontmake will appear out of order below. This is expected...")
        print(" ")
        print(" ")

        p = Pool(processes)
        p.map(build_fonts, source_path_list)


def build_fonts(ufo_path):
    try:
        fp = FontProject()
        fp.run_from_ufos(ufo_path, output=build_file_type)
    except Exception as e:
        lock.acquire()
        print(" ")
        print("[ERROR] The fontmake compile for " + ufo_path + " failed with the following error"
              ":" + os.linesep)
        sys.stdout.flush()
        traceback.print_exc()
        print(str(e))
        sys.stdout.flush()
        lock.release()


if __name__ == '__main__':
    main(sys.argv[1:])
