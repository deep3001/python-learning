info = {"name":"deepanshu",
        "age":9,
        "sub":["maths","physics","chemistry"],
        "fev-fruit":{"1":"aam",
                     "2":"kela",
                     3:"jamun"}
        
        }


print(info)


print(info["name"])
print(info.get("age"))
info["age"] = 21
print(info)
info["fev-fruit"]["1"] = "orange"
print(info)