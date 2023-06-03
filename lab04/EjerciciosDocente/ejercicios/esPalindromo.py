def noSpace(texto):
    return texto.replace(" ", "")


def esPalindromo(texto):
    sinEsp = noSpace(texto)
    if sinEsp.lower() == sinEsp[::-1].lower():
        print("es palindromo")
    else:
        print("no es palindromo")  


esPalindromo("12321")
esPalindromo("amo la paloma")
esPalindromo("la ruta natural")
esPalindromo("cosaadsfs")

