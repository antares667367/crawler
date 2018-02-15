from  .info import Info
from .debug import Debug
import os
import fnmatch
import magic
import hashlib
# setting useful vars
debuggen = Debug(internal_debug=True, color_output=True)
debuggen.setLogger(os.path.basename(__file__))
anzeigen = Info(enabled=True)

def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
        return h.hexdigest()

def crawl():
    rootPath = '/'
    pattern = '**'
    search = "ELF"
    count = 1

    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            if os.path.isfile(os.path.join(root,filename)) and not os.path.islink(os.path.join(root,filename)):
                try:
                    if search in magic.from_file(os.path.join(root, filename)):

                        _hash = file_hash(os.path.join(root,filename))
                        debuggen.log(os.path.join(root, filename),count,
                                   _hash)
                        count = count+1
                except Exception as e:
                    pass
                    # print(e.args)
                else:
                    pass

crawl()
