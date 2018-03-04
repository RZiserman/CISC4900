#!/usr/bin/env python

#Reference: Hussein Ghaly

import subprocess, os, time

connl_dir="connl"
out_dir="malt_parsed"
my_cwd = os.getcwd()

#Time the execution of this script
t0=time.time()

for fname in os.listdir(connl_dir):
    connl_file_path=os.path.join(connl_dir, fname)
    out_file_path=os.path.join(out_dir, fname)
    parser_command=" java -Xmx1024m -jar maltparser-1.8.1.jar -c engmalt.poly-1.7.mco -i %s -o %s -m parse "%(connl_file_path , out_file_path )
    proc=subprocess.Popen(parser_command, shell=True, cwd=my_cwd)
    proc.wait()

t1=time.time()
elapsed=t1-t0

with open(out_dir + '/TOTAL_RUN_TIME.txt', 'w') as tot_time:
    print>>tot_time, "Total runtime: " + str(elapsed)
