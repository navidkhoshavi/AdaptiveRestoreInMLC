#!/usr/bin/python -O

import sys
import re
#benchmark = sys.argv[1] # e.g., canneal

ftrace = open('../reuse_rows.dat', 'r')
#ftrace2 = open('../../llc_access_trace.log', 'r')


num_read_access_1_2 = 0
num_read_access_2_10 = 0
num_read_access_10_50 = 0
num_read_access_50_120 = 0
num_read_access_120_up1 = 0
num_read_access_up_up = 0

list_row_1_2 = [int(line.split()[0]) for line in open("1_2_pp.dat", 'r')]

list_row_2_10 = [int(line.split()[0]) for line in open("2_4_pp.dat", 'r')]

list_row_10_50 = [int(line.split()[0]) for line in open("4_8_pp.dat", 'r')]

list_row_50_120 = [int(line.split()[0]) for line in open("8_16_pp.dat", 'r')]
list_row_120_up1 = [int(line.split()[0]) for line in open("16_64_pp.dat", 'r')]
list_row_up_up = [int(line.split()[0]) for line in open("64_up_pp.dat", 'r')]

cycle = 0
list_iter_1_2 = len(list_row_1_2)
list_iter_2_10 = len(list_row_2_10)
list_iter_10_50 = len(list_row_10_50)
list_iter_50_120 = len(list_row_50_120)
list_iter_120_up1 = len(list_row_120_up1)
list_iter_up_up = len(list_row_up_up)

i = 0
#dont_add = 0
for line in ftrace:
    row = int(line.split()[0])

    # find read only cachelines
    if list_row_1_2.count(row) == 1:
            num_read_access_1_2 += int(line.split()[1])
    elif list_row_2_10.count(row) == 1:        
	    num_read_access_2_10 += int(line.split()[1])
    elif list_row_10_50.count(row) == 1:
            num_read_access_10_50 += int(line.split()[1])
    elif list_row_50_120.count(row) == 1:
            num_read_access_50_120 += int(line.split()[1])
    elif list_row_120_up1.count(row) == 1:
            num_read_access_120_up1 += int(line.split()[1])
    elif list_row_up_up.count(row) == 1:
            num_read_access_up_up += int(line.split()[1])
    else:
            continue


fout = open('bt_mem.dat', 'w')
# Access Pattern for 1-2, 2-4, 4-64, 64-up time cache line read only
print >>fout, "  1-2,   2-4,    4-8,  8-16,  16-64, 64-up"
print >>fout, " %-4d   %-4d  %-4d   %-4d    %-4d   %-4d " % (num_read_access_1_2, num_read_access_2_10, num_read_access_10_50,num_read_access_50_120, num_read_access_120_up1,num_read_access_up_up)
fout.close()



#ftrace2.close()
ftrace.close()

