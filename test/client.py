#!/usr/bin/env python

import json

from sklearn import datasets
from sklearn.model_selection import train_test_split

import requests


def load_data():
    data = datasets.load_iris()
    x_train, x_test, y_train, y_test = \
        train_test_split(data.data, data.target, test_size=0.3, random_state=0)

    return x_train, x_test, y_train, y_test


def main():
    x_train, x_test, y_train, y_test = load_data()
    uri = "http://127.0.0.1:8000"       # TODO if you changed the server ip and port, update it.
    for feature in x_test:
        data = {"feature": feature.tolist()}
        headers = {"Content-Type": "Application/json"}
        response = requests.post(uri, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data["errno"] == 0:
                label = data["label"]
            else:
                errmsg = data["errmsg"]


if __name__ == '__main__':
    main()

