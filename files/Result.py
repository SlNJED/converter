class Result():
    def __init__(self, bytes=0, bits=0, nb=0, result=0):
        
        self.bytes = bytes      # bytes 
        self.bits = bits        # bits
        self.nb = nb            # original number
        self.result = result    # result
    
    def __repr__(self):
        return f"{self.nb}, ({self.bytes} bytes, {self.bits} bits): {self.result}"