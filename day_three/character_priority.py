priority_table = '~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(c: chr) -> int:
    return priority_table.find(c)