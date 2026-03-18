mi_navegacion = [
    "google.com",
    "uniminuto.edu",
    "Error 404: Campus Virtual",
    "github.com",
    "stackoverflow.com"
]

def retroceder(historial, pasos):
    if pasos == 0 or len(historial) == 0:
        return historial
    if "Error 404" in historial[-1]:
        print(f"Se detuvo en: {historial[-1]}")
        return historial
    historial.pop()
    return retroceder(historial, pasos - 1)

nuevo_historial = retroceder(mi_navegacion.copy(), 3)
print("Historial final:", nuevo_historial)