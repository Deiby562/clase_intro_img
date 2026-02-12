import numpy as np

def img_letra(lt):
    if lt == 'a':
        a = np.array([[0, 0, 0],[25, 255, 25],[50, 50, 50],[75, 255, 75]])
    elif lt == 't':
        a = np.array([[0, 0, 0],[255, 25, 255],[255, 50, 255],[255, 75, 255]])
    else:
        raise ValueError("Letra no reconocida.")


def img_letras(letras):
    letras_list = list(letras)
    imgs_list = [img_letra(lt) for lt in letras_list]

