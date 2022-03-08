from zipfile import ZipFile

# membuat zip file
zipObj = ZipFile('sample.zip', 'w')

# file yang di masukan ke zip
# disini saya memasukan file std.py yang ada di direktori saya

zipObj.write('std.py')

# untuk menutup zip file
zipObj.close()
