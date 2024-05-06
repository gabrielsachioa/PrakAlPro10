def list_to_dict(Lista, Listb):
    hasil = {}

    for item, key in enumerate(Lista):
        if item < len(Listb):
            hasil[key] = Listb[item]
    return hasil

# PROGRAM UTAMA
Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

print(list_to_dict(Lista, Listb))