
from os import rename, listdir

badprefix = "xyz " #Annoying prescript that is bad and you want to remove
fnames = listdir('.')
print(fnames)

for fname in fnames:
    if fname.startswith(badprefix):
        rename(fname, fname.replace(badprefix, '', 1))
