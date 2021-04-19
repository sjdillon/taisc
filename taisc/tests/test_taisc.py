#!python
# ==========================================================#
# project        :sjdillon
# title          :test_taisc.py
# description    :unit test taisc
# author         :sjdillon
# date           :04/17/2021
# python_version :3.7
# notes          :
# ==========================================================#
import logging
import os

import taisc

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

max_size_mb = 10
max_files = 9
stream0 = ('rnaf', 'https://radio.canstream.co.uk:9072/live.mp3')
stream1 = ('rnag', 'http://icecast2.rte.ie/rnag')
streams = [stream0, stream1]


def test_make_file_name():
    folder = 'recordings'
    file = 'radio'
    runner = taisc.Taisc(streams=streams, max_size_mb=max_size_mb, max_files=max_files, folder=folder)
    file_name = runner.make_file_name(file)
    assert file_name.startswith(os.path.join(folder, file))
