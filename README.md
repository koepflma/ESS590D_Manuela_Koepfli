# ESS590D_Manuela_Koepfli

## Goal
My goal is to better understand the eruptions at Mt St Helens. I am focusing on the onset of the 2004 eruption and hope to find some precursors for the eruption. After testing the code on the comparatively good continuos seismic data for the 2004 eruption I would like to look into the recovered data for the 1980 eruption.


## Installation
To work with the folder, you have to clone the github rep first. Therefore copy the ssh (bode button). Then create the environment by typing ``` conda env create --file ESS590D_env.yml```.

Next, activate the new environment by typing ```conda activate ESS590D_env```.

To create a kernel from the environment by typing ```ipython kernel install --name "ESS590D_env --user```.

Then you can run the python script like ```python RSAM_DSAR.py year start_day end_day 'network' 'station' 'channel'``` which will calculate the energy in the three frequency bands and the DSAR.

To calculate the normalized DSAR and the median, use the jupyter notebook. Make sure to open the notebook when the conda environment is still active.


## Folder Structure
The folder ```code``` includes all the used python scripts and jupyter notebooks.

The folder ```data``` includes all used data to create the plors exept of the seismic data and the extended2_long.csv files, which can be downloaded via the IRIS server for the seismic data and create with one of the scripts.

The folder ```plots``` includes all saved plots created with any of the provided scriprs.






## Some more information about the Project
### Background
Mount St. Helens gained widespread recognition due to its infamous 1980 eruption, during which the stratovolcano experienced the catastrophic loss of its northern flank. This eruption had several precursors (Malone et al., 1982). In more recent years, specifically from 23 September 2004 to February 2008, the volcano exhibited renewed activity (Sherrod et al., 2008). The most recent active phase of Mt St Helens started on 23 September 2004 with a shallow earthquake swarm at 9 UTC (2 am local time). Interestingly, this subsequent eruption occurred with minimal precursory indications. The only notable precursor was the detection of a shallow earthquake swarm, which took place just seven days prior to the initial explosion (1 October 2004). During this time, the number and magnitude of the earthquakes, presumably of volcanic origin, increase. Thus far, most analyses have focused on events, such as an increase in the number or magnitude of seismic activities (Sherrod et al., 2008). However, it is worth noting that seismic noise also contains valuable information regarding subsurface changes and can serve as a precursor for detecting the ascent of magma. Successful examples in studying the energy in different seismic frequency bands are Ardid et al., 2022, Caudron et al., 2021, Dempsey et al., 2020.  In contrast, the technique from Seydoux et al., 2016 describes how directional and coherent seismic noise is. Possibly, the combination of several ambient seismic noise methods does not aid in predicting future eruptions but also enhances our comprehension of the underlying physical processes occurring within the volcano.

### Seismometers
The number of active seismometers in this period varies from around 10. Most of the seismometers are single-component velocity sensors, sampled at 100 Hz. The aperture of the seismic array is around 10 km. For few stations we have digital data of the 1980 eruption. Most of the seismic instruments I’m using have a flat gain flat between 0.8 and 30 Hz. For the comparison between different stations, I always correct the instrument response before I start with the calculations. This is time consuming but reduces the error potential. On top of that I check the dip of the instrument. In the past I figured out that some instruments change their dip after an instrument check. In this case I multiply by minus one to get rid of this human made change.

### Data
During the eruption we can see the high number of events which have dominant frequencies around 10 Hz and many data gaps (which we hate!). The frequency content of the evetns is around 10 Hz, whereas the dominant fequencies of the microseimic noise (ocean waves) is around 0.2 Hz. Ocean waves are the dominant noise source during quiet periods. During an eruption, the dominant wave source is the volcano itself. Rising or oscillating magma, volcanic earthquakes, explosions, steam and ash bursts all these kinds of events dominate the seismicity. Single events often have frequencies between 10 and 20 Hz and the background seismic noise which is produced by the volcano is lower (1-8 Hz).


