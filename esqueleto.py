import esqueleto as ms
import numpy as np

def main():
	"""
	Lee los datos de encefalogramas para determinar si los valore supremos 	de las frecuencias de un espectro de potencias producen una senal con una breve aproximacion a la original
	"""

	#define archivos input/output
	filename='data.txt'
	output='outdata.txt'
	grafica_datos='g_electrodos'
	#carga de datos
	datos=ms.getdata(filename)
	#obtiene columna de datos
	fft_freq=ms.getcolumn(datos)

if __name__ == "__main__":
	main()


"""
Functions for exercise 1 hw 5
Authors: Martha Ortiz
Wed 09 - October - 2013
"""

def getdata (filename):
    """
    load the data in the given file

    in: filename
    out: numpyarray with the data
    """
    n=400;
    m=25;
    datos = np.ones((n,m))
    return datos

    
def getcolumn(data):
    """
    returns the column given of the array of data

    in: narray the array
 
    out: ndarray column (single electrode data)
    """

    fft_freq=data
    return fft_freq


def fouriercol (electrode):
    """
    returns the fourier transform of a single electrode

    in: ndarray electrode
    out: ndarray fourier transform
         ndarray frecuencies
    """
    fft_freq=electrode
    return fft_freq


def espectrop(FFT):
    """
    for a fourier transform, calculates its squared norm
    
    in: ndarray FFT, 
    out: ndarray squared norm of all the components of FFT
    """

    return 


def searchmax (sqnorm, FrecFFT):
    """
    selects the 10 maximum norms of the array of norms
    
    in: ndarray sqnorm
        ndarray FrecFFT, frecuencies of fft
    out: ndarray of 10 max norms
         ndarray of 10 frecuencies, corresponding to the positios of the max norms
    """
    return

def reconstruct (maxnorm, FrecFFT):
    """
    reconstructs the signal doing a inverse fourier transform of the max norms
    
    in: ndarray maxnorm
        ndarray FrecFFT
    out: ndarray ReconsSignal the reconstructed signal
    """
    return

def plotsig (ReconSig, electrode):
    """
    plots the reconstructed signal and the original
    
    in: ReconSig, the reconstructed signal
        electrode, the original signal
    """

def chisq (ReconSig, electrode):
    """
    calculates the chi squared of the reconstruction
    
    in: ReconSig, the reconstructed signal
        electrode, the original signal
    out: Chi2, the chi squared of a signal
    """
    return
