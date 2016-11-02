#!/usr/bin/python -O

import sys
import re

ftrace = open('llc_access_trace.log', 'r')

read_odd_counter = 0
read_even_counter = 0
write_odd_counter = 0
write_even_counter = 0

line_num = []
a = 0
pre_state = -1

#########################  1st part ##############################
# RR ==> pre_state = 0, cur_state = 0   , SEU
# WR ==> pre_state = 2, cur_state = 0   , SEU
# WE ==> pre_state = 2, cur_state = 3   , SEU
# RE ==> pre_state = 0, cur_state = 3   , SEU
# RW ==> pre_state = 0, cur_state = 2
# WW ==> pre_state = 2, cur_state = 2
#LRR: Long RR
#MRR: Medium RR
#SRR: Short RR

#LWR: Long WR
#MWR: Medium WR
#SWR: Short WR

#LWE: Long WE
#MWE: Medium WE
#SWE: Short WE

#LRE: Long RE
#MRE: Medium RE
#SRE: Short RE

for line in ftrace:
    pre_state = int(line.split()[1])
    row = int(line.split()[2])

    # If the memory operation is read, count hom many even and odd cache lines have been read
    if pre_state == 0:
        if row in line_num:
            a += 1
        else:
            line_num.append(row)
        if (row % 2) == 0:
            read_even_counter += 1
        else:
            read_odd_counter += 1
    # If the memory operation is write, count hom many even and odd cache lines have been written
    elif (pre_state == 1) or (pre_state == 2) or (pre_state == 5):
        if row in line_num:
            a += 1
        else:
            line_num.append(row)
        if (row % 2) == 0:
            write_even_counter += 1
        else:
            write_odd_counter += 1
fout = open('Bodytrack_RW_Even-odd.dat', 'w')
print >> fout, "Read_even,Read_odd,Write_even,Write_Odd"
print >> fout, "%-7s %-7s %-7s %-7s" % (read_even_counter, read_odd_counter, write_even_counter, write_odd_counter)

ftrace.close()
fout.close()
