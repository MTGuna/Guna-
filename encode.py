import base64
str="""hello who are you"""
str=base64.b64encode(str.encode("utf-8"))
print("encode string:",str)
str=base64.b64decode(str).decode("utf-8")
print("decode string:",str)
                            
