
num_repeats = 60

pre="#!/bin/bash"
com="ffmpeg \\"
base_file="r.mp3"

inputs=""

for i in range(0,num_repeats):
    inputs=inputs+"-i "+base_file

print(pre)
print("\n")
print(com)
print(inputs)
