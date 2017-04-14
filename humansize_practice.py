SUFFIXES = {1000:['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024:['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kiloyte_is_1024_bytes=True):
    '''This function gives the file size in human readable form
    
    Keywords:
                size -- gives the file size in bytes
                a_kiloyte_is_1024_bytes=True -- if True(default), use muliples of 1024
                                             -- if False, use multiples of 1000
                
                Returns string
    
    '''
    
    if (size < 0):
        raise ValueError('number must be non-negative')
   
    multiple = 1024 if a_kiloyte_is_1024_bytes else 1000
    
    for suffix in SUFFIXES[multiple]:
         size /= multiple
         if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('number is too large')
    
if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
    
        
        
        
        