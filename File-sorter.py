import os
import shutil

def label_files(filepath: str) -> str:
    #iterate though each of the files in the filepath
    list_of_dir = os.listdir()
    for x in list_of_dir:
        if x.endswith(".py") or "data.txt" in x:
            continue
        #open the file for the user
        os.startfile(x)
        #for each file, ask the user what folders it goes into
        user = input("What folders would you like this file to go into for instuction\
        s please read readme.txt     ")
        #make a text file called "data.txt" in that same folder
        with open(filepath + "\data.txt","a+") as txt:
        #write the compiler instuctions into that txt file
            txt.write(x.split("/")[-1] + "=" + user)
            txt.write(" \n")
    txt.close()
    #return the location of the text file for later use
    return(filepath + "\data.txt")

def compiler(txtfile: str, filepath: str) -> "done":
    #open txt file
    txt = open(txtfile,"r")
    #read file line
    for line in txt:
        instructions = line.split("=",1)[1].split(",")
        filename = line.split("=",1)[0]
        for instruction in instructions:
            #sort infomation from the text file
            #take uncompiled information
            info = instruction.split("=")
            #split it into a list of enteries
            parents = info[0].split(" ")
            child = info[1].split(" ")
            child.pop(-1)
            #make the directories accordingly
            filepaths = []
            for x in parents:
                path = str(filepath + "\\" + x)
                for z in child:
                    filepaths.append(path + "\\" + z)

        #copy the file to that directory
        for x in filepaths:
            try:
                f = os.makedirs(x,exist_ok = True)
                pass
            finally:
                pass
            print(x)
            shutil.copy2(os.getcwd() + "\\" + filename,x)


    return("done")
location = input("where are the files that you want sorting?")
txt = label_files(location)
compiler(txt,location)
