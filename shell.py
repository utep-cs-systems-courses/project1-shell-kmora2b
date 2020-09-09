import os,re,sys

try:
    ps1_char = sys.argv[1]
except:
    ps1_char = "$"

sys.ps1 = ps1_char
print(sys.ps1)