origin = 'Guvf vf zl frperg zrffntr.'
origin = origin.upper()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(letters)):
    encrypt = ''
    for i in origin:
        # or i in origin T/F
        dI = letters.find(i)
        if dI != -1:
            encrypt += letters[(dI + key) % len(letters)]
        else:
            encrypt += i
    print("#Key %s %s" % (key, encrypt))
