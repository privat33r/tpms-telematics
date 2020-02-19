from rtlsdr import RtlSdr
from pylab import *
from rtlsdr import *

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6  # Hz
sdr.center_freq = 96e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

samples = sdr.read_samples(256*1024)

sdr.close()

# use matplotlib to estimate and plot the PSD
psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')

show()