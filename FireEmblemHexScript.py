def Hexvaloutput ():
    userInit = raw_input("Enter a Hex faggot: ")
    print
    hexInit = int("0x" + userInit, 16)
    hexList = [0x74, 0x70, 0x64, 0x60, 0x5C, 0x58, 0x8, 0x4]
    valList = [" -74 ::StarCount Value = 5", " -70 ::StarCount Val   = 0",
                " -64 ::+X Value        = 10", " -60 ::+X Val          = 0",
                " -5C ::Level Value     = 40", " -58 ::Level Val       = 0",
                " -8  ::SP Value        = 2500", " -4  ::SP Val          = 0"]

    for (i, x) in zip (hexList, valList):
        n = hex(hexInit - i)
        n1 = n.upper()      
        print n1[2:10] + x
        
    print
    raw_input("Yah dun gud ked, now press ENTER to close dis shit")
    
    return ()

Hexvaloutput()
