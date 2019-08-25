import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Panah Kanan Kiri')
print(b+'\t        Official TCT')
print('\t          NO TOXIC NO LIFE')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!] Behasil Gan :v')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Leh Ugha Berhasil :v')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Simsalabim Dah Munculkan? ^_^'+c+'\n\nJangan Lupa Subscribe Channel : Makky 2693 :*\n\n')


# ini cuma shortcut buat bantu para nub
# Toxic Cyber Team
