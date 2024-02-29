import unittest

from rdatasets import data, descr, get_data_path, items, packages, summary


class TestWrapper(unittest.TestCase):
    def test_iris_dataset(self):
        dataset = data("iris")
        doc = descr("iris")
        self.assertTrue(len(dataset) > 0)
        self.assertTrue(len(doc) > 0)

    def test_forecast_gas(self):
        dataset = data("forecast", "gas")
        doc = descr("forecast", "gas")
        self.assertTrue(len(dataset) > 0)
        self.assertTrue(len(doc) > 0)

    def test_summary(self):
        s = summary()
        self.assertTrue(len(s) > 0)

    def test_get_data_path(self):
        self.assertTrue(len(get_data_path()) > 0)

    def test_packages(self):
        self.assertTrue(len(packages()) > 0)

    def test_items(self):
        i = items("forecast")
        self.assertTrue(len(i) > 0)
