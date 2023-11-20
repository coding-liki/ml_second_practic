from DataFetcher import DataFetcher

data_fetcher = DataFetcher("./data/train.csv", "./data/test.csv")

data_fetcher.fetch()
# def test_neural_network():
#     network = NewNetwork()
#     NetworkTester(network).test(data_fetcher.fetch())
#     pass
