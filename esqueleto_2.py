import numpy as np


"""
Functions for exercise 2 hw 5
Authors: Juan Estupinan, Martha Ortiz
Wed 09 - October - 2013
"""

def getdata (filename):
    """
    load the data in the given file

    in: filename
    out: numpyarray with the data
    """
    return

    
def getcolumns(data, ty, tm, td, m):
    """
    returns the columns given of the array of data (time(years), time(months), 	    time(days),stain)

    in: narray the array
        ty the column of time(years) wanted
	tm the column of time(months) wanted
	td the column of time(days) wanted
	m the column of observed stains wanted
    out: array column (years of observation)
	 array column (observed stains)
	 array column (months of observation)
	 array column (days of observation)
    """
    return

def constant_interpolation(ty, tm, td, stains):
    """
    calculate the constant interpolation between the observed stains in the three frecuencies of measurements

    in: ndarray stains
    out: ndarray constant interpolation
    """
    return

def lineal_interpolation(ty, tm, td, stains):
    """
    calculate the lineal interpolation between the observed stains in the three frecuencies of measurements

    in: ndarray stains
    out: ndarray lineal interpolation
    """
    return

def cubic_interpolation(ty, tm, td, stains):
    """
    calculate the cubic interpolation between the observed stains in the three frecuencies of measurements

    in: ndarray stains
    out: ndarray cubic interpolation
    """
    return

def espectrop_const(const_interp):
    """
    from the constant interpolation, calculates its power spectrum
    
    in: ndarray const_interp, 
    out: ndarray squared norm of all the components of FFT from the constant interpolation
    """
    return

def espectrop_lin(lin_interp):
    """
    from the linear interpolation, calculates its power spectrum
    
    in: ndarray lin_interp, 
    out: ndarray squared norm of all the components of FFT from the linear interpolation
    """
    return

def espectrop_cub(cub_interp):
    """
    from the cubic interpolation, calculates its power spectrum
    
    in: ndarray cub_interp, 
    out: ndarray squared norm of all the components of FFT from the cubic interpolation
    """
    return

def reconstruct (data_aprox, interpolations):
    """
    reconstructs the signal and the new data by calculating the inverse fourier transform of the power spectrums with the aproximation that implies making cero all the FFT with frecuencies 2<k<20 years
    
    in: ndarray data_aprox
        ndarray interpolations
    out: ndarray ReconsSignal the reconstructed signal
    """
    return

def plotsig (ReconSig, data):
    """
    plots the reconstructed signal and the original
    
    in: ReconSig, the reconstructed signal
        data, the original signal
    """

def solar_cycle (ReconSig)
	"""
	estimate the solar cycle
	in: ReconSig, the reconstructed signal
	out: s_c, cycle of the sun
	"""
	return
    return
