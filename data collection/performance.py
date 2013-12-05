import sys

interval=25

if len(sys.argv) == 3:
    testfile_name = sys.argv[1]
    predictfile_name = sys.argv[2]

    testratings = []
    predictratings = []

    #parse upvotes
    with open(testfile_name,'r') as testfile:
        count = 0
        for line in testfile:
            testratings.append((float(line.split()[0]),count))
            count += 1

    #parse predictions
    with open(predictfile_name, 'r') as predictfile:
        count = 0
        for line in predictfile:
            predictratings.append((float(line),count))
            count += 1

    #Sort both rating lists
    testratings.sort()
    predictratings.sort()
    testratings.reverse()
    predictratings.reverse()


    #rescale interval to remove arbitrary cutoffs
    condition = testratings[interval-1][0] == testratings[interval][0]
    count = 1
    while(condition and interval+count < len(testratings)):
        condition = testratings[interval-1][0] == testratings[interval+count][0]
        if condition:
            count += 1

    use_interval = interval + count

    top_predict = []
    top_test = []
    for i in range(use_interval):
        top_predict.append(testratings[i][1])
        top_test.append(predictratings[i][1])

    print "Accuracy on top " + str(use_interval) + " is: " + str(len(set(top_test).intersection(set(top_predict)))/float(use_interval))



else:
    print "improper usage"





