volume = 1.44
pages = 100
lines = 50
chars = 25
bytes_in_char = 4
print('количество книг:', int(volume*1024**2 // (pages * lines * chars * bytes_in_char)))