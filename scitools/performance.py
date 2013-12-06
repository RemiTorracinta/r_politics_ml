import sys

interval=25
interval_ten=10
interval_five=5

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




    #rescale interval_ten to remove arbitrary cutoffs
    condition = testratings[interval_ten-1][0] == testratings[interval_ten][0]
    count = 1
    while(condition and interval_ten+count < len(testratings)):
        condition = testratings[interval_ten-1][0] == testratings[interval_ten+count][0]
        if condition:
            count += 1

    use_interval_ten = interval_ten + count

    top_predict = []
    top_test = []
    for i in range(use_interval_ten):
        top_predict.append(testratings[i][1])
        top_test.append(predictratings[i][1])

    print "Accuracy on top " + str(use_interval_ten) + " is: " + str(len(set(top_test).intersection(set(top_predict)))/float(use_interval_ten))


    #rescale interval_five to remove arbitrary cutoffs
    condition = testratings[interval_five-1][0] == testratings[interval_five][0]
    count = 1
    while(condition and interval_five+count < len(testratings)):
        condition = testratings[interval_five-1][0] == testratings[interval_five+count][0]
        if condition:
            count += 1

    use_interval_five = interval_five + count

    top_predict = []
    top_test = []
    for i in range(use_interval_five):
        top_predict.append(testratings[i][1])
        top_test.append(predictratings[i][1])

    print "Accuracy on top " + str(use_interval_five) + " is: " + str(len(set(top_test).intersection(set(top_predict)))/float(use_interval_five))

    #calculates better than random
    for i in range(1,31):
        top_predict = []
        top_test = []
        for j in range(i):
            top_predict.append(testratings[j][1])
            top_test.append(predictratings[j][1])
        
        acc = len(set(top_test).intersection(set(top_predict)))
        print str(acc)
    #       print "Better than random on top " + str(i) + " is: " + str(acc/(i/100.))


else:
    print "improper usage"



