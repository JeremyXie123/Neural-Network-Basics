import network
net = network.Network([784, 30, 10])


training_data = []
test_data = []

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)