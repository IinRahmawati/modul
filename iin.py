import emon

def main():

    #Menghitung Pemuaian Panjang
    p = 54
    P = 20
    t = 25
    
    #Rumus Pemuaian Panjang
    PemuaianPanjang = emon.muaipanjang(p, P, t)

    print("Rumus Pemuaian Panjang")
    print("Panjang\t\t: ", p)
    print("Koefisien\t: ", P)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", PemuaianPanjang)

    #Menghitung Pemuaian Luas
    l = 31
    L = 34
    t = 12

    #Rumus Pemuaian Luas
    PemuaianLuas = emon.muailuas(l, L, t)

    print("\nRumus Pemuaian Luas")
    print("Luas\t\t: ", l)
    print("Koefisien\t: ", L)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", PemuaianLuas)

    #Menghitung Pemuaian Volume
    v = 12
    V = 30
    t = 5

    #Rumus Pemuaian Volume
    PemuaianVolume = emon.muaivolume(v, V, t)

    print("\nRumus Pemuaian Volume")
    print("Volume\t\t: ", v)
    print("Koefisien\t: ", V)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", PemuaianVolume)

if __name__ == "__main__":
    main()
