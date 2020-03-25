
num_repeats = 60 
OUTFILE = "out.mp3"
pre="#!/bin/bash"
com="ffmpeg "
base_file="r.mp3"

inputs=""

for i in range(0,num_repeats+1):
    inputs=inputs+"-i "+base_file+" "

print(pre)
print("")
print(com+inputs+"-vn \\")
print("-filter_complex \\")
print("\" \\")
print("[0][1]acrossfade=d=10:c1=tri:c2=tri[a01]; \\")

for i in range(1,num_repeats-1):
    print("[a0"+str(i)+"]["+str(i+1)+"]acrossfade=d=10:c1=tri:c2=tri[a0"+str(i+1)+"]; \\")    
i=i+1
print("[a0"+str(i)+"]["+str(i+1)+"]acrossfade=d=10:c1=tri:c2=tri\" \\")    
print(OUTFILE)
