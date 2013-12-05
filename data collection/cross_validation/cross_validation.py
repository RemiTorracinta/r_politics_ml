import sys
import random

kfold = 10

if len(sys.argv) == 2:
    inputfile = sys.argv[1]

    lines = []
    with open(inputfile,'r') as trainfile:
        for line in trainfile:
            lines.append(line)


    random.shuffle(lines)

    val_array = []
    train_array = []
    for i in range(kfold):
        val_array.append(open('val'+str(i)+'.data','wb'))
        train_array.append(open('train'+str(i)+'.data','wb'))

    val_num = 0
    for line in lines:
        for i in range(10):
            if i==val_num:
                val_array[i].write(line)
            else:
                train_array[i].write(line)
        val_num = (val_num + 1) % kfold

    for i in range(kfold):
        val_array[i].close()
        train_array[i].close()


else:
    print "Wrong usage - jsut give me the datafile to split up"