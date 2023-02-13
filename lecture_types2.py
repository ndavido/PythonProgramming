import numpy as np

# uint8
# ==========
# u represents unsigned meaning that values cannot be negative
# 8 bytes and an integer 
x = np.array([1,], dtype=np.uint8)

x[0] = 1
print(x[0])

x[0] = 14
print(x[0])

x[0] = 400
print(x[0])

# 8 bit uint = 1111 1111 = 128+64+32+16 + 8+4+2+1 = 255
# 255 = 2^7 + 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0

print(bin(400))
print(bin(144))

x[0] = -1
print(x[0])

print(bin(255))
print(bin(-1))

# if int8
# bit is -, then we have 7 bits for number
# 64+32+16 + 8+4+2+1 = 127
y = np.array([1,], dtype=np.int8)

y[0] = -127
print(y[0])

y[0] = -128
print(y[0])

y[0] = -129
print(y[0])

# -1 = 1111 1111 = 1= -256 + 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1

first_dict = {"key":"value"}
print(first_dict)

second_dict = {"name":"Johan", "age":24, "alive":True}
print(second_dict)

print(second_dict["name"])

second_dict["height"] = 175
print(second_dict)

second_dict["height"] = 170
print(second_dict)

second_dict.update({"name":"Saana"})
print(second_dict)

second_dict.update(first_dict)
print(second_dict)

person1 = {"name":"Johan", "age":24, "alive":True}
person2 = {"name":"Toni", "age":27, "alive":True}
person3 = {"name":"Saana", "age":44, "alive":False}

humans = {
    "person1": person1,
    "person2": person2,
    "person3": person3
}

print(humans)
print(humans["person1"]["age"])
print(humans["person1"]["alive"])

x = np.array([1,], dtype=np.uint16)
min_value = np.iinfo(x.dtype).min
print(min_value)