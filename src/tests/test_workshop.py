import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal
from src.workshop import add, impute_nans


class TestWorkshop(unittest.TestCase):
    def test_one_should_equal_one(self):
        # arrange -- how it should work
        expected = 2

        # act -- make it work
        actual = add(1, 1)

        # assert -- make sure it works
        self.assertEqual(expected, actual)
        # Don't trust tests that pass the first time

    # Tests drive development!  Write tests first!  LOL
    def test_len_cat_equal_len_dog(self):
        self.assertEqual(len("dog"), len("cat"))

    def test_df_should_equal_itself(self):
        # arrange
        df = pd.DataFrame({"column_1": [1, 2, 3]})

        # assert
        assert_frame_equal(df, df)

    def test_impute_nans_should_fill_nans_with_median_value(self):
        # arrange
        df = pd.DataFrame({"column": [1, np.nan]})
        expected = pd.DataFrame({"column": [1.0, 1.0]})

        # act
        actual = impute_nans(df, ["column"])

        # assert
        assert_frame_equal(expected, actual)
