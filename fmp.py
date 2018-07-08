#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ===================================================================
#  fmp.py
#    Concurrent font compilation from UFO source files with fontmake
#
#   Copyright 2018 Christopher Simpkins
#   MIT License
#
#   Source Repository: https://github.com/source-foundry/fontmake-mp
# ===================================================================

import os
import sys
import timeit
import traceback

from multiprocessing import Lock, Pool, cpu_count
from fontmake.font_project import FontProject

PROCESSES = 0

lock = Lock()

VERSION_NUMBER = "1.0.0"
VERSION = "fontmake-mp v" + VERSION_NUMBER
USAGE = "[./fmp.py|fontmake-mp] (--ttf|--otf) [UFO file path 1] (UFO file path ...)"
HELP = """
===================================================================
 fontmake-mp
   Parallel font compilation from UFO source files with fontmake

   Copyright 2018 Christopher Simpkins
   MIT License

   Source Repository: https://github.com/source-foundry/fontmake-mp
====================================================================

fontmake-mp compiles *.otf and/or *.ttf font binaries from UFO source files in parallel.

Execute fontmake-mp with the fmp.py Python script (located in the root of repository) or the fontmake-mp executable (located in the repository releases).

Usage:
  Execution of Python script:
     $ python fmp.py (--ttf|--otf) [UFO file path 1] (UFO file path ...)

  Execution of executable file installed on system PATH
     $ fontmake-mp (--ttf|--otf) [UFO file path 1] (UFO file path ...)

Options:
  --otf          Build *.otf files only (optional, default=*.otf AND *.ttf)
  --ttf          Build *.ttf files only (optional, default=*.otf AND *.ttf)

  -h, --help     Display help text
      --usage    Display application usage
  -v, --version  Display application version

Fonts are compiled in the working directory on the directory path(s) master_otf and/or master_ttf.
"""


def main(argv):
    if len(argv) == 0:
        sys.stderr.write(
            "[ERROR] Please include at least one UFO path in your command." + os.linesep
        )
        sys.exit(1)
    # help, version, usage flag handling
    if argv[0] in ("-h", "--help"):
        print(HELP)
        sys.exit(0)
    elif argv[0] in ("-v", "--version"):
        print(VERSION)
        sys.exit(0)
    elif argv[0] == "--usage":
        print(USAGE)
        sys.exit(0)

    processes = PROCESSES

    # define the build file types in the request
    build_file_types = []
    if "--ttf" in argv:
        build_file_types.append("ttf")
    if "--otf" in argv:
        build_file_types.append("otf")

    if len(build_file_types) == 0:
        build_file_types.append("ttf")
        build_file_types.append("otf")

    # create source path list with single UFO path per build type
    # definition in order to parallelize builds across otf/ttf types
    source_path_list = []
    for arg in argv:
        if arg[0] == "-":
            pass
        else:
            for build_type in build_file_types:
                # create a tuple of (source file path, build type)
                source_path_list.append((arg, build_type))

    # Command line error handling
    if len(source_path_list) == 0:
        sys.stderr.write(
            "[ERROR] Please include one or more paths to UFO source directories as "
            "arguments to the script." + os.linesep
        )
        sys.exit(1)

    for source_path_tuple in source_path_list:
        if len(source_path_tuple[0]) < 5:  # not a proper *.ufo file path
            sys.stderr.write(
                "[ERROR] '"
                + source_path_tuple[0]
                + "' is not properly formatted as a path to a UFO source "
                "directory" + os.linesep
            )
            sys.exit(1)
        elif not source_path_tuple[0][-4:] == ".ufo":  # does not end with .ufo
            sys.stderr.write(
                "[ERROR] '"
                + source_path_tuple[0]
                + "' does not appear to be a UFO source directory"
                + os.linesep
            )
            sys.exit(1)
        elif not os.path.isdir(source_path_tuple[0]):  # is not an existing directory
            sys.stderr.write(
                "[ERROR] '"
                + source_path_tuple[0]
                + "' does not appear to be a valid path to a UFO source "
                "directory" + os.linesep
            )
            sys.exit(1)

    # begin compile
    print(" ")
    print("[*] Beginning fontmake-mp font compile...")

    if len(source_path_list) == 1:
        # there is only one source compile necessary, skip spawning of processes and just build it
        print("[*] Single font compile requested. No additional processes spawned...")
        print(" ")

        # begin compile
        start_time = timeit.default_timer()

        build_fonts(source_path_list[0])

        elapsed_time = timeit.default_timer() - start_time
        elapsed_time_string = "{0:.2f}".format(elapsed_time)
        print(os.linesep + os.linesep + "---")
        print("Build complete in " + elapsed_time_string + " seconds!")
        if "ttf" in build_file_types:
            print("*.ttf fonts in master_ttf directory")
        if "otf" in build_file_types:
            print("*.otf fonts in master_otf directory")
        sys.exit(0)
    else:
        # if not defined by user, start by defining spawned processes as number of available cores
        if processes == 0:
            processes = cpu_count()
            print("[*] Detected " + str(cpu_count()) + " cores...")
        else:
            print("[*] Spawning " + str(processes) + " processes for the compile...")

        # if total cores available is greater than number of font compiles requested, limit to the latter number
        if processes > len(source_path_list):
            processes = len(source_path_list)
            print(
                "[*] Limiting spawned process number to the number of font compiles needed "
                "(" + str(processes) + ")..."
            )

        print(
            "[*] Output from the fontmake compiler will appear out of order below. This is expected..."
        )
        print(" ")
        print(" ")

        # begin compile
        start_time = timeit.default_timer()

        p = Pool(processes)
        p.map(build_fonts, source_path_list)

        elapsed_time = timeit.default_timer() - start_time
        elapsed_time_string = "{0:.2f}".format(elapsed_time)
        print(os.linesep + os.linesep + "---")
        print("Build complete in " + elapsed_time_string + " seconds!")
        if "ttf" in build_file_types:
            print("*.ttf fonts in master_ttf directory")
        if "otf" in build_file_types:
            print("*.otf fonts in master_otf directory")
        sys.exit(0)


def build_fonts(ufo_path_tuple):
    """build_fonts uses fontmake to build fonts from UFO source files with
       the definitions in the ufo_path_tuple that is defined as
       (UFO source path, build file type)"""
    try:
        fp = FontProject()
        fp.run_from_ufos(ufo_path_tuple[0], output=ufo_path_tuple[1])
    except Exception as e:
        lock.acquire()
        print(" ")
        print(
            "[ERROR] The fontmake compile for "
            + ufo_path_tuple[0]
            + " failed with the following error"
            ":" + os.linesep
        )
        sys.stdout.flush()
        traceback.print_exc()
        print(str(e))
        sys.stdout.flush()
        lock.release()


if __name__ == "__main__":
    main(sys.argv[1:])
