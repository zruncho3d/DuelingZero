## Design Walkthrough

Whenever I see an interesting new printer, or even a non-trivial mod, I don't want to just get access to the STLs or CAD...

I want to know what the designer was thinking, and why.  

I want to learn from them, to understand the design, as well as how it can be improved.

I want to avoid wasting time going down dead-ends trying to make it better, especially ones the designer has already gone down.

Dueling Zero will probably evolve faster with more eyes and more CAD designers taking a crack at it.  So to encourage action there, this section provides a walkthrough of the current status of the Dueling Zero design, covering all the key parts that are unique to it.  At the end are bonus pics from the early prototypes.

**The #1 thing about the design: it's all about being pragmatic**.

D0 is heavily optimized for using off-the-shelf parts from the stock V0 parts catalog, with off-the-shelf geometry... vs optimized for motion travel, or cost, or anything else.

Put another way, optimized for time-to-market.

**It’s not squeezing out every mm, and should have plenty of opportunities for travel optimization later.**

With that small caveat out of the way... I think there’s a lot of interesting stuff here!

More changes were needed than originally expected, and this section tries to summarize those changed or completely new parts.  Surprisingly, the toolheads and almost all Z parts are unmodified.

Highlights:

* No fundamentally new non-printed parts are needed.  You don’t need to cut any extrusions, and few holes need to be drilled.
* The entire gantry floats within the frame.  After building, you can loosen 12 screws and then slide it up or down to balance umbilical rubbing against Z travel.
* Correct, *there are no Z rails*.  This is not a CAD mistake.  I didn’t feel like buying any, and I didn’t know the optimal size anyway.  Printed sliders work fine as a replacement for rails, and you should expect more info about them soon.  If you want proper Z rails, no problem! They'll fit in place, just like on a regular T0.

### XY Motion

The soul of *this* new machine.  A two-headed beast.

![alt_text](Renders/gantry_iso.png)

The low-side (black, left-side) gantry went first, as I really wanted to improve the belt-mounting path on the carriage first, and *then* modify the resulting carriage design to support a higher set of belt mounts.

#### Low-side gantry

Take a look.  It's now underslung:

![](Renders/walkthrough/low_side_iso_perspective.png)

##### New Short X Carriage

The new X carriage is based on Double Dragon X carriage geometry, but modified to support both belts in one carriage.

![](Renders/walkthrough/low_side_x_carriage_iso_ortho.png)

This new X carriage improves on the stock V0 carriage by enabling the belt loops to come back on the sides, providing grip for future re-belting, especially for printers where you can’t loosen the front idlers.

| ![](Renders/walkthrough/low_side_x_carriage_front_ortho.png) | ![](Renders/walkthrough/low_side_x_carriage_side_ortho.png) | ![](Renders/walkthrough/low_side_x_carriage_top_ortho.png) | ![](Renders/walkthrough/low_side_x_carriage_rear_ortho.png) |
| - | - | - | - |

Highly recommended for your regular V0 or V0 mod!  Having to clip belts to length sucks.  No more, with this part.  You can see the belt path from the section view below.

![](Renders/walkthrough/low_side_x_carriage_sectioned_iso_perspective_2.png)

Note also: this part is MGN9C-only.  MGN9C is a great mod to reduce the potential for "toolhead flop".  With the default low-preload MGN7 rails, especially when combined with a plastic carriage, there is a possibility of unwanted toolhead motion.  MGN9C adds a little weight and size, but you can trust the rigidity more.

##### Low-side XY Joints

These are a flipped-upside-down version of the original V0.1 XY joints:

![](Renders/walkthrough/low_side_front_ortho.png)

The flipped orientation enables both gantries to share the same pair of rails.  A few counterbores had to be reversed and the height for extrusion mounting needed a lil' adjustment, but that was it.

| ![](Renders/walkthrough/low_side_xy_joint_assembly.png) | ![](Renders/walkthrough/low_side_xy_joint_ortho.png) | ![](Renders/walkthrough/low_side_xy_joint_only_iso.png) |
| - | - | - |

The endstop mounting on one side is simple and adjustable.  It's a hole for a screw to form a thread.  The edge of a SHCS hits the plunger on a microswitch, directly.

![](Renders/walkthrough/low_side_xy_joint_endstop.png)

#### High-side (high) gantry

This is the much more interesting half, with some new stuff:

![alt_text](Renders/walkthrough/high_side_front_ortho.png)

The challenge here is that when you flip the belts to live above the carriages, the belts want to go through the extruder motor.  So you have to find a way to terminate the belt connections in a tight space, at a location that is away from the original crossbar, and hence, subject to large forces from the belt tension.

| ![alt_text](Renders/X_Gantry_High_Side_iso.png) | ![alt_text](Renders/X_Gantry_High_Side_rear_iso.png) | ![alt_text](Renders/X_Gantry_High_Belts.png) |
| - | - | - |

Reminds me a bit of the [Narushevich](https://www.airplane-pictures.net/manufacturer.php?p=1458)!

The toolhead looks like this, and has some real advantages.

| ![](Renders/walkthrough/high_side_x_assembly_side_ortho.png) | ![](Renders/walkthrough/high_side_x_assembly_front_ortho.png) | ![](Renders/walkthrough/high_side_x_assembly_top_ortho.png)
| - | - | - |

For example:
* You can remove the Sherpa Mini extruder while leaving the toolhead board, carriage mount, and cowling in place.  Extruder maintenance is super-easy: remove two screws and one plug.
* The toolhead board mount is much more rigid, which should provide more faithful Input Shaper measurements for toolheads with integrated ADXLs (like Huvud 0.61, FLY-SHT42, or EBB42).
* The MiniAS supports a wide variety of hotends, and even multiple extruders.  It's a nice design.
* You can easily change out the entire X carriage assembly and retain the original tensioning setting.

However, the design is currently specific to the motor positioning of the MiniAS and the Sherpa Mini.  You can't currently use a MiniAB, as the holes there would be much lower, because the motor mounts lower.   

##### New Tall X Carriage

You've probably never seen a carriage mount quite like this. It’s a mod of the low-side X carriage, with provisions for belt attachments as well as a more rigid toolhead board mount.

| ![](Renders/walkthrough/high_side_x_carriage_front_ortho.png) | ![](Renders/walkthrough/high_side_x_carriage_iso.png) | ![](Renders/walkthrough/high_side_x_carriage_iso_2.png) |
| - | - | - |

The lower belt attachments remain, so that you can use the same part on the low side too, with the benefit of the more rigid toolhead board mount.  This isn't shown in the renders yet, but it's not too hard to imagine.

##### Belt Grabs

The geometry of the belt attachments comes from F-Zero and Tri-Zero, which use toolless belt grabs for their Z axes.  

![](Renders/walkthrough/belt_grab_iso_perspective.png)

This geometry works great here too, and it makes the entire toolhead easy to remove and then add back.  That’s important for a designer expecting to make many X carriage tweaks, for example, to add wire management, but probably not a big benfits for most builders.  

##### Toolhead Board Mount

The toolhead mount is sized for a NEMA17-hole-pattern-compatible square toolhead board.

![](Renders/walkthrough/high_side_toolhead_board_mount.png)

For now, this part assumes board-specific spacers to work with multiple board-spacer heights, but it could (and probably should) be an integrated part in the future with board-height-specific variants.

##### Y Toolhead Strut

This part strengthens and locks in all the belt grabs, but also provides a surface to rigidly mount the toolhead plate on top.

![](Renders/walkthrough/high_side_x_top_strap_iso_perspective.png)

The whole X assembly here is so much more rigid than in Double Dragon, where the entire toolhead board and shroud is dangling and can flex behind the extruder stepper.

##### Y Gantry Strut

Why?  Without this, the belt tensioning forces bend the upper XY joints inwards, which would surely cause belt damage over time.  Resist the forces!

![](Images/build/gantry_strut_power.jpeg)

Going with a strut was the fastest design solution here.  I don't particularly like it.  It gets in the way of tightening things.

In a future design, a symmetric gantry with changed motor and cowling mounts might remove the need for this part entirely.  

##### High-side XY joints

These ended up as a 4-part stack.  The geometry complexity enables support-free printability.

![](Renders/walkthrough/high_side_xy_joint_iso_perspective.png)

It's not the most elegant, but it works.  And it's rigid enough to transfer belt tensioning forces to the strut.

| ![](Renders/walkthrough/high_side_xy_joint_front_ortho.png) | ![](Renders/walkthrough/high_side_xy_joint_side_ortho.png) | ![](Renders/walkthrough/high_side_xy_joint_top_ortho.png) |
| - | - | - |

#### X Endstops

The new height of the gantry crossbar relative to the AB blocks meant that the endstop had to move.  Here, it’s a minimal, adjustable, and symmetric design.

![](Renders/walkthrough/x_endstop.png)

A similar matching part holds the microswitch to the gantry crossbar.  

![](Renders/walkthrough/x_endstop_switch_mount_iso.png)

NOTE: on D0 these are X endstops.  On a V0 or similar, these would be Y endstops.  It's all twisted!

#### Modified BoxZero AB blocks

To get closer to full X motion, BoxZero idlers needed a mod to provide more clearance for a "toolhead backpack" - the area behind the motor where a toolhead board can go.  Normally such a cutout wouldn’t be needed, but the changed height of the fixed gantry-frame crossbar causes the toolhead-board backpack to get in the way.

![](Renders/walkthrough/high_side_ab_highlighted_iso_perspective.png)

This notched version is only needed on the high-side gantry, so if converting from a regular B0, you can reuse the AB blocks.

#### BoxZero-derived idlers

![](Renders/walkthrough/idlers_highlighted_side_ortho.png)

These parts are not strictly needed, and in fact, originally the gantry used stock B0 idlers, but they provide visual symmetry with the AB blocks (I know, I know...).

![](Renders/walkthrough/idlers_iso_perspective.png)

These use the usual V0 9mm drive spacers.

#### Toolhead Umbilical Receiver

Derived, in principle, from the F0 umbilical, but without a cover.  Fits a cable gland and routes wires to the nearby cable channels.

![](Renders/walkthrough/umbilical_receiver_iso_perspective.png)

A potential improvement here: to add push-fit connections on top and bottom, to enable low-friction rotation of the reverse bowden tube, as well as enable variable-length reverse bowden tubes to the filament feed.


### Z Motion

#### Z Sliders

Oh yes.  They’re real, and they’re spectacular :smile:.  

## [>>> See YouTube video of sliding motion!](https://youtu.be/JXZt2rP1yQQ)

| ![](Renders/walkthrough/mgn7h_slider_bottom_iso_ortho.png) | ![](Renders/walkthrough/mgn7h_slider_end_ortho.png) | ![](Renders/walkthrough/mgn7h_slider_top_iso_perspective.png) |
| - | - | - |

They're extremely simple and low-cost. Each uses the geometry from a ZeroPanels panel, extruded, with 4 holes added to match a typical MGN7H carraige.

They're flexible.  Literally... the flex makes it possible to insert and remove them without taking a rail apart.

The key to making them properly is to use the edge of an extrusion as a planer to gently remove a tiny amount of plastic, so that the printed slider fits tightly in place, without backlash or excessive friction. You can get the technique pretty easily, and if you screw up, just throw it away and start again.  Remove move material equally from both ends of one side, gentry, until you notice the grip lessen as you slide the slider in the exact extrusion you'll be using.  Yes, matching each slider to the extrusion helps.  There is surprising variance not just between extrusion brands, but also batches, and even between slots on the same extrusion piece.  You can probably also modify the geomtry slightly to get really close without the planer action.

These work fine without lube, but with a little Super Lube, they’re comparably smooth to actual rails.  Don’t expect them to handle large side or twisting loads, but for the highly constrained loads they have (up and down Z), they seem just fine, especially with the front bedframe and rear Z designs here that support tensioning.

In the future, these can be easily changed to *not* stick out the sides, to enable the use of flush-fitting default V0 side panels.

#### Front Idler Mounts

This is a surprisingly interesting part.

From the front view, you see a boring old box.  

![](Renders/walkthrough/front_idler_base_front_ortho.png)

Soooo boring, right?  But this part hides a secret entrance.

You need space for a screw head to go in, but a straight screw would conflict with the tensioning screw and heatset used with T0.  Sure, you could make this part and the corresponding Z idler wider... unlike T0, the space is available; there's a huge gap from these parts to gantry with the superwide layout.  But  that's lazy talk.  I wanted to keep the parts as stock as possible here, to reduce the time cost of conversions.

The solution: add an oblique-angled access hole for a balldriver to tighten the main screw, combined with a slot to insert that screw without requiring disassembly.

![](Renders/walkthrough/front_idler_base_iso_oblique.png)

You can see the slot above, peeking through the oblique access hole.

| ![](Renders/walkthrough/front_idler_base_bottom.png) | ![](Renders/walkthrough/front_idler_base_side_inner.png) | ![](Renders/walkthrough/front_idler_base_iso.png) |
| - | - | - |

After all - once you've built the double-gantry unit, you really don't want to take it apart again.   You can’t see the angled hole for screw access, or the area where the part slides in!  Just looks like a box from the outside.

#### Unmodified T0 Rear Z Motor Mount

This one was a happy little accident.

![](Renders/walkthrough/bottom_view_iso_perspective.png)

The T0 rear Z motor mount part did not need to be modified.  The motor is flipped from its usual orientation, with simple spacers added so the belt can escape through.

One part that didn't demand a redesign.... I'll take it.

#### Rear Z "Crossbar Corners"

These take geometry cues from the BoxZero corners:

![](Renders/walkthrough/rear_z_crossbar_corner.png)

They enable a mount for the modified ZeroClick dock, as well as the rear Z parts.

Since no blind joints are used here, this part can slide up and down at will...

#### Unmodified T0 Rear Z Idler Base

... which helps set the rear Z height.  Z can be adjusted after the frame has been built.

![](Renders/walkthrough/rear_z_idler_mount.png)

This whole area is unmodified T0 stuff, currently.

It's absolutely a place where there's tons of opportunity to get back Z, possibly even without parts changes, just by raising the rear Z crossbar and adjusting the Zeroclick dock to match.

It's also a design that isn't truly locked-in, to properly resist Z tensioning forces.  Extending the rear Z idler base to lock against the rear Z crossbar would solve this potential issue, easily.

#### Larger bedframe, with new Wago mounts

This is more of a T0+ thing, but it's worth calling out, until T0+ is separately released and documented.

![](Renders/walkthrough/bed_bottom_iso_perspective.png)

A few small mods were needed:
* Widened-by-15mm T0 Bedframe Z Mounts
* Fromt bed mounts adjusted to fit the 180x180 bed.

![](Renders/walkthrough/bed_side_ortho.png)
![](Renders/walkthrough/bed_front_ortho.png)
![](Renders/walkthrough/bed_top_ortho.png)

The widened front-corner Z mounts have a side hole added to enable preload adjustment.  Haven't tried these out yet, but they should help with fine-tuning the Z motion, and possibly increasing the friction, intentionally, to increase the bed hold.

### Frame

#### Modified BoxZero Corners

BoxZero corners provide a nice bump in rigidity for 1515 frames.  Instead of a 7.5mm offset with a single screw, most corners have two screws and a 37.5mm offset.

Since the default D0 size is wider, taller, and deeper, it make sense to add 4 more BoxZero corners to the bottom of the frame for even more rigidity.  Since the optimal size seemed close to 330mm, adding 15mm to each end seemed logical, to enable off-the-shelf 300mm extrusion packs.

Here are the 3 new variants, each of which has a mirrored version too:

| ![](Renders/walkthrough/corner_1_iso_ortho.png) | ![](Renders/walkthrough/corner_2_iso_ortho.png) | ![](Renders/walkthrough/corner_3_iso_ortho.png) |
| - | - | - |

The bottom rear corners provide a large opening for cables, so that 2 stepper cables, an endstop cable, and a full toolhead cable can pass through the frame without issue.

#### Modified ZeroClick Dock

ZeroClick handles probing here.

![](Renders/walkthrough/zeroclick_dock_iso_perspective.png)

The usual ZeroClick Side Dock needed a few mods to fit here: changes to depth, height, and even a shave off the top.

#### Cable Channels

These derive from ones first made available with Double Dragon:

| ![](Renders/walkthrough/cable_carrier_end_perspective.png) | ![](Renders/walkthrough/cable_carrier._iso_perspective.png) |
| - | - |

There's one on each side of the umbilical receiver to hold and hide the stepper and toolhead cables.

### Other Mods

Even more mods... these were all straightforward:
* 25mm T0 Side Skirts added for the longer depth
* 65mm T0 Front Skirts added for the custom width



### Prototypes

If you have V0 AB blocks lying around, you can even make a test gantry like this:

| ![](Images/test_gantry/top_real.jpg) | ![](Images/test_gantry/test_gantry_side.jpg) |
| - | - |

This was the first test gantry to prove out the concept.  BoxZero AB blocks are a much better fit, though, as they enable you to build the gantry separately, then drop it into the frame from the top.  

The second test gantry moved to BoxZero-derived ABs, with additional width and length, and lived for a bit in a "stubby Z" test config.  This one had an unpowered Z travel of 10mm (!), but it helped with iterating on gantry and bed parts.  In particular, the test gantry made clear that achieving a target X motion of 170mm would require adding width.

| ![alt_text](Images/test_build/top.jpg) | ![alt_text](Images/test_build/front.jpg) | ![alt_text](Images/test_build/side.jpg) |
| - | - | - |

The third and final gantry is 30mm wider, using 15mm corner cubes between 300mm horizontal extrusions and the frame.  Once belted up, this gantry supported validation of the collision avoidance code.  Let’s just say the toolheads have butted heads once or twice!
