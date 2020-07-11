# -*- coding: utf-8 -*-
version = 2

# https://github.com/jketterl/openwebrx/wiki/Configuration-guide

# Settings RTL_SDR Version 3 on Raspberry Pi 4 4gb USB-2 Port

# *** reduce if audio underruns while CPU usage is 100%

# ==== Server settings ====
web_port = 80						
max_clients = 2	# *** reduce if audio underruns while CPU usage is 100%

# ==== Web GUI configuration ====
receiver_name = "N3FTU"
receiver_location = "Clearwater Beach Florida USA"
receiver_asl = 0
receiver_admin = "rpsmithii@mac.com"
receiver_gps = {"lat": 27.971900, "lon": -82.826500}
photo_title = "Clearwater Beach"
photo_desc = """
Operated by: <a href="mailto:%[RX_ADMIN]">%[RX_ADMIN]</a><br/>
Device: %[RX_DEVICE]<br />
Antenna: %[RX_ANT]<br />
Website: <a href="http://radical" target="_blank">http://radical</a>
"""

# ==== sdr.hu listing ====
sdrhu_key = ""
sdrhu_public_listing = False
server_hostname = "localhost"

# ==== DSP/RX settings ====
fft_fps = 9					# *** reduce if audio underruns while CPU usage is 100%
fft_size = 4096  				# *** power of 2 reduce if audio underruns while CPU usage is 100%
fft_voverlap_factor = (
    0.3  					# >0 multiple FFTs used for diagram lines
)						# *** reduce if audio underruns while CPU usage is 100%
audio_compression = "adpcm"  			# valid values: "adpcm", "none"
fft_compression = "adpcm"  			# valid values: "adpcm", "none"
digimodes_enable = True  			# Decoding digimodes come with higher CPU usage.
digimodes_fft_size = 1024
digital_voice_unvoiced_quality = 1		# quality, and thus the cpu usage, for the ambe codec
digital_voice_dmr_id_lookup = True		# enables lookup of DMR ids using the radioid api

# ==== I/Q sources ====
sdrs = {
    "rtlsdr": {
        "name": "RTL-SDR",
        "type": "rtl_sdr",
        "ppm": 0,
        "profiles": {
            "NOAA": {
                "name": "NOAA Weather",
                "center_freq": 162475000,
                "rf_gain": 30,
                "samp_rate": 2000000,
                "start_freq": 162475000,
                "start_mod": "nfm",
            },
            "2m": {
                "name": "2m Packet",
                "center_freq": 144390000,
                "rf_gain": 30,
                "samp_rate": 2000000,
                "start_freq": 144390000,
                "start_mod": "nfm",
            },
			  "70cm": {
                "name": "70cm 440",
                "center_freq": 438800000,
                "rf_gain": 30,
                "samp_rate": 2000000,
                "start_freq": 439275000,
                "start_mod": "nfm",
            },
            "FM1": {
                "name": "FM1",
                "center_freq": 9000000,
                "rf_gain": 10,
                "samp_rate": 2000000,
                "start_freq": 9000000,
                "start_mod": "FM",
            },
            "20m": {
                "name": "20m",
                "center_freq": 14150000,
                "rf_gain": 10,
                "samp_rate": 2000000,
                "start_freq": 14070000,
                "start_mod": "usb",
            },
            "30m": {
                "name": "30m",
                "center_freq": 10125000,
                "rf_gain": 10,
                "samp_rate": 2000000,
                "start_freq": 10142000,
                "start_mod": "usb",
            },
            "40m": {
                "name": "40m",
                "center_freq": 7100000,
                "rf_gain": 10,
                "samp_rate": 2000000,
                "start_freq": 7070000,
                "start_mod": "usb",
            },
        },
    },
}

# ==== Color themes ====
waterfall_colors = [0x000000FF, 0x0000FFFF, 0x00FFFFFF, 0x00FF00FF, 0xFFFF00FF, 0xFF0000FF, 0xFF00FFFF, 0xFFFFFFFF]
waterfall_min_level = -88  # in dB
waterfall_max_level = -20
waterfall_auto_level_margin = {"min": 5, "max": 40}
csdr_dynamic_bufsize = False  			# This allows you to change the buffering mode of csdr
csdr_print_bufsizes = False  			# This prints the buffer sizes used for csdr processes
csdr_through = False  				# True prints how much data is going into the DSP chains
nmux_memory = 50  				# (MB) nmux circular buffer size
google_maps_api_key = ""
map_position_retention_time = 2 * 60 * 60

wsjt_queue_workers = 2
wsjt_queue_length = 10
wsjt_decoding_depth = 3
wsjt_decoding_depths = {"jt65": 1}
temporary_directory = "/tmp"
services_enabled = True
services_decoders = ["ft8", "ft4", "wspr", "jt65", "jt9", "packet"]

# === aprs igate settings ===
# if you want to share your APRS decodes with the aprs network, configure these settings accordingly
aprs_callsign = "N3FTU"
aprs_igate_enabled = True
aprs_igate_server = "noam.aprs2.net"		# Worldwide Servers http://aprs2.net
aprs_igate_password = "xxxxx"			# Passwrd generator http://www.aprs-is.net/Connecting.aspx
aprs_igate_beacon = False
aprs_symbols_path = "/opt/aprs-symbols/png"

# === PSK Reporter setting ===
pskreporter_enabled = True
pskreporter_callsign = "N3FTU"

# === Web admin settings ===
webadmin_enabled = False
