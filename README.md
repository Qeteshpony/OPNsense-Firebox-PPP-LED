# OPNsense-Firebox-PPP-LED
Injects LED control commands into the OPNsense ppp-up and -down scripts for Firebox M400/500 hardware

Uses https://github.com/stephenw10/WGXepc to control the LEDs on a Firebox

Copy to /usr/local/etc/rc.syshook.d/early/20-injectWGXepc and chmod to 755
