try:
    data = {"a": 1, "b": 2}
    print(data["c"])
except KeyError:
    print("Key not found..!")
