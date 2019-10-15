# Abramov et al. parameters

# fimi_grayscale
window_pix_h = 1280
window_pix_v = 1080
frameDur = 1/85

# Grating
stim_dur_secs = 2
ramp_up_secs = .5
full_scale_secs = 1
ramp_dn_secs = ramp_up_secs

grating_deg = (3.2, 3.2)
max_contr = 0.5
spfreqs = [1, 20]
spf = spfreqs[0]
tfreqs = [1, 20]    # Hz
tf = tfreqs[0]      # Hz
cyc_secs = 1/tf     # seconds

# Donut/response frame
donut_outer_rad = 3.5
donut_inner_rad = 3.2
donut_color = .6

# Interstimulus and intertrial timing
iti = 3.0           # seconds
isi_min = .250      # seconds
isi_max = .500      # seconds
iti_min = 1.0       # seconds
iti_max = 2.5       # seconds
