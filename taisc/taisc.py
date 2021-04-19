#!python
# ==========================================================#
# title          :taisc.py
# description    :helps record streaming radio
# author         :sjdillon
# date           :04/04/2021
# python_version :3.7
# ==========================================================================
import datetime
import logging
import multiprocessing as mp
import os

import requests

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Taisc:
    """ Records streaming audio """

    def __init__(self, streams, max_size_mb, max_files, date_fmt='%Y%m%d_%H%M', file_ext='mp3', proxies=None,
                 folder='mp3'):
        self.streams = streams
        self.max_size = max_size_mb * 1024 * 1024
        self.max_files = max_files
        self.date_fmt = date_fmt
        self.file_ext = file_ext
        self.folder = folder
        self.proxies = proxies

    def capture(self, stream_url, filename, max_size):
        r = requests.get(stream_url, stream=True, proxies=self.proxies)
        with open(filename, 'wb') as f:
            for block in r.iter_content(1024):
                f.write(block)
                if f.tell() > max_size:
                    return False

    def make_file_name(self, root_name):
        self.make_folder()
        file_name = datetime.datetime.now().strftime(f"{root_name}_{self.date_fmt}.{self.file_ext}")
        return os.path.join(self.folder, file_name)

    def make_folder(self):
        if not os.path.exists(self.folder):
            logger.info(f'creating folder {self.folder}')
            os.makedirs(self.folder)
        return True

    def record(self, stream):
        logger.info(f'recording {stream} for {self.max_files} files')
        stream_name = stream[0]
        stream_url = stream[1]
        cnt = 0
        while cnt < self.max_files:
            cnt += 1
            file_name = self.make_file_name(stream_name)
            logger.info(f'starting new file {cnt} {file_name}')
            self.capture(stream_url, file_name, self.max_size)
        logger.info('done!')

    def run(self):
        """
        record all the streams in parallel
        """
        tasks = []
        for stream in self.streams:
            task = mp.Process(target=self.record, args=[stream])
            task.start()
            tasks.append(task)
        for t in tasks:
            t.join()
