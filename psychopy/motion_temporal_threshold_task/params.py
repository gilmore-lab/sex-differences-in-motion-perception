# Murray et al. parameters

"""
This code is an attempt to replicate the Murray et al. 2018 study on sex differences in temporal motion detection thresholds.

Murray, S. O., Schallmo, M.-P., Kolodny, T., Millin, R., Kale, A., Thomas, P., Rammsayer, T. H., et al. (2018). 
Sex Differences in Visual Motion Processing. Current biology: CB. 
Retrieved from http://dx.doi.org/10.1016/j.cub.2018.06.014
"""

# fimi_grayscale
#monitor_name = 'fimi_grayscale'
#window_pix_h = 1280
#window_pix_v = 1024
#frameDur = 1/85

# testMonitor
monitor_name = 'testMonitor'
window_pix_h = 800
window_pix_v = 600
frameDur = 1/60

# Data file parameters
task_name = "temp_thresh"

# Fixation
fixation_secs = .850
fixation_grating_isi = .15

# Grating (not fixed for this study, must calculate based on current temporal duration in staircase)
stim_dur_secs = 2
ramp_up_secs = .5
full_scale_secs = 1
ramp_dn_secs = ramp_up_secs

grating_deg = (10, 10) # 
max_contr = 0.98 # Add 0.03?
spfreqs = [1.2]
spf = spfreqs[0]
tfreqs = [4]    # Hz
tf = tfreqs[0]      # Hz
cyc_secs = 1/tf     # seconds
max_resp_secs = 5
grating_ori = 0

# Donut/response frame
show_response_frame = True
donut_outer_rad = 10
donut_inner_rad = 9.7
donut_color = .55

# Interstimulus and intertrial timing
iti = 3.0           # seconds
isi_min = .250      # seconds
isi_max = .500      # seconds
iti_min = 1.0       # seconds
iti_max = 2.5       # seconds
