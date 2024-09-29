#

def get_hour (epoch_seconds):
    result = epoch_seconds // 3600
    remainder = result % 24
    return remainder

def get_minutes (epoch_seconds):
    result = epoch_seconds // 60
    remainder = result % 60
    return remainder

def get_seconds (epoch_seconds):
    result = epoch_seconds % 3600
    remainder = result % 60
    return remainder
