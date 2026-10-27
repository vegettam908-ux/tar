tableroJuego = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]

def mostrarGrilla(matriz):
    print("    1   2   3    4   5   6    7   8   9")
    print("  " + "-" * 37)
    for f in range(9):
        if f % 3 == 0 and f != 0:
            print("  " + "-" * 37)
            
        texto = str(f + 1) + " | "
        for c in range(9):
            if c % 3 == 0 and c != 0:
                texto += "| "
                
            if matriz[f][c] == 0:
                texto += "_   "
            else:
                texto += str(matriz[f][c]) + "   "
        print(texto)
    print()

def esNumeroPermitido(valor, f, c):
    for i in range(9):
        if tableroJuego[f][i] == valor or tableroJuego[i][c] == valor:
            return False
            
    baseFila = (f // 3) * 3
    baseCol = (c // 3) * 3
    
    for i in range(baseFila, baseFila + 3):
        for j in range(baseCol, baseCol + 3):
            if tableroJuego[i][j] == valor:
                return False
                
    return True

def buscarCeldaVacia():
    for f in range(9):
        for c in range(9):
            if tableroJuego[f][c] == 0:
                return f, c
    return None, None

def jugarSudoku():
    f, c = buscarCeldaVacia()
    
    if f is None and c is None:
        return True
        
    for valor in range(1, 10):
        if esNumeroPermitido(valor, f, c):
            tableroJuego[f][c] = valor
            
            if jugarSudoku():
                return True
                
            tableroJuego[f][c] = 0
            
    return False

print(">>> TABLERO INICIAL <<<")
mostrarGrilla(tableroJuego)

if jugarSudoku():
    print(">>> ¡TABLERO COMPLETADO CON ÉXITO! <<<")
    mostrarGrilla(tableroJuego)
else:
    print(">>> ERROR: No se pudo resolver este Sudoku <<<")