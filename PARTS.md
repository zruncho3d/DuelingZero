## Parts List

In general, none of the parts here should be a surprise.  Beyond anything D0-specific, you'll need everything to build at least one V0, likely a Tri-Zero, but also everything for the Boops and extra toolhead.

#### Rails

| Part | Qty | Qty | Notes |
| - | - | - | - |
| X rails | [300mm MGN7H](https://www.aliexpress.com/item/2251832694486732.html?) | 2x | Make sure to also buy a ‘Carriage Only’ part and message the seller to add it to the rail before they ship it. |
| Y rails | [250mm MGN9H rails](https://www.aliexpress.com/item/2251832586981749.htm) | 2x | Make sure to order high (Z1) preload |
| Z rails | 200mm-220mm MGN7H | 4x | |

#### Extrusions

NOTE: the CAD is not the right size.  It's Zruncho's build size.  Which doesn't quite get you a full 180 cube.

The recommended frame size enables a full 180x180x180 build volume, with a bit of extra travel in the rear Y area for a nozzle endstop, nozzle brush, and maybe a camera for alignment.  Yes, you can build a smaller test bed build, but the travel won't be practical.

You can start from a V0 kit and end-join (BoxZero-style) the chunks ([process described here](https://github.com/zruncho3d/BoxZero#assembly-notes)), as well as use 1515 supplements cut to length to get a choice of color.  If the size is close for the verticals, you can bridge the gap slightly with BoxZero corners (e.g., 400 + 50 -> 450 with B0 corners).

For build areas beyond 180x180 in XY, frame stability becomes a question, and girthier-than-1515 extrusions may be needed - or at least, some form of frame bracing.

1515 extrusions:

| Part | Qty | Dimensions | Notes |
| - | - | - | - |
| frame/gantry/bedframe/rear-brace x-dir | 8 | 350mm |
| frame Y-dir | 4 | 260mm |
| frame Z-dir | 4 | 450mm |
| gantry fixed small Y-dir | 2 | 160mm |
| bedframe Y-dir | 1 | 160mm |
| gantry moving Y-dir | 2 | 250mm |

These parts should yield travel of approximately 188 x 194 x 180 in XYZ.

#### Panels

The bottom baseplate has a complex shape, but all other panels are simple rectangles.

The way to think about the sizes is like this:
* **the baseplate** fits within extrusions, so its size is the inner extrusion size + 4.5mm to fill each extrusion slot - so, inner size + 9mm in total.
* **the exterior panels** fit on top of the extrusions; foam tape and the panels need to cover the 6mm gap to where ZeroPanels plastic fills the extrusion slot, on both sides.  So: inner size + 12mm.

If your panel supplier or extrusion supplier can't guarantee tight tolerances, you may want to drop each size by 1mm to ensure clearance.

| Part | Qty | Dimensions | Material |
| - | - | - | - |
| Baseplate | 1x | 359 mm x 269 mm (with cutouts - TBA to repo!) | 3mm ABS or ACM |
| Front/Back | 2x | 362 mm x 432 mm | 3mm Acrylic in front; acrylic or ABS/ACM in back |
| Sides | 2x | 282 mm x 443 mm | 3mm Acrylic |
| Top | 1x | 362 mm x 282 mm | 3mm Acrylic |

#### Triple-Z vs Single-Z

You can actually do a single-Z-motor build if you want, and then the whole shebang can use 7 drivers and a single board.  This option isn’t shown in CAD, but should work with stock V0 parts, or maybe minor changes.

If you’re not a fan of cantilevers (Zruncho's hand just raised, too...), and you want a more scalable printer (especially to the T0+50mm size), Tri-Zero is a good option, at the small cost of adding 2 extra Z stepper drivers, motors, and a few other motions parts.  It also has a nozzle endstop by default, which enables automatic, or at least measurement-supported, Z offset calibration.  This alone is a reason to use Tri-Zero, given the importance of the first layer in 3D printing.

#### Control Boards

The control board situation is up to you.  In theory, any boards should be fine, as long as you get enough steppers.  

Gantry boards (GBB15) are highly recommended, as they enable a single cable per side, as well as easier toolhead-cable plug/unplug.

Toolhead boards are highly recommended, as they simplify your wiring; CAN and USB enable a much smaller main control board, too.
