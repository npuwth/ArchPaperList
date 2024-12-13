import os
import sys

src_name = "PaperList.md"
dst_name = "../README.md"
cnt = 1
src_file = open(src_name, "r")
dst_file = open(dst_name, "w")
for line in src_file:
    if "[*]" in line:
        dst_file.write(line.replace("[*]", "[{}]".format(cnt)))
        cnt = cnt + 1
    else:
        dst_file.write(line)

            