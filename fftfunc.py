import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftshift

'''def sinusoidFunc(x, **funcSpecs):
	 y = funcSpecs['a'] * np.sin(((np.pi * 2)/(funcSpecs['p'])) * (x - funcSpecs['ps'])) + funcSpecs['vs']
	 return y


def generateOutputArray(numPoints, spacing, **funcSpecs):
	i = 0
	outPut = []
	while i < (numPoints * spacing):
		outPut.append(round(sinusoidFunc(i * spacing, **funcSpecs), 4))
		i = i + 1
	return tuple(outPut)'''

def sinusoidFunc(t, **funcSpecs):
 	return np.sin(2*np.pi*t)


def generateOutputArray(numPoints, spacing, **funcSpecs):
 	outPut= signal.gaussian(200,std=5)
	'''outPut = sinusoidFunc(t, **funcSpecs)'''


	return outPut




def main():
	functionSpecs = {'a': 5, 'p': 2 * np.pi, 'ps': np.pi, 'vs': 1}
	outPutArray = generateOutputArray(100, 0.5, **functionSpecs)
	t = np.arange(0.0, 2.0, 0.01)
	print outPutArray
	'''fftArray = np.fft.fft(outPutArray)'''
	fftArray =fft(outPutArray)

	print fftArray
	plt.plot(t, outPutArray)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Function')
	plt.grid(True)
	plt.savefig("function.png")
	plt.show()
	inputArray = np.linspace(0,50,100)
	plt.plot(t, fftArray)
	plt.plot(t, np.abs(fftArray))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('FFT')
	plt.grid(True)
	plt.savefig("fftfunction.png")
	plt.show()



if __name__ == '__main__':
	main()
