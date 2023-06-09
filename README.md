# ESS590D_Manuela_Koepfli

My goal is to better understand the eruptions at Mt St Helens. I am focusing on the onset of the 2004 eruption and possibly also the known eruption that started in 1980.

The active phase of Mt St Helens started on 23 September 204 with a shallow earthquake swarm at 9 UTC (2 am local time). The number and magnitude of the earthquakes, presumably of volcanic origin, increase in the following days and weeks. At the beginning of October, the first changes can also be observed on the surface. The end of the volcanic activity is in February 2008. The number of active seismometers in this period varies from around 10 to 15. Most of the seismometers are single-component velocity sensors, sampled at 100 Hz.

So far the shallow earthquake swarm is the only precursor and I would like to investigate the noise field in more detail to find previously undetected signs of the imminence of the eruption. A proven method is to calculate the energy in specific frequency bands. For volcanoes the frequency bands 2-5, 4.5-8 and 8-16 Hz are used. The resulting time series is called Real Time Seismic Amplitude (RSAM). However, the USGS analysis of the Mt St Helens 2004 eruption found no foreshocks in the RSAM. Therefore, I focus my attention on the Displacement Seismic Amplitude Ratio (DSAR). DSAR is a quantity that describes attenuation. DSAR can also be normalized and other different processing steps can be added.

To better understand the origin of the noise, I use the covariance matrix eigenvalue distribution to analyze the directionality and coherence of the noise sources.


## Installation
To work with the folder, you have to clone the github rep first. Therefore copy the ssh (bode button). Then create the environment by typing ``` conda env create --file ESS590D_env.yml```.

Next, activate the new environment by typing ```conda activate ESS590D_env```.

To create a kernel from the environment by typing ```ipython kernel install --name "ESS590D_env --user```.

Then you can run the python script like ```python RSAM_DSAR.py year start_day end_day 'network' 'station' 'channel'``` which will calculate the energy in the three frequency bands and the DSAR.

To calculate the normalized DSAR and the median, use the jupyter notebook. Make sure to open the notebook when the conda environment is still active.


## Data
The folder ```code``` includes all the used python scripts and jupyter notebooks.

The folder ```data``` includes all used data to create the plors exept of the seismic data, which will be downloaded via the IRIS server.

The folder ```plots``` includes all saved plots created with any of the provided scriprs.
