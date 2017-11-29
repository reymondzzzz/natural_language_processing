import sys, os

basename = os.path.splitext(os.path.basename(sys.argv[1]))[0]
dir = os.path.dirname(sys.argv[1])

with open(sys.argv[1], 'r') as input_file , open(dir + os.sep +  basename + ".txt", 'w') as output_file, open(dir + os.sep +  basename + "_tagged.txt", 'w') as output_tagged_file:
    lines = input_file.read().splitlines()
    index = 0
    while index < len(lines):
        if lines[index] != '':
            if "# text = " in lines[index]:
                index += 1
                print (lines[index])
                while lines[index] != '':
                    tmp = lines[index].split()
                    output_file.write(tmp[1] + " ")
                    output_tagged_file.write(tmp[1] + "/" + tmp[3] + " ")
                    index +=1
                output_file.write("\n")
                output_tagged_file.write("\n")
                # output_file.write(lines[index].replace("# text = ", "", 1) + "\n")
        index += 1

