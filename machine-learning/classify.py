#!/usr/bin/env python

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import joblib

MODEL_PATH = "./model/rfc.model"


def load_data():
    data = datasets.load_iris()
    x_train, x_test, y_train, y_test = \
        train_test_split(data.data, data.target, test_size=0.3, random_state=0)

    return x_train, x_test, y_train, y_test


def main():
    x_train, x_test, y_train, y_test = load_data()
    classify = RandomForestClassifier(5)
    classify.fit(x_train, y_train)
    joblib.dump(classify, MODEL_PATH)


if __name__ == "__main__":
    main()

