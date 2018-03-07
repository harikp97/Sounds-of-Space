# Sounds-of-Space
Creating music assosciated with astrophysical phenomena


The backbone of the motivation for this project comes from the fact that any two time varying properties of an astrophysical phenomenon or an astronomical body can be mapped to frequency and amplitude to create music. 

1)Gravitational waves are a natural candidate as the data obtained is essentially an amplitude-time plot. The waveform for coalescing binaries was created in the frequency domain and inverse Fourier transformed to get the chirp sound.
Files - template.py, LIGO_sound_generator.py

2)The orbit of an eccentric body was used to create music with the velocity mapped to frequency and distance from the focus deciding the amplitude. Both a continuous version and discrete version was created. In the continuous version, the velocity values were mapped to frequency values within a range and played at the corresponding time. In the discrete version, the frequency range was binned such that all velocity values mapped to one of the notes in the octave. The amplitude was a function of the distance and the relation could be made either an inverse one or an exponential decay.
Files - orbit_continuous.py, orbit_discrete.py

3)Worked on mapping the spectral types of stars to the notes in an octave and spacing the notes according to their rise times to create a "Star Walk".
Files -  	star_walk_wav.py

4)Making use of the lighthouse like property of pulsars, a note depending on their frequency of revolution was played every time its beam pointed towards the earth.
Files - pulsars.py

5)The trajectory of a rocket was simulated using parameters like initial mass, air density, drag coefficient, frontal reference area, fuel mass flow rate etc. The velocity and height from the surface was mapped to frequency and inverse of amplitude to create tones.
Files - rocket_trajectory.py
