class String(str):    
    DEFAULT_REDACTION = '[REDACTED]'
    DEFAULT_SANITIZATION = '█'
    
    def redact(self):
        return ''.join([self.DEFAULT_REDACTION] * len(self.split()))

    def sanitize(self):
        return ''.join([self.DEFAULT_SANITIZATION if c.islower() and c.isalnum() else c for c in self])