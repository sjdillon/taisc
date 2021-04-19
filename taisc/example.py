import taisc

max_size_mb = 10
max_files = 9
stream0 = ('rnaf', 'https://radio.canstream.co.uk:9072/live.mp3')
stream1 = ('rnag', 'http://icecast2.rte.ie/rnag')
stream2 = ('rnal', 'http://beryl.streamguys.com:5010/live')
streams = [stream0, stream1, stream2]

proxies = None

runner = taisc.Taisc(streams=streams, max_size_mb=max_size_mb, max_files=max_files, proxies=proxies)
runner.run()
