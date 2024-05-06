sample = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

item = 0
print(f"key\tvalue\titem") 
for key in sample:
    item += 1
    print(f"{key}\t{sample[key]}\t{item}") 