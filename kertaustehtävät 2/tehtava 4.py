def kuusi(koko):
    print("Tämä on kuusi!")
    for i in range(1, koko + 1):
        tähdet = "*" * (2 * i - 1)
        välilyönnit = " " * (koko - i)
        print(välilyönnit + tähdet)
    runko_väli = " " * (koko - 1)
    print(runko_väli + "*")
kuusi(5)