n = 16
with open('foobar.file', 'rb') as fp:
    while True:
        chunk = fp.read(n)
        if not chunk: # end of file, stop running.
            break
        print(chunk)
        # process(chunk)