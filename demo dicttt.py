dict={"101":"guna","102":"mahi","103":"king"}
print(dict)
print("keys:",dict.keys())
print("values:",dict.values())
print("items:",dict.items())
print(dict["101"])
dict1=(dict.copy())
print(dict1)
print(dict)
print(dict.get("101"))
print(dict.setdefault("101",100))
dict1={"104":"guna","105":"hii","106":"king"}
print(dict,dict1)
(dict.update(dict1))
print(dict)
t=(104,105,106)
print(dict.fromkeys(t))
print(dict.fromkeys(t,12))
(dict.clear())
print(dict)
