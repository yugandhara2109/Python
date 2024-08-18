d={"a":12,"for":25,"c":9}
d1={"Geeks":100,"c":200,"for":300}

print(d)
print(d1)
for key in d1:
    if key in d:
        d1[key]=d1[key]+d[key]
    else:
        pass
print(d1)
