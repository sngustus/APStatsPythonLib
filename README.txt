"""""""""""""""""""""""""""
PyStats python library
written by Steve Gustus

"""""""""""""""""""""""""""

NAME
	PyStats - Basic calculator functions useful for statistics

DESCRIPTION
	This module expands on the built-in "statistics" module.

CLASSES
	None

FUNCTIONS
	zScore(y,mu,sigma)
		calculates the z score of a value
			y - value
			mu - sample/population mean
			sigma - sample/population stdev

	normpdf(z)
		calculates the probability of a z-score

	normcdf(z1,z2)
		calculates the probability of a z-score between z1 and z2

