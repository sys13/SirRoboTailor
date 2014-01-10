import csv
from pybrain import TanhLayer
from pybrain.datasets import ClassificationDataSet, SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork

# create the dataset with inputs and outputs specified
numberOfInputs = 7
numberOfOutputs = 4

d = SupervisedDataSet(numberOfInputs, numberOfOutputs)
with open('data.csv', 'rb') as csvfileRead:
    datareader = csv.reader(csvfileRead, delimiter=',',
                            quotechar='*')

    next(datareader, None)
    for row in datareader:

        trainIn = []
        for x in row[:numberOfInputs]:
            trainIn.append(x)

        trainOut = []
        for x in row[numberOfInputs:]:
            trainOut.append(x)

        d.appendLinked(trainIn, trainOut)

    # build a neural network with the second parameter being the number of hidden layers
    n = buildNetwork(d.indim, 3, d.outdim, recurrent=True)

    # configure the trainer
    t = BackpropTrainer(n, learningrate=0.01, momentum=0.99, verbose=True)

    # split the data randomly into 75% training - 25% testing
    train, test = d.splitWithProportion(0.75)
    print "{} - {}".format(len(train), len(test))

    # train the data with n number of epochs
    t.trainOnDataset(train, 10)

    # test the data with the remaining data
    t.testOnData(test, verbose=True)

    # try the same test but with a different method
    net = buildNetwork(d.indim, 3, d.outdim, bias=True, hiddenclass=TanhLayer)
    trainer = BackpropTrainer(net, d)
    trainer.trainUntilConvergence(verbose=True)
