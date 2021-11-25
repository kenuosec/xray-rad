@echo off
if not defined bflag set bflag=1 && start wt --title "xray" %0 && exit
xray.py
@cmd /k