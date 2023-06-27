# Scatering Network for Seismology

import os
import pickle

import matplotlib.dates as mdates

import numpy as np
import obspy
from obspy.clients.fdsn.client import Client 
import time

from scatseisnet import ScatteringNetwork

dirpath_save = "../example_long"

# Create directory to save the results
os.makedirs(dirpath_save, exist_ok=True)

print('Package imported and folder created.')

# load data ===============================================================================================
stime = time.time() # start time
client = Client("IRIS")

# Collect waveforms from the datacenter
stream = client.get_waveforms(
    network="UW",
    station="SHW",
    location="*",
    channel="EHZ",
    starttime=obspy.UTCDateTime("2004-09-01T00:00"),
    endtime=obspy.UTCDateTime("2004-10-01T00:00.1"),
)

stream.detrend("linear")
stream.taper(0.05, type='hann')
stream.merge(fill_value=0)

stream.filter(type="highpass", freq=1.0)
stream.resample(100)
stream.plot(rasterized=True);

# stream.write("../example_long/scattering_stream.mseed", format="MSEED")
print('Loading data tooks {} seconds.'.format(round(time.time()-stime,3)))

# create layers ===============================================================================================

segment_duration_seconds = 60.0
sampling_rate_hertz = stream[0].stats.sampling_rate
samples_per_segment = int(segment_duration_seconds * sampling_rate_hertz)
# the network will have 2 layers
bank_keyword_arguments = (
    {"octaves": 4, "resolution": 4, "quality": 1},
    {"octaves": 5, "resolution": 2, "quality": 3},
)

# create scatnet ===============================================================================================

network = ScatteringNetwork(
    *bank_keyword_arguments,
    bins=samples_per_segment,
    sampling_rate=sampling_rate_hertz,
)

print(network)

# Save the scattering network with Pickle
filepath_save = os.path.join(dirpath_save, "scattering_network.pickle")
with open(filepath_save, "wb") as file_save:
    pickle.dump(network, file_save, protocol=pickle.HIGHEST_PROTOCOL)

# preparation for network transform ===================================================================================

# Extract segment length (from any layer)
segment_duration = network.bins / network.sampling_rate
overlap = 0.5

# Gather list for timestamps and segments
timestamps = list()
segments = list()

# Collect data and timestamps
for traces in stream.slide(segment_duration, segment_duration * overlap):
    timestamps.append(mdates.num2date(traces[0].times(type="matplotlib")[0]))
    segments.append(np.array([trace.data[:-1] for trace in traces]))
    
# scattering transform ===============================================================================================
st = time.time() # start time
scattering_coefficients = network.transform(segments, reduce_type=np.mean)

# Save the features in a pickle file
np.savez(
    "../example_long/scattering_coefficients.npz",
    order_1=scattering_coefficients[0],
    order_2=scattering_coefficients[1],
    times=timestamps,
)
print('Scattering transform and saving took {} seconds.'.format(round(time.time()-st),3))
print('Script run for {} minutes.'.format(round((time.time()-stime)/60,3)))