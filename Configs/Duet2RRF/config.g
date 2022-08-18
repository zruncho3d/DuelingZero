; CoreXYUV Config, with 2 Toolheads defined
; X stepper: L2
; Y stepper: L1
; Z stepper: R1
; E0 stepper: R2

; General preferences
M575 P1 S1 B57600                              ; enable support for PanelDue
G90                                            ; send absolute coordinates...
M83                                            ; ...but relative extruder moves
M550 P"duelingzero"                            ; set printer name

; Network
M552 S1                                        ; enable network
M586 P0 S1                                     ; enable HTTP
M586 P1 S0                                     ; disable FTP
M586 P2 S0                                     ; disable Telnet

; Printer
M669 K8 ; switch to CoreXYUV mode
M569 P0 S0                                     ; physical drive 0 goes forwards
M569 P1 S1                                     ; physical drive 1 goes forwards
M569 P2 S0                                     ; physical drive 2 goes forwards
M569 P3 S1                                     ; physical drive 3 goes forwards
M584 X0 Y1 U2 V3 E4                            ; set drive mapping (CoreXYUV); E4 is a dummy but needed for tool defn's later.
M350 X16 Y16 U16 V16 I1                        ; configure microstepping with interpolation
M92 X80.00 Y80.00 U80.00 V80.00                ; set steps per mm
M566 X900.00 Y900.00 U900.00 V900.00           ; set maximum instantaneous speed changes (mm/min)
M203 X6000.00 Y6000.00 U6000.00 V6000.00       ; set maximum speeds (mm/min)
M201 X1000.00 Y1000.00 U1000.00 V1000.00       ; set accelerations (mm/s^2)
M906 X650 Y650 U650 V650 I30                   ; set motor currents (mA) and motor idle factor in per cent
M84 S30                                        ; Set idle timeout

; Axis Limits
M208 S1 X0 Y0 U0 V0                               ; set axis minima
M208 S0 X120 Y160 U120 V160                       ; set axis maxima

; Endstops
M574 X1 S1 P"xstop"                            ; configure switch-type (e.g. microswitch) endstop for low end on X via pin xstop
M574 Y2 S1 P"ystop"                            ; configure switch-type (e.g. microswitch) endstop for high end on Y via pin ystop
M574 U2 S1 P"zstop"                            ; configure switch-type (e.g. microswitch) endstop for high end on U via pin zstop
M574 V1 S1 P"e0stop"                            ; configure switch-type (e.g. microswitch) endstop for low end on V via pin ystop

;M574 Z1 S2                                     ; configure Z-probe endstop for low end on Z

; Z-Probe
;M558 P1 C"zprobe.in" H5 F120 T6000             ; set Z probe type to unmodulated and the dive height + speeds
;G31 P500 X0 Y0 Z2.5                            ; set Z probe trigger value, offset and trigger height
;M557 X15:120 Y15:160 S20                       ; define mesh grid

; Heaters
M308 S0 P"bedtemp" Y"thermistor" T100000 B4138 ; configure sensor 0 as thermistor on pin bedtemp
M950 H0 C"bedheat" T0                          ; create bed heater output on bedheat and map it to sensor 0
M307 H0 B1 S1.00                               ; enable bang-bang mode for the bed heater and set PWM limit
M140 H0                                        ; map heated bed to heater 0
M143 H0 S120                                   ; set temperature limit for heater 0 to 120C
M308 S1 P"e0temp" Y"thermistor" T100000 B4138  ; configure sensor 1 as thermistor on pin e0temp
M950 H1 C"e0heat" T1                           ; create nozzle heater output on e0heat and map it to sensor 1
M307 H1 B0 S1.00                               ; disable bang-bang mode for heater  and set PWM limit
M143 H1 S280                                   ; set temperature limit for heater 1 to 280C

; Fans
M950 F0 C"fan0" Q500                           ; create fan 0 on pin fan0 and set its frequency
M106 P0 S0 H-1                                 ; set fan 0 value. Thermostatic control is turned off
M950 F1 C"fan1" Q500                           ; create fan 1 on pin fan1 and set its frequency
M106 P1 S1 H1 T45                              ; set fan 1 value. Thermostatic control is turned on

; Tools
; https://docs.duet3d.com/User_manual/Reference/Gcodes#m563-define-or-remove-a-tool
; Note: Axes are mapped in the order XYZUVWABC, where X=0, Y=1, Z=2, U=3 etc, not by driver number.
M563 P0 D0 H1 F0 S"left"                       ; define tool 0
G10 P0 X0 Y0                                   ; set tool 0 axis offsets
G10 P0 R0 S0                                   ; set initial tool 0 active and standby temperatures to 0C

M563 P1 D0 H1 F0 X3 Y4 S"right"                ; define tool 1 motion;
G10 P1 U0 V0                                   ; set tool 1 axis offsets
G10 P1 R0 S0                                   ; set initial tool 1 active and standby temperatures to 0C

; Custom settings are not defined

