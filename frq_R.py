#!/usr/bin/python -O

import sys
import re
import os
#EPOCH = 1000000

#benchmark = sys.argv[1] # e.g., canneal
#tech = sys.argv[2] # e.g., sram_32nm_32MB_mix

ftrace = open('../reuse_rows.dat', 'r')
fout = open('bt_frq_R.dat', 'w')


# These variables have been changes several times. That's the reason they're not matched with the the output
num_row_read_1_8 = 0
num_row_read_8_32 = 0
num_row_read_32_128 = 0
num_row_read_128_up = 0
num_row_read_128_up2 = 0  
num_row_read_up_up = 0

list_frq_row_1_8 = [0] * (1000000)
list_frq_row_8_32 = [0] * (1000000)
list_frq_row_32_128 = [0] * (1000000)
list_frq_row_128_up = [0] * (1000000)
list_frq_row_128_up2 = [0] * (1000000)
list_frq_row_up_up = [0] * (1000000)

i = 0  #index for 1_8
j = 0  #index for 8_32
k = 0  #index for 32_128
l = 0  #index for 128_up
m = 0  #index for 128_up2
n = 0  #index for up-up
mem_access_to_Cache_sets = 282


print >>fout, "# of cache Lines which are read in the below range"
for line in ftrace:
    if int(line.split()[0]) == 0:
        continue
    elif int(line.split()[0]) != 0 and (int(line.split()[1]) != 0) and (mem_access_to_Cache_sets/int(line.split()[1])) < 2:
        num_row_read_1_8 += 1
        list_frq_row_1_8 [i] = int(line.split()[0])
        i += 1
    elif (int(line.split()[1]) != 0) and 2 <= (mem_access_to_Cache_sets/int(line.split()[1])) <= 4:
        num_row_read_8_32 += 1
        list_frq_row_8_32 [j] = int(line.split()[0])
        j += 1
    elif (int(line.split()[1]) != 0) and 4 < (mem_access_to_Cache_sets/int(line.split()[1])) <= 8:
        num_row_read_32_128 += 1
        list_frq_row_32_128 [k] = int(line.split()[0])
        k += 1
    elif (int(line.split()[1]) != 0) and 8 < (mem_access_to_Cache_sets/int(line.split()[1])) <= 16:
        num_row_read_128_up += 1
        list_frq_row_128_up [l] = int(line.split()[0])
        l += 1
    elif (int(line.split()[1]) != 0) and 16 < (mem_access_to_Cache_sets/int(line.split()[1])) <= 64:
        num_row_read_128_up2 += 1
        list_frq_row_128_up2 [m] = int(line.split()[0])
        m += 1
    elif (int(line.split()[1]) != 0) and 64 < (mem_access_to_Cache_sets/int(line.split()[1])):
        num_row_read_up_up += 1
        list_frq_row_up_up [n] = int(line.split()[0])
        n += 1
    else:
        continue
        
#for x in num_read_access:
print >>fout, "1-2,   2-4,    4-8,    8-16,    16-64,    64-up"
print >>fout, " %-4d   %-4d  %-4d    %-4d   %-4d    %-4d" % (num_row_read_1_8, num_row_read_8_32, num_row_read_32_128,num_row_read_128_up,num_row_read_128_up2, num_row_read_up_up)
fout.close()


# pring cache lines which have been read 1_8 in program execution
fout = open('1_2.dat', 'w')
for a in list_frq_row_1_8:
    print >>fout, a
fout.close()

# pring cache lines which have been read 8_32 in program execution
fout = open('2_8.dat', 'w')
for a in list_frq_row_8_32:
    print >>fout, a
fout.close()

# pring cache lines which have been read 32_128 in program execution
fout = open('8_16.dat', 'w')
for a in list_frq_row_32_128:
    print >>fout, a
fout.close()


# pring cache lines which have been read 128_up in program execution
fout = open('16_up.dat', 'w')
for a in list_frq_row_128_up:
    print >>fout, a
fout.close()


# pring cache lines which have been read 128_up2 in program execution
fout = open('16_up2.dat', 'w')
for a in list_frq_row_128_up2:
    print >>fout, a
fout.close()

# pring cache lines which have been read up_up in program execution
fout = open('up_up.dat', 'w')
for a in list_frq_row_up_up:
    print >>fout, a
fout.close()


############   Post Process ###############
with open("1_2.dat","r") as input:
    with open("1_2_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("1_2.dat")

with open("2_8.dat","r") as input:
    with open("2_4_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("2_8.dat")

with open("8_16.dat","r") as input:
    with open("4_8_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("8_16.dat")

with open("16_up.dat","r") as input:
    with open("8_16_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("16_up.dat")


with open("16_up2.dat","r") as input:
    with open("16_64_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("16_up2.dat")


with open("up_up.dat","r") as input:
    with open("64_up_pp.dat","wb") as output:
        for line in input:
            if int(line.split()[0]) != 0:
                output.write(line)
os.remove("up_up.dat")


#flog.close()
ftrace.close()

