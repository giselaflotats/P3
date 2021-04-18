import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

#Creació de l'arxiu a partir del qual traiem la frequencia de mostreig i les seves mostres d'audio
arxiu = '/Users/giselaflotatsboix/PAV/P3/pav_2301_02.wav'
fm, audio = waves.read(arxiu)
audio = audio.astype(float)

#Vector temps
dt = 1/fm
mostres = []
for x in range(0, len(audio)):
    mostres.append(x*dt)

#Enfinestrem utilitzant Hamming (FER_HO BÉ)
audio2 = np.arange(len(audio))
audioEnfinestrat = audio2*np.hamming(len(audio))

#Autocorrelació
autocorrelacio=np.correlate(audioEnfinestrat, audioEnfinestrat, "same")

#Gràfica
plt.subplot(211)
plt.title("Senyal temporal")
plt.plot(mostres, audio, linewidth = 0.5)
plt.xlabel('Temps (s)')
plt.ylabel('Forma de ona')
plt.grid(True)
plt.subplot(212)
plt.title("Autocorrelació")
plt.xlabel("Mostres")
plt.ylabel("Autocorrelació")
plt.plot(range(0, len(autocorrelacio)), autocorrelacio, linewidth = 0.5)
plt.grid(True)
plt.show()