import csv
import urllib2
import tempfile
import os
import hashlib

# returns list of hxl code parts
# i.e. #geo+bounds+json -> ['geo','bounds','json']
def get_hxl_code_parts(hxl_code):
    pass
    

class HxlDataSet(object):
    
    def __init__(self, remote_file=None, local_file=None):
        self.remote_file = remote_file
        self.local_file = local_file
        #self.hxl_data = []

    
    def __str__(self):
        result = 'HxlDataSet['
        if self.remote_file is not None:
            result += self.remote_file + ', '
        else:
            result += 'None, '
        if self.local_file is not None:
            result += self.local_file
        else:
            result += 'None'
        result += ']'
        return result

    
    def generate_local_filename(self):
        tmp_dir = tempfile.gettempdir()
        m = hashlib.md5()
        m.update(self.remote_file)
        #print(m.hexdigest())
        filename = 'hxl_' + m.hexdigest() + '.csv' #TODO: find a unique name for an url
        full_name = os.path.join(tmp_dir, filename)
        return full_name


    def download(self):
        remote_available = False
        if self.remote_file is None:
            raise Exception('No remote file defined')
            return
        response = urllib2.urlopen(self.remote_file)
        remote_available = True
        #raise Exception('Unable to download %s' % self.remote_file)
        if remote_available:
            fn = self.generate_local_filename()
            print(fn)
            f = open(fn, 'w')
            f.write(response.read())
            f.close()
            self.local_file = fn
        else:
            self.local_file = None
    
    
    def get_hxl_definitions(self):
        if self.local_file is None:
            print('No local file available')
            return
        # read first 2 lines:
        f = open(self.local_file, 'r')
        f.read
    
    def load_table(self):
        pass
