def add(a, b):
    return a + b


def impute_nans(df, columns):
    return df[columns].fillna(df[columns].dropna().median())
