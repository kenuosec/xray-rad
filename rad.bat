@echo off
if not defined bflag set bflag=1 && start wt --title "rad" %0 && exit
rad.py
@cmd /k