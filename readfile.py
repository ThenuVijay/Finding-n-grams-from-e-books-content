import glob
import csv
import read as re
read_files = glob.glob("F:\\FTE_TextFiles\\FTE_TextFiles\\*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())




file=open(r'C:\\Users\\User\\Desktop\\python practice\\result.txt',encoding="utf-8") 
content = file.read()
file.close()


re.Findgrams1(content,1)
re.Findgrams1(content,2)

























# import csv
# import glob
# files = glob.glob('C:\\Users\\User\\Desktop\\bbb\\*.txt')
# for file in files:
    # print(file)
    # with open('result.txt', 'w') as result:
        # result.write(str(file)+'\n')



# # file1 = glob.glob("C:\Users\User\Desktop\bbb\*.txt")

# # with open("result.txt", "wb") as outfile:
    # # for f in file1:

        # # with open(f, "rb") as infile:
            # # outfile.write(infile.read())