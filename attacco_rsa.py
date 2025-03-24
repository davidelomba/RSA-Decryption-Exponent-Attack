import math
import random
import time

import sympy as sympy
import numpy as np

def euclide_esteso(a, b):
    # inizializzo i coefficienti per a e b (servono due coppie per mantenere i coeff. dell'iterazione precedente)
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    # itero fin quando il resto non diventa zero
    while b != 0:
        q = a // b
        r = a % b

        # le due seguenti istruzioni valgono perché MCD(a, b) = MCD (b, a mod b)
        a = b
        b = r

        # aggiorno i coefficienti
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0

# funzione che mette in pratica l'attacco a RSA
def decryptionexp(n, ed):
    # definisco n-1 come 2^r * m con m dispari
    m = ed - 1
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    # contatore per il numero di iterazioni
    num_iter = 0
    # ciclo finché non trovo i due fattori primi di n
    while True:
        # scelgo casualmente x in Zn*
        x = n
        while math.gcd(x, n) != 1:
            x = random.randint(2, n - 2)

        # x0 e x1 rappresentano x(j-1) e xj

        # calcolo x0 = x^m mod n
        x0 = pow(x, m, n)

        if x0 == 1 or x0 == n - 1:
            continue
        # itero fino a r
        for j in range(1, r):
            num_iter += 1
            # calcolo x = x^2 mod n
            x1 = pow(x0, 2, n)
            # effettuo i controlli descritti nell'esercizio
            if x1 == 1 and (x0 % n != (n - 1)):
                # calcolo il mcd
                mcd, _, _ = euclide_esteso(x0 + 1, n)
                # restituisco i due fattori primi di n
                return mcd, n // mcd, num_iter
            x0 = x1

    return None, None, num_iter

# funzione per la generazione della chiave pubblica
def genera_e(phi):
    # cicla finché non trovo un valore e coprimo con phi(n)
    while True:
        # genero un valore in Zphi(n)
        e = random.randint(2, phi - 1)
        # calcolo il MCD con l'algoritmo di euclide esteso
        mcd, _, _ = euclide_esteso(e, phi)
        # se è coprimo restituisco il valore trovato
        if mcd == 1:
            return e

# funzione per la generazione dei parametri di RSA
def genera_parametri_RSA(bits):
    # genero un numero dispari fissato il numero di bit
    p = sympy.randprime(2 ** (bits - 1), 2 ** bits)
    q = sympy.randprime(2 ** (bits - 1), 2 ** bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = genera_e(phi)
    _, d, _ = euclide_esteso(e, phi)
    if d < 0:
        d = d + phi
    return n, d, e, p, q

# funzione che applica 100 moduli di RSA e calcola numero medio di iterazioni, vraianza e media dei tempi
def test_decryptionexp(num_tests=100):
    tempi = []
    iterazioni = []

    for _ in range(num_tests):
        n, d, e, p, q = genera_parametri_RSA(1024)
        start_time = time.time()

        _, _, num_iter = decryptionexp(n, e * d)

        end_time = time.time()
        tempi.append(end_time - start_time)
        iterazioni.append(num_iter)


    media_tempi = np.mean(tempi)
    varianza_tempi = np.var(tempi)
    media_iterazioni = np.mean(iterazioni)

    print(f"Tempo medio: {media_tempi:.4f} secondi")
    print(f"Varianza del tempo: {varianza_tempi:.4f}")
    print(f"Numero medio di iterazioni: {media_iterazioni:.4f}")

if __name__ == '__main__':
    test_decryptionexp()