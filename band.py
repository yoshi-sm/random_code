from math import ceil


def limpeza(f):
    temp = f.readline().strip().split(' ')
    for i in range(temp.count('')):
        temp.remove('')
    return temp


def main():
    arquivo = input("Digite o nome do arquivo (ex: Label.bands): ")
    # valor de k e da energia para o minimo da banda de conducao e maximo da banda de valencia

    k_val = 0
    k_cond = 0
    e_cond = 10000
    e_valen = -10000

    with open(arquivo) as f:
        e_fermi = round(float(f.readline().strip()), 4)

        # kmin and kmax
        temp = limpeza(f)
        kmin = float(temp[0])
        kmax = float(temp[1])

        # Emin and Emax
        temp = limpeza(f)
        e_min = float(temp[0])
        e_max = float(temp[1])

        # number of bands, number of spin, number of kpoints
        temp = limpeza(f)
        num_bands = int(temp[0])
        num_spin = int(temp[1])
        num_k = int(temp[2])

        # important part of the code
        e_per_k = 0
        for i in range(num_k):
            for j in range(ceil(num_bands * num_spin/10)):
                temp = limpeza(f)
                temp = [float(k) for k in temp]
                if j == 0:
                    e_per_k = temp[0]
                    temp.pop(0)
                for k in temp:
                    if e_fermi <= k < e_cond:
                        e_cond = k
                        k_cond = e_per_k
                    elif e_fermi >= k >= e_valen:
                        e_valen = k
                        k_val = e_per_k

        print(f"\nEnergia de fermi = {e_fermi} eV\n"
              f"Minimo da banda de conducao e seu valor de k: E = {e_cond} eV,  k = {k_cond} \n"
              f"Maximo da banda de valencia e seu valor de k: E = {e_valen} eV, k = {k_val}\n"
              f"Gap de banda = {round(e_cond - e_valen, 4)} eV\n")


main()
