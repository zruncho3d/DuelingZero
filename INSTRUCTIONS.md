## Printing Instructions

Parts in this repo are intentionally only the delta from other projects, so that as those projects evolve, you get the latest parts, and there's no copy/paste maintenance overhead.

For settings:
* Use BoxZero settings for BoxZero corners.
* Use Tri-Zero settings for Tri-Zero parts.
* Use ZeroPanels settings for ZeroPanels parts.
* Standard Voron settings should be fine for all custom parts: 40% infill, 4 perims, 5 top/bottom layers, 0.2mm layer height.  Lower infill is likely fine.

BoxZero corners will need a lower layer height (0.16 mm) and/or wider extrusion width (0.55 mm), as they have the highest-angle overhangs.

A distinct color per gantry and per toolhead really does help keep things sane!  It's easy to get turned around when the gantry is upside-down, and when each gantry itself is flipped from the usual V0 orientation.

## Assembly Instructions

In general, the CAD should be your primary reference.  Don’t expect 100% of all screws and nuts to be present in CAD, though... the model is already big enough, and I've left out some bits that should be obvious.

### Prep

* Join extrusions as needed with 20mm set screws, using the BoxZero instructions for this:
  * 4x 200 + 200
  * 2x 200 + 100 (front, color-matched)
  * 10x 200 + 50
* Drill new holes for blind joints, using the V0 drill guide.
  * 8 holes in the back 400mm verticals at ends
  * 4 repositioned gantry blind access holes in the 300mm.  Use the 15mm corner cubes for these to get the right position with the drill guide.
* Print out a small army’s worth of no-drop nuts [NDN](https://github.com/zruncho3d/f-zero/tree/main/STLs/NoDropNuts)s.  Size these to your extrusions.  If using a mix of LDO + MBXL, keep them apart, as the sizes will be different.  You don’t want to have to pause the build for these, or hold off on adding them everywhere because you’re running low.
* Print out extra cable channels and Wago mounts.

#### Build

It’s a cake with layers.  You make the layers independently.

![](Images/build/layers.jpeg)

Then you join them.

You don’t need to follow the order below, but it’s known to work.  In all steps, make sure to add more NDNs that you think might need!  You’ll need a lot, especially as all corners add 4-6 NDs.

In all steps, get screws finger tight, but wait until the printer includes all parts to fully tighten all (accessible) screws.

Layers:
* Build the base + skirts layer, along with lower corners.
* Build the bedframe (for T0)
* Build the rear Z assembly, with rails or sliders, and join it to the rear crossbar.
* Build the complete double-gantry.
    * Add X rails to X extrusions
    * Add Y extrusions to the complete gantry frame
    * Add cable channels and umbilical plates to the gantry frame
    * Build BoxZero AB blocks
    * Build BoxZero-derived idlers
    * Build Y gantry crossbars, but don’t add the high-side Y strut yet.
    * Attach Y gantries to the gantry frame.
    * Add belts, with motors out; then add motors.
    * Attach toolhead carriages.
    * Add the high-side toolhead strut.
    * Add the high-side gantry strut.
* Build the top crown with 4 BoxZero-style corners and 4 horizontal extrusions.
* Assemble rear verticals with cable carriers.
* Assemble the front verticals with T0 parts and rails or sliders.

Main assembly:

* Add all verticals to the base, including the rear Z frame.  Now you have a "bed of nails" layout.
* Slide in the gantry from above, matching each nail in the "bed of nails".
  * Recommended: use the joining point of the verticals as a measurement reference to get the gantry at a level height.
  * Do an initial tightening.
* Slide on the top crown.
* Tighten all non-gantry screws.  A lot of them.
* Measure and align the gantry, so that it is as parallel as possible to the bed.  Tighten all gantry-to-frame screws (12).
* Add Z belts and attach bedframe.
* Attach toolheads.

Do all the wiring. Note stepper orientations:

* X Stepper Input to Left Rear Stepper
* Y Stepper Input to Left Front Stepper
* Z Stepper Input to Right Front Stepper
* E Stepper Input to Right Rear Stepper

The order for the two gantries is not the same, intentionally, because of the reversed orientation of one gantry to the other.

Stepper, endstop, and toolhead (CAN) wires are meant to pass through the rear BoxZero-style corners.

TBD: pic of underside wiring and near-steppers wiring

## Firmware Instructions

### “Two of everything but the Pi” Klipper Config notes {#“two-of-everything-but-the-pi”-klipper-config-notes}

* Install as usual on a Pi; I used MainsailOS.
* Install [KIAUH](https://github.com/th33xitus/kiauh) per repo instructions.
* Using KIAUH, remove the existing MainsailOS image-installed Klipper and Moonraker.  You can leave Mainsail.
* Using KIAUH, add 2 instances of Klipper and Moonraker.
* For simplicity (two UIs simultaneously), add Fluidd via KIAUH
    * Call the Klipper instances klipper-right and klipper-left
    * Call the Moonraker instances moonraker-left and moonraker-right
* In ``/home/pi/klipper_config`, add `left/` and `right/`` dirs.
    * Into each, copy any needed config.
* Ensure there is a left and right systemd service for each kind and side.
    * Check files like `/etc/systemd/system/moonraker-right.service` - that kinda thing.
* Mod configs for Moonraker services to reference the correct distinct config file directories.
    * vim /etc/systemd/system/moonraker-right.service
    * Example changes:

          [Service]
          ...
          Environment=MOONRAKER_CONF=/home/pi/klipper_config/**right**/moonraker.conf
          ...
          Environment=MOONRAKER_LOG=/home/pi/klipper_logs/moonraker-right.log

* Reload changes services as needed
    * `sudo systemctl daemon-reload`
* Mod fluidd local config to connect to the second Moonraker instance.
    * Imagine you have two Moonrakers at `dz.local:7125` and `dz.local:7126`, with fluid on port 81.
    * Mod right/moonraker.conf: CORS change to add `http://dz.local:81/` so Moonraker-right can connect.
    * URL was the Moonraker one defined in fluidd/mainsail (duh!) - Add a printer and put the second URL in, something like `http://dz.local:7126/`.
* Make sure each Klipper references the correct side in printer.cfg - a one-line change.
