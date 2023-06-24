import pandas as pd

if __name__ == '__main__':
    data = {
        'a': [4, 5, 6],
        'b': [4, 5, 6],
        'c': [7, 8, 9],
        'd': [10, 11, 12],
    }

    df = pd.DataFrame(data)
    print(df)
    print(df.info())