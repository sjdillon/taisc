# `taisc` - record streaming radio
[![Build Status](https://travis-ci.com/sjdillon/taisc.svg?branch=master)](https://travis-ci.com/sjdillon/taisc)
- captures streaming radio to files
- rotate files at a specified size
- records multiple streams in parallel
- [taisc](https://www.teanglann.ie/en/fgb/taisc) is the Irish word meaning **to store or hoard**


## Purpose
- Learning a new language?
  - Find and record a few streaming radio stations in the language.
  - Rewind, slow down the audio to aid learning
  - Have tons of content
  - Skip past the music
  
# Setup
```bash
$ virtualenv venv --python=python3
$ source venv/bin/activate
$ pip install git+https://github.com/sjdillon/taisc.git
```

# Using
```python
from taisc import Taisc

max_size_mb = 10
max_files = 9
stream0 = ('rnaf', 'https://radio.canstream.co.uk:9072/live.mp3')
stream1 = ('rnag', 'http://icecast2.rte.ie/rnag')
stream2 = ('rnal', 'http://beryl.streamguys.com:5010/live')
streams = [stream0, stream1, stream2]

runner = Taisc(streams=streams, max_size_mb=max_size_mb, max_files=max_files)
runner.run()

```

# Output
```bash
2021-04-17 07:39:29,639 - 140421557757760 - INFO - recording ('rnaf', 'https://radio.canstream.co.uk:9072/live.mp3') for 9 files
2021-04-17 07:39:29,641 - 140421557757760 - INFO - starting new file 1 mp3/rnaf_20210417_0739.mp3
2021-04-17 07:39:29,643 - 140421557757760 - INFO - recording ('rnag', 'http://icecast2.rte.ie/rnag') for 9 files
2021-04-17 07:39:29,645 - 140421557757760 - INFO - starting new file 1 mp3/rnag_20210417_0739.mp3
2021-04-17 07:39:29,646 - 140421557757760 - INFO - recording ('rnal', 'http://beryl.streamguys.com:5010/live') for 9 files
2021-04-17 07:39:29,648 - 140421557757760 - INFO - starting new file 1 mp3/rnal_20210417_0739.mp3
```