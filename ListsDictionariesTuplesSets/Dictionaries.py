if __name__ == '__main__':

    my_dict = {"key1": "value1", "key2": "value2"}
    print(my_dict)
    print(my_dict["key1"])
    prices_lookup = {"apple": 2.99, "oranges": 1.99, "milk": 5.80}
    print(prices_lookup["apple"])

    d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
    print(d["k2"])
    print(d["k2"][2])
    print(d["k3"])
    print(d["k3"]["insideKey"])

    dict2 = {"key1": ["a", "b", "c"]}
    mylist = dict2["key1"]
    print(mylist)
    letter = mylist[2]
    print(letter.upper())
    print(dict2["key1"][2].upper())

    prices_lookup["celery"] = .79
    print(prices_lookup)
    print(prices_lookup.keys())
    print(prices_lookup.values())
    print(prices_lookup.items())