So far the shallow earthquake swarm is the only precursor and I would like to investigate the noise field in more detail to find previously undetected signs of the imminence of the eruption. A proven method is to calculate the energy in specific frequency bands. For volcanoes the frequency bands 2-5, 4.5-8 and 8-16 Hz are used. The resulting time series is called Real Time Seismic Amplitude (RSAM). However, the USGS analysis of the Mt St Helens 2004 eruption found no foreshocks in the RSAM. Therefore, I focus my attention on the Displacement Seismic Amplitude Ratio (DSAR). DSAR is a quantity that describes attenuation. DSAR can also be normalized and other different processing steps can be added.

### RSAM, DSAR & many more
o comprehensively analyze the seismic data, I computed various time series for all available stations located within 5 km of Mt St Helens. These time series were derived from raw seismic data, meticulously corrected for instrument response, and spanned several years.

I also looked into the frequency content of the extracted time series. Here I quickly discuss the spectrograms of RSAM, DSAR, z-score DSAR. I dropped all nan values and concatenated the remaining data together within 2004. The eruption onset is now clearly visible in the RSAM and  z-score DSAR data in the frequency domain but not for the DSAR data.

### Covariance matrix eigenvalue distribution
This part of the study still requires careful parameter tuning, particularly regarding the length of time windows, the number of windows to be combined and the preprocessing. Further extensive testing is necessary to determine the optimal configurations for the actual task.

The result illustrate the coherence of ambient seismic noise across all seismic stations located within 5 km of Mt St. Helens. Small values indicate a narrow spectral width, indicating that seismic energy originates from a specific direction. Large values indicate well-distributed seismic energy. After spectral whitening, the presence of ocean-induced microseisms (at around 0.2 Hz) becomes evident. The spectral width of these microseisms is typically smaller during the winter months due to stronger and more frequent storms. Additionally, the onset of explosions on October 1st can be observed. However, the shallow earthquake swarm on September 23rd is barely discernible, and no eruption precursor is apparent. It is noteworthy that the low spectal width pattern observed in the summer, which is visible without preprocessing, was also present during the previous summer. This suggests that this directed energy may originate from surface events. The reason why they are only visible without preprocessing remains unclear.

To assess the eigenvalue distribution, I attempted to select individual events. To accomplish this, I reduced the time window to 10 seconds and averaged over only 5 consecutive time windows. Manually selected events occure where the average of the spectral within the specific frequency band is high. This implies that the energy during the event is more evenly distributed compared to before and after the event. The results are counterintuitive but could be attributed to different polarities observed by stations situated on the opposite side of the source (volcano). 

### Discussion
These preliminary findings have not revealed any precursors for the 2004 Mt St. Helens eruption. Further research is necessary to fine-tune parameters such as window length and preprocessing techniques for spectral width calculations. I also have to spend more time looking through all stations and comparing interesting features with the raw data. For example UW-YEL, positioned in close proximity to the glacier tongue, exhibits a prominent seasonal pattern. Notably, the energy levels, particularly in the highest frequency band (8 to 16 Hz), are most pronounced during the summer season. This intriguing observation suggests a plausible link to the meltwater outflow from the glacier, which is known to generate seismic noise. Conversely, during the winter months, the ratio between a low and high-frequency band reaches its peak. This observation implies that the high frequencies experience greater attenuation during winter or that the seismic energy source shifts towards lower frequencies. Further work is required to refine our methodologies and gain a more comprehensive understanding of the seismic behavior associated with Mt St. Helens.

Looking ahead, we aim to investigate correlations within the extracted time series on a daily and yearly basis. This analysis will help us identify any underlying trends over the past 20 years, potentially linking them to climate patterns.

Another objective of our study is to determine the direction of the dominant eigenvalue, enabling us to locate the source of the observed seismic energy. We will compare these results with conventional event location methods to validate the accuracy and reliability of our approach.

Finally, we plan to apply the same methods to analyze the famous 1980 eruption of Mt St. Helens.

## Upscaling
The work presented here can be scaled up for longer time series. The goal is to apply the presented methods for the last 20 years of continuous seismic data at Mt. St. Helens. What is available in the class github repository is partially not made for such long time series. Especially the covseisnet part includes a lot of computational power and it is of interest to calculate the spectral with on a daily basis and save the output. The plotting then will be the second step. This split reduces the memory load and is more efficient. For longer time series I use a slightly different piece of code which is parallized. I would like to apply the procedure, especially the covariance spectral width to DAS data, because increasing the number of stations improves the result.
