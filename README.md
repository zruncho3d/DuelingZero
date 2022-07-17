## Dueling Zero - a Dual Gantry V0 mod

Enable dual-color, dual-material, and even multi-part printing... with the same speed and quality as single-extruder printing.

Mod a [Voron Zero](https://vorondesign.com/voron0.1), or build one fresh.

**D0** is the only open-source, fully-documented, reproducible-by-anyone Dual Gantry printer out there.

And yes... it prints.

TBD: Youtube Video link

![alt_text](Images/test_build/top.jpg)

![alt_text](Renders/iso.png)

Renders:

| ![alt_text](Renders/top-2.png) | ![alt_text](Renders/front.png) | ![alt_text](Renders/side.png) |
| - | - | - |

Initial test build:

| ![alt_text](Images/test_build/top.jpg) | ![alt_text](Images/test_build/front.jpg) | ![alt_text](Images/test_build/side.jpg) |
| - | - | - |

"Real thing" pics coming soon - with wiring, enclosure, fully-built toolheads, etc.

## Release History

### 2022-07-X: Alpha-1  
This first release covers everything you need to build and run your own Dueling Zero: CAD, STLs, DXFs, sample firmware configs, smart avoidance code, G-code streaming code, instructions, and a parts list... everything but an illustrated manual.  But if you're reading this, you almost certainly don't need a manual, anyway.

To make it easy for anyone to grok this crazy Dual Gantry layout - and learn about its opportunities and challenges, both in hardware and software - this README walks through the software and the design.

Enjoy!  There's a lot of content here, and I hope you enjoy it as much as I did bringing this concept to life.  -Z.

Join the [Reddit thread (TBD)]() on `r/VoronDesign` for any comments, questions, or kudos.

## Overview

### What’s a Dual Gantry printer?

**Dual Gantry** is a rare 3D printer type with two toolheads moved by **two** *completely independent* XY motion systems:

![alt_text](Renders/top-2.png)

Yes, you’re seeing double, with black and silver toolheads in a dual-CoreXY motion configuration.

### Why a Dual Gantry printer?

In general, a second toolhead adds enormous flexibility - to support multiple colors, multiple materials, multiple nozzle sizes, and even multi-part printing.  Sounds good, right!

The typical way to add a second toolhead is to add it to the X rail, called IDEX (Independent Dual Extrusion).

Open-source IDEX designs include Zruncho’s [Double Dragon](https://github.com/zruncho3d/double-dragon), Eddie’s [Tridex](https://github.com/FrankenVoron/Tridex/), Ankurv’s IDEX Switchwire) and the [Muldex](https://github.com/3dprintingworld/MULDEX).  There's no shortage of commercial examples, too: [Sovol SV04](https://sovol3d.com/products/sv04), [FlashForge Creator Pro](https://www.flashforge.com/product-detail/flashforge-creator-pro-2-3d-printer), [BCN Sigma](https://www.bcn3d.com/bcn3d-sigma-d25/), [Jadelabo J1](https://www.jadelabo.com/), and many more.

But that second toolhead comes at a cost: moving mass, which has real effects on print speed (max accel) and quality (typically, ringing artifacts).

> Simplify, then add lightness - [famous quote from Colin Chapman at Lotus](http://www.lotuscars.com.tr/about-us/lotus-philosophy/index-31332.html#:~:text=At%20the%20root%20of%20our,was%20another%20of%20Chapman's%20premises.)

Whether building a fast race car or a fast printer, physics can't be ignored.  

You can mitigate the moving mass somewhat, by using lighter toolhead, typically with a remote Bowden extruder, but Bowden extruders introduce their own tuning challenges.

With Dual Gantry, you get a no-mass-added, no-downsides gantry for the common case of single-extruder prints.  There’s no hit to max acceleration or any potential ringing issues from dragging around a heavy second toolhead on a longer rail all the time, like on an IDEX.

This motion concept fits within a broader space of 3D printer types that support multiple extrusion, where the number of toolheads, hotends, and extruders vary... 1, 2, or N for each of these:

![alt_text](Diagrams/landscape_of_multiple_extruders.png)

Take a look.  This diagram is not comprehensive, but gives a sense for the depth of the design space.

### What’s the catch?

If it sounds too good to be true... it probably is.

You don't have to design it (anymore), but you still need to build it, which is roughly twice the work of a typical printer.  Compared to a typical single-extrusion, single-toolhead 3D printer, there are added cost, complexity, and alignment challenges, many of which are identical to IDEX.

**But the main reason you’ve probably never seen a Dual Gantry 3D printer: firmware support.**

RepRapFirmware *does* support two active gantries using one control board.

Klipper doesn’t, *yet*, but there’s a workaround.

**Regardless,** neither firmware implements the smart avoidance necessary for safe motion within the full area of bed travel.

This is not a blocker anymore, though!  

The code in this repo enables a functioning printer with full bed-travel usage.  See the [Software](#Software) section for a full explanation.

### How does this mod work?

Start with the trusted, tested Voron Zero CoreXY gantry.   Duplicate and rotate it, so that both gantries share the same rails.  Flip the XY joints upside down.  Voila!   

![alt_text](Renders/gantry_iso.png)

That’s the core idea.

In practice, though, there are quite a few additional bits to design to make it work.  And like with any V0 mod, the devil is in the packaging details: *every mm matters*.

Each gantry is heavily customized vs a regular V0, to make an underslung low-side gantry (left, in black) as well as an underslung high-side gantry (right, in silver). Beyond these new gantry XY joints, there’s some extra work to relocate the endstops and add a high-side strut; *something* needs to directly resist the forces of the tensioned belt.

Fortunately, most of the other needed parts can be repurposed or at least derived from other designs.  

**D0 Alpha-1** heavily leverages off-the-shelf parts from the [BoxZero](https://github.com/zruncho3d/BoxZero) and [TriZero](https://github.com/zruncho3d/tri-zero) mods, plus a few custom parts and custom panels.

### Zruncho’s Printer: D0.000

The first D0 build puts a [Tri-Zero](https://github.com/zruncho3d/tri-zero) Plus50 Z setup below, with two twisted-90-degree [BoxZero](https://github.com/zruncho3d/BoxZero) gantries above, using a V0-derived frame.

![](Images/build/together.jpg)

TBD: final images, not the test build!

Highlights of this particular build:

* LDO Red 1515 V0 frame kit, with added MakerBeamXL 300mm, 200mm, and end-joined 50mm pieces
* [Tri-Zero](https://github.com/zruncho3d/tri-zero) triple-belted Z (simple, low-cost, and fast) with tool-less belt attachments
* [ZeroClick](https://github.com/zruncho3d/zeroclick) for bed probing
* Rail-less Z motion (!) using printed MGN7 sliders - **new in this printer**
* Tool-less, removable-in-seconds sealed enclosure with [Technologic-style ZeroPanels](https://github.com/Tecnologic/ZeroPanels/tree/main/Mods/tecnologic/FlyingZero300/STLs)
* AC 180x180 [Prusa Mini size plate bed](https://www.aliexpress.com/item/3256803530287164.html) with removable textured PEI sheet
* 2x [Mini-AfterSherpa](https://github.com/PrintersForAnts/Mini-AfterSherpa) toolheads for Revo Voron
* 2x [Sherpa Mini](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder) extruders
* [BoxZero](https://github.com/zruncho3d/BoxZero)-derived motor blocks
* V0.1-size LRS-150-24 Power Supply
* [PrinterExperiments](https://github.com/zruncho3d/printer-experiments) code for easier Z nozzle alignment with a single command
* More F623 bearings than you’ve ever seen on one printer.  So many!
* Travel: ~170mm x 165mm in XY, ~130mm in Z (but completely unoptimized)
* Frame: 360 x 280 x 450 in XYZ.  Enclosure, feet, and displays add a bit to this.

Two control options have been tested:
* Control Option 1: RepRepFirmware with Duet
    * Duet2 Wifi + Duex5
    * 2x Pancake V0 toolhead boards
    * 5” PanelDue
* Control Option 2: Klipper
    * Raspberry Pi Zero 2 W
    * 3x SKR Pico controller boards
    * 2x EBB42 toolhead boards
    * Waveshare CAN hat
    * BTT U2C USB CAN board
    * Mini 12864 display with [Klipper adapter](https://www.aliexpress.com/item/3256802553287831.html)

Flexibility, or fear of commitment… you decide!

### Earlier Prototypes

If you have V0 AB blocks lying around, you can even make a test gantry like this:

| ![](Images/test_gantry/top_real.jpg) | ![](Images/test_gantry/test_gantry_side.jpg) |
| - | - |

This was the first test gantry to prove out the concept.  BoxZero AB blocks are a much better fit, though, as they enable you to build the gantry separately, then drop it into the frame from the top.  

The second test gantry moved to BoxZero-derived ABs, with additional width and length, and lived for a bit in a "stubby Z" test config.  This one had a unpowered Z travel of 10mm (!), but helped iterate on gantry and bed parts.  In particular, the test gantry made clear that achieving a target X motion of 170mm would require adding width.

| ![](Images/test_build/top.jpg) | ![](Images/test_build/front.jpg) |
| - | - |

The third and final gantry is 30mm wider, using 15mm corner cubes between 300mm horizontal extrusions and the frame.  Once belted up, this gantry supported validation of the collision avoidance code.  Let’s just say the toolheads have butted heads once or twice!

Final pics TBD.

Speaking of which… on to by far the most interesting & novel part on this mod, the software!

## Software

This early video shows the motion and introduces the core challenge: two toolheads moving in a shared space.  Didn't know if it work would at all when this was made!

[add to YouTube as unlisted]

[https://discord.com/channels/460117602945990666/982515287704354856/982518947876327425](https://discord.com/channels/460117602945990666/982515287704354856/982518947876327425)

There are a few ways to handle the "two toolheads, one workspace" challenge, for a single print.

Here are the different cases, visualized, with more details explanations below.

|  | Visualization | Usable Bed Fraction (for D0.000) |
| - | - | - |
| Legend | ![](Diagrams/workspace_legend.png) | - |
| Single Toolhead: full workspace | ![](Diagrams/workspace_single.png) | 100% |
| Dual Toolhead, Option 1: Park in Opposite Corners| ![](Diagrams/workspace_dual_corners.png) | ~50% |
| Dual Toolhead, Option 2: Park in Back | ![](Diagrams/workspace_dual_sameside.png) | ~47% |
| Dual Toolhead, With Interference Detection and Avoidance | ![](Diagrams/workspace_single.png) | **~100%** |

### Single Toolhead

Ditch one of the toolheads, and Dual Gantry reduces to a single CoreXY.  You can leave the inactive toolhead on and lose a corner of printable space, or you can remove the second toolhead to get nearly the full printable space.

If you mostly print in one color/material, this full travel is ... well, useful!  **Can’t do that with an IDEX.**

In a way, your daily driver for single-extrusion prints can also be the project car for the weekend (multi-material and multi-color).  But that’s not why we’re here, is it?

### Dual Toolhead, No Interference Detection

This mode works similarly to an IDEX, where a toolhead activation macro (typically `T0` or `T1`) parks the now-inactive toolhead, and motion then continues with the newly-active toolhead.  This method is simple to implement and RRF can already handle it, but firmware simplicity comes at the cost of printable space.

Options below assume that a V0-style carriage is used, which sets the homing direction.  Once homed, the toolheads can hang out on either side.

##### Option 1: Park in Opposite Corners

Use the front left area, possibly with a regular V0 bed.  You lose a toolhead's depth of X travel and a toolhead’s width of Y travel, yielding a nearly-square build area, in the front left or rear right.  For the prototype, ~170 x ~170 bed → ~125 x ~115 usable.

##### Option 2: Park in Back

Use the center area.  It’s just like an IDEX here; you lose twice the depth of a toolhead in the X direction, but retain full Y.  For the prototype, ~170 x ~170 bed → ~80 x ~170 usable.

##### Usable Workspace with Two Heads

For both options, to avoid collisions, the toolhead-park macro must move the head in the X first, then the Y, to the parking position, out of the way.  

That’s it.  

There’s no sophistication needed, beyond triggering a `T0` or `T1` macro to park a head.  But that space loss is a big deal at smaller sizes.

For a 140 x 120 travel Dueling Zero (300mm X extrusions, 200mm Y extrusions), with a 55 x 45 toolhead, parking in opposite corners:

    1.0 - (95.0 * 65) / (140 * 120) = 63% loss

Put another way - you're throwing away almost 2/3 of the available build space.  That's not acceptable.

For a 170 x 170 travel default Dueling Zero (330mm X, 250mm Y), with a 55 x 45 toolhead, parking at opposite corners:

    1.0 - (125.0 * 115) / (170 * 170) = ~50% loss

At bigger bed sizes, the loss is much smaller.  For example, for a port of Dueling Zero to a 350 x 350 printer, parking at opposite corners, with a 50 x 60 toolhead, the loss would be:

    1.0 - (290.0 * 300.0) / (350 * 350) = 29% loss

You can overcome the loss in all cases here by going with ~50mm wider X and Y extrusions and wider panels; you don’t even really need a bigger bed.  But that means a larger, heavier printer, with more air to heat up, longer belt runs, and potentially more challenges with tuning.  

For rear parking with the default Dueling Zero, we're looking at a similar, but slightly larger, loss:

    1.0 - (90.0 * 170.0) / (170 * 170) = ~53% loss

The loss is a bit higher vs parking at opposite-corners, because the dead zones don't overlap.

### Dual Toolhead, With Interference Detection and Avoidance

**Ahhh yes.  Where it gets interesting!  Read on.**

For every travel move, some code:
* slicer with geometry knowledge
* G-code post-processor with geometry knowledge
* firmware

... must detect toolhead interference and proactively avoid it to use the full workspace.

Consider any g-code move command (`G0`, `G1`, `G28`, etc.), then ask this question:

> Would one toolhead (a ~40 mm x 53 mm rectangle in XY, plus some clearance) intersect with the other toolhead's rectangle, at any point in the motion for that move command?  

There are four distinct cases of motion here, at least when the toolheads are small relative to the travel. An American football analogy will help us here:

![](Diagrams/cases_endzones.png)

The **"endzones"** are in the far X positions, on each side.  

An endzone begins where one toolhead would potentially collide with the other far-X-position toolhead.

We'll walk through the four distinct cases.

#### (1) No Avoidance Needed

An interference can only occur if the move goes to a far X edge - to the endzone.  If the move doesn’t start or enter either endzone, and the inactive extruder is parked in the endzone, then nothing smart is needed.

![](Diagrams/case1.png)

#### (2) Simple Avoidance

If a move enters the endzone and there's a detected collision - more precisely:

> “the bounds of the active toolhead’s travel intersect the inactive toolhead's bounds"

…then an active intervention, in the form of an **"endzone shuffle"**, is needed.  This will be our term for an inactive toolhead moving from the front to the back, or the back to the front, to get out of the way of the active toolhead.

![](Diagrams/case2.png)

Say the inactive extruder is in the way - in a corner - and is approached via an X move.  The inactive extruder must get out of the way, by doing an endzone shuffle.  To minimize print artifacts, a filament retract is needed here, followed by the original move.  This is the simple avoidance case:

* (1) shuffle inactive toolhead
* (2) do original move

Full-length endzone shuffles (corner-to-corner moves) are not required, or optimal, but are simpler to implement and explain.  Assume for the rest of the discussion here that all toolhead parking is in a corner.

#### (3) Backup-X Avoidance

Now, imagine that the active extruder is in the endzone, in a location where the inactive toolhead would smack into the active extruder during the shuffle, but the active toolhead is not overlapping the final location of the inactive one.

![](Diagrams/case3.png)

Here, the answer is to back the active toolhead out of the way first.  The sequence looks like this:

* (1) back up the active toolhead: move it out of the “endzone”
* (2) shuffle inactive toolhead
* (3) restore X position of active toolhead
* (4) do original move

The picture shows a bit more backup than absolutely needed, but you get the idea.

#### (4) Segmented Avoidance

If the inactive toolhead’s shuffle would cause it to overlap with the current active extruder’s position - when it’s in the corner of an endzone - we need to do something a little smarter.

Say the left toolhead is inactive in the rear left corner, and then the right toolhead continues on a counter-clockwise circle along the edge of the print area, getting to the front left.  The toolheads are now in opposite corners of the same endzone.

| There is no single move that works.  The two toolheads must switch positions, and the move must be split.

Time to do an "**endzone dance**"!

![](Diagrams/200.gif)

The dance looks like this:

![](Diagrams/case4.png)

The move command is split into two parts:
* The first part moves the active toolhead into a position where it will no longer interfere with the inactive extruder, post-shuffle.  
* The second part completes the original move from the partway point.  

The sequence looks like this:
* (1) do first part of the original move
* (2) back up the active toolhead: move it out of the “endzone”
* (3) flip inactive toolhead
* (4) restore X position of active toolhead
* (5) do second part of the original move

The first part of the move is necessary to ensure that the Y position of the active toolhead “just clears” the future position of the post-shuffle inactive toolhead.

Endzone dancing adds print time and the potential for print artifacts (from retractions), but it’s necessary to use the full travel.  When does it happen?

##### Worst-case for Segmented Avoidance

The worst case for motion is when **every** travel move triggers an endzone dance; for example, this condition occurs when printing an end of a square and when using a square-aligned infill direction (0 degrees or 90 degrees).

TBD: pics of motions matching this description

More generally, endzone dancing is needed for each outer perimeter of a full-size square.

> This is the downside of the Dual Gantry approach. It is what it is.

However, some straightforward techiques can help us avoid it.

TBD: Table summarizing techniques, with parts.

###### Rotate Long Parts

Don’t hang out in the endzone if it’s not necessary! Long, skinny parts can be reoriented to use the full Y height with park-in-the-back mode, or on a diagonal with the park-in-opposite-corners mode.

###### Rotate Infill

Rotate the infill direction to 45 degrees, so that the inactive extruder is only in the way twice for each square.

###### Use Fewer Perimeters

Avoid outer perimeters on large parts to avoid endzone dancing.  For example, go from 4 to 3 outer perimeters and increase the outer perimeter width to compensate.

###### Minimal Flips

Instead of doing a full-Y-travel move for each flip, what about minimizing the flip distance to only what’s necessary?

###### Simultaneous Motion

The inactive extruder could get out of the way, while the extruder is on the other side, to hide some of the time cost of the dancing.  

Simultaneous motion can be triggered with the two-Klipper control option, where each gantry is independently controlled.  Doing this with RepRapFirmware would require at least minor changes to the generated g-code to drive XY and UV (second-gantry) axes simultaneously.  Any implementation that assumes the use of `T0` and `T1` commands to share XY move commands between gantries cannot enable this.

###### Preemptive Positioning

The G-code processor could be smarter with positioning to avoid the need for retractions for interesting shapes, like a C-shaped part where one toolhead preemptively darts to the correct spot to get out of the way, or even just parks in the crook of the C shape and never moves.

### Duplication and Mirroring

A side benefit of Dual Gantry - like IDEX - is the option of simultaneous multi-part modes that split up the workspace.  Here, we assume that collision detection and avoidance enables full workspace access.

* Duplication Mode: like an IDEX, split the workspace in two:
  * Usable bed space: divide the bed in two.
    * 2x 85 x 170.

* Mirror mode: similar, but you leave space for the toolheads to never touch, so less space is usable.
  * Usable bed space: divide the bed in two and leave an interior gutter.
    * 2x 60 x 170.

However, you could get more flexibility to use the space with a slight bit of slicer awareness.  Imagine offsetting the start Y positions for two mirrored parts so that you get effectively higher overlap than a simple static partitioning (two circles, each larger than half the bed width or height).  You could print two half-bed-size triangles at the same time, for example.

Or, imagine having two streams of independent g-code, where the streams are sync’ed at Z moves.  

[Apparently this will be a thing for RRF for version 3.5](https://forum.duet3d.com/topic/29023/independent-dual-gantry-any-examples-out-there/3?_=1656291960523)!  As of 2022-07-16, this is in beta.

You can then print completely different parts at the same time.  How cool is that?  IDEX can never do that.

### Current Software Implementations

The software and firmware side will be an evolving space - to implement the optimizations described above, but also to reduce the complexity of configuration and tuning for new builds.

**Watch out for new stuff here.  Join in!**

At minimum, any Dual Gantry-capable firmware needs to control both gantries, but you also need *something* to ensure safety and insert moves with added G-codes.  

You’ll need to align the toolheads in XYZ too.  Z alignment can be done with a shared Tri-Zero nozzle endstop. XY alignment is the same process as with an IDEX, of either measuring with Vernier-style or other test prints or macros, or connecting up to a camera and using machine vision (TBD: add TAMV link).

Below are your software options.. at least, the ones that come from Zruncho with :heart:.

#### RepRapFirmware (RRF)

RRF has built-in support for CoreXYUV built-in, which makes it stupid simple here to at least get the axes in motion.  You select this printer type with a single G-code command, where you map the X, Y, U, and V axes to your printer control board’s stepper outputs.  Then you configure a homing macro to home all axes, and then you add macros to execute on each toolchange, specifically, to park the toolheads in opposing corners.

TBD: link to config within repo.

As long as the slicer spits out `T0` and `T1` commands, like for an IDEX, everything should then “just work”, for the `Dual Toolhead, No Avoidance Needed` case.

This was a big surprise!  

In fact, the main Duet/RRF developer, David Crocker, made it easy and general for all kinds of “linear axis combination” machines to flexibly use the same firmware.   See [this forum post](https://forum.duet3d.com/topic/22850/stacked-dual-markforged-kinematics-possible?_=1655971338993):

> "...after I implemented CoreXY, CoreXZ, Core XYU and CoreXYUV kinematics, I got fed up with having to add a new kinematics class every time someone wanted another variant of CoreXY. That is why RRF now has a universal linear kinematics class, which supports any kinematics for which the motion of every axis is a linear combination of the motion of each axis motor, up to the maximum number of axes supported."

That’s our setup.  

Nice going, David!  Impressive foresight.

RRF “just works” here.  There is a known-good configuration for a Duet 2 Wifi board in the Configs/ folder.   

NOTE: This config is gantry-only. You’ll need to add your Z and E config.

For the curious, here are the most relevant RepRapFirmware documentation pages:

* [Configuring RepRapFirmware for CoreXY Printer](https://docs.duet3d.com/en/User_manual/Machine_configuration/Configuration_coreXY)
* [M669]((https://docs.duet3d.com/User_manual/Reference/Gcodes#m669-set-kinematics-type-and-kinematics-parameters)): Set type to K8 (CoreXYUV)
* [M584](https://docs.duet3d.com/User_manual/Reference/Gcodes#m584-set-drive-mapping): Set drive mapping (add U & V axes)
* [M563](https://docs.duet3d.com/User_manual/Reference/Gcodes#m563-define-or-remove-a-tool): Define tools

**To be clear, this config does not handle the `Dual Toolhead, With Avoidance Needed` case.**

To support that case, you would need to make at least these changes:

* Change printer config type to not map XY and UV axes to XY (in the M669 command, change away from type K8, probably to K1 and with a custom movement matrix)
* Generate separate XY and UV commands in the G-code post-processor
* Replace `T0` and `T1` macros with G-code equivalents

#### Klipper

Klipper supports a massive ecosystem of control boards, sees new features added frequently (especially Input Shaper), and supports many toolhead boards that work well in a printer with tiny toolheads like Dueling Zero.

As of 2022-06-25, however, Klipper does not *directly* support a Dual Gantry printer.

##### Klipper-internal Dual Gantry Support: not yet

A direct, single-board-possible implementation of additional U and V axis support for CoreXY might look something like this:

    [printer]
    kinematics: dual_corexy
    ...
    [stepper_u]
    ...
    [stepper_v]
    ...
    [extruder]
    ...
    [extruder1]
    ...

That could be followed up with something to enable the no-avoidance case, similarly to the [[dual_carriage]](https://www.klipper3d.org/Config_Reference.html#dual_carriage) config option:

    [dual_gantry]
    gantry0_extruder: extruder
    gantry1_extruder: extruder1
    ...

Again, the above does exist... it's a suggested interface for users.

But such changes would require more familiarity with Klipper internals and development.  In the meantime, we have other options.

##### Single-board Test Config: yes, with caveats {#single-board-test-config-yes-with-caveats}

See `Configs/Klipper/single_board_test` for a single-board Klipper config for an SKR Pico that is useful for testing all endstops and gantries.   This enables a Single Toolhead starting point, for either toolhead.

One gantry config goes into each file {`left.cfg`, `right.cfg`} and only one can be enabled at a time.  You can uncomment/comment one file at a time, then restart Klipper, to check endstops and gantry motion, but you can’t use this config for actual two-gantry motion.  By the way, the gantry sides have the same axis extents, but have opposing endstop-position configs.

This file would hopefully provide a starter config for future single-board Klipper gantry control.  

* **Steppers:** wire up:
  * `X` to the rear left stepper
  * `Y` to the front left stepper
  * `Z` to the front right stepper
  * `E` to the rear right stepper
* **Endstops:** wire up:
  * the left-gantry `X` endstop to the `X` input
  * the left `Y` endstop to the `Y` input
  * the right `X` endstop to the `Z` input
  * the right `Y` endstop to the `E0` input.

This config only covers the gantry, intentionally.

##### Klipper-external Dual Gantry Support: yes, with caveats

An alternative is to use two gantries with two Klipper instances on two boards.

See `src/duel.py` for a provided Python program (duel.py) which implements this “externalized control” approach.   

TBD: Picture: one pi (outer rectangle), two Moonrakers on two ports, two Klippers, two boards, two config dirs, showing distinct moonraker ports and multi-printer Fluidd/Mainsal config.

Each Klipper instance has no idea about the existence of the other gantry! **They’re "ships in the night".**

The control program knows the position of each toolhead at all times.  It reads in a G-code file from a slicer and sends each command to the correct gantry, as well as manages switching between the two.  

For example, when `T0` is seen in the G-code stream, the other toolhead must be parked, and the control program emits the G-code for that.  Critically, this program implements `M400` calls to drain the move queue; it must wait for each move to complete before starting any other move that could put the two toolheads in danger of colliding.  Ask Zruncho how he knows about this…

Each G-code is triggered by doing a [POST to a Moonraker web server](https://moonraker.readthedocs.io/en/latest/web_api/#gcode-apis) in front of the gantry-specific Klipper instance.  The control program runs on a nearby laptop or on the controlling Pi.

The caveats here are numerous.  Honestly, this approach is just a hack to validate smart avoidance algorithms more easily, but it works.  Issues include:
* More Complex
    * You need two of everything.
    * Slightly higher memory load from two Klippers and Moonrakers and UIs.
    * The control program may not divert all G-codes properly, so watch out.
* Less Usable
    * Can’t initiate or check the progress of a print from the UI.
* Less Flexible
    * Static partitioning of steppers across boards is not ideal.
        * All Z steppers need to be on the same Klipper/Moonraker instance, so you may need more boards just to run 3 Z steppers from one place.
        * Individual G-code move commands can’t be perfectly split and synchronized between boards, so the extruder must be co-located with the corresponding XY steppers.
            * If using CAN, that means two CAN hats or dongles!  Sigh.  This is why the prototype has two separate CAN buses with one board each, vs one bus with two boards.
* Potentially lower-quality prints
    * REST calls add delay to every command, which might create larger part zits from toolhead flips.  On a home network over WiFi, this was in the 20-40ms range per command.  Should be lower with a co-resident duel.py.

`duel.py` uses a few Python modules to simplify the implementation:
* [gcodeparser](https://pypi.org/project/gcodeparser/): a simple parser to turn ASCII lines into modifiable python objects
* [requests](https://pypi.org/project/requests/): the usual Pythonic way to do clean REST interactions
* [cmd](https://docs.python.org/3/library/cmd.html): a simple way in Python to do interactive programs.  “Battle mode” is a little easter egg.
* [shapely](https://pypi.org/project/Shapely/): a geometry library
* [nose](https://pypi.org/project/nose/): test-running library

There’s some config needed to get this all running, but nothing too bad, and it’s noted in the Firmware Instructions section below.

#### Software Smart Avoidance

The control program (`duel.py`) needs to process G-code anyway, so it might as well also add the G-code commands needed for safe motion.   All 4 cases for interference are implemented.

The polygon intersect from Shapely enables interference detection.

That code looks like this, with a function `get_toolhead_bounds()` to get toolhead bounds as a shapely.geometry.Polygon instance:

```
    poly1 = get_toolhead_bounds(p1)
    poly2 = get_toolhead_bounds(p2)
    overlap = poly1.intersects(poly2)
```

One mildly interesting bit is the move split needed for the Segmented Avoidance case, which can be handled with basic y = mx + b math.  

Aside from these bits, the code is pretty straightforward... surprisingly so.

## Parts List

In general, none of the parts here should be a surprise.  

Yes, extrusions will get longer, X rails are longer and need two carriages, and you’ll need longer belts.  You’ll want longer Y rails if doing T0+.

In fact, it may be cheaper to just buy two V0 kits and supplement with a few parts.  You'll want:

* 2x [250mm MGN7H rails](https://www.aliexpress.com/item/2251832694486732.html?)
  * Make sure to also buy a ‘Carriage Only’ and message the seller to add it to the rail before they ship it.
* [2x 200mm MGN9C rails](https://www.aliexpress.com/item/2251832586981749.htm)
* 20mm set screws are recommended to double up extrusions, just like noted on the BoxZero GitHub.  

The bottom baseplate has a custom size, but all other panels are simple rectangles.

TBD: sample SCS order

#### Size: {Small, Stock, Larger}

You don’t have to build it at the default CAD size (~170 x ~170 travel), but that feels like a sweet spot.  Here's why:

* You *can* go smaller with the build - say 300mm fronts, 200mm sides, stock V0 bed - but the toolhead overlap will make the need for endzone dances higher, when printing on the full area.
* Subjectively, the stock larger CAD size feels reasonably rigid, even without rigid panels adding any stiffness.  
  * The BoxZero corners add a noticeable amount of stiffness, and the multiple attachment points on the gantry shorten the effective span length of the vertical extrusions.
  * A single rigidly-mounted rear panel should do wonders here, too.
* Anything larger than the default size may need added rigidity.  Maybe you could do a 200x200 bed with 1515… but at that point, 2020 extrusions should be a consideration.  
  * On the plus side, Tiny-M provides a roadmap to doing such a 2020 conversion, and when combined with a Tri-Zero port like Ankurv’s one… the work might not be too bad.

For the stock size, you can use the extrusions in a V0 kit, supplemented with:

* 10x 50mm extrusion chunks in the Y dir: most are for the sides and gantry crossbars; plus, one for the bedframe and one for the strut
* 5x 300mm extrusions in the rear: 4 for the box plus for the bedframe crossbar
* 6x 200mm extrusions on the base sides as well as rear verticals
* 1x 100mm extrusion for the bedframe

As a bonus, most holes in the V0 kit can be reused, if you put the right parts in the right places, in advance: mostly for verticals, which need blinds joints all around.

This pic doesn’t show the 50mm chunks accurately, but the rest is accurate.  Add flashes of color where you want, and make it your own.

TBD: Add frame pic

You can buy 200s and join them to 100s to save a little money too.  

I keep one 100mm extrusion as a souvenir from each V0, but also to test sliders, which need to be matched to the particular extrusion type, and even batch.  Running out of colors from all the V0 builds...

TBD: pic of "souvenir extrusions"

#### Triple-Z vs Single-Z

You can actually do a single-Z-motor build if you want, and then the whole shebang can use 7 drivers and a single board.  This option isn’t shown in CAD, but should work with stock V0 parts, or maybe minor changes.

If you’re not a fan of cantilevers (Zruncho's hand just raised, too...), and you want a more scalable printer (especially to the T0+50mm size), Tri-Zero is a good option, at the small cost of adding 2 extra Z stepper drivers, motors, and a few other motions parts.  It also has a nozzle endstop by default, which enables automatic, or at least measurement-supported, Z offset calibration.  This alone is a reason to use Tri-Zero, given the importance of the first layer in 3D printing.

#### Control Boards

The control board situation is up to you, but make sure to consider the need to split the gantries across two boards with the current Klipper option (see note above in Klipper section).  In theory, any boards should be fine, as long as you get enough steppers.

CAN toolhead boards are highly recommended, as they reduce your wiring, and enable the use of stock 8-driver boards.  But remember, until Klipper supports two gantries on one instance, you’ll need at least two CAN-bus boards. :thumbsdown:

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

It’s a cake with layers.  The layers can be done independently, then joined.  You don’t even need to follow this order, but it’s known to work.  In all steps, make sure to add more NDNs that you think might need!  You’ll need a lot, especially as all corners add 4-6 NDs.  

In all steps, get screws finger tight, but wait until the printer includes all parts to fully tighten all (accessible) screws.

TBD: pic of layers, before and after

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

## Links

### Dual Gantry

Others have built printers or similar CNC devices with at least two gantries operating in a single shared workspace.  Here are some real ones:

* Cronus - a 5-head, single-workspace 3d printer
    * [https://www.youtube.com/watch?v=TkEOMQ6rQ6s](https://www.youtube.com/watch?v=TkEOMQ6rQ6s)
* Other dual gantry example in CNC:
    * [Dual Gantry CNC Machining Centers](https://www.cronsrud.com/cro-dual-gantry.html)

TBD: many, many more links.

## FAQ

### What’s the cost?

Probably $250+ minimum beyond a stock V0, depending on the parts you already have, with costs similar to a Double Dragon.  The second toolhead dominates the cost (hotend, extruder motor, toolhead board, fans, …), with the extra gantry adding the cost of 2 motors, bearings, rails, and new belts.  And you’ll need some new panels for the necessary widening.  Plus, you’ll need to have the extra drivers and a potentially larger power supply.

The Tri-Zero mod (if included in the build) adds cost too, as you’ll need the 3 Z motors, belts, extra extrusions, and longer rails.  And a new bed.

### How much XY travel do I get?

There’s an aspirational goal to use as much of the 170x170 motion for the 180x180 bed as possible, using the corner-cube-extended 300mm front/rear horizontals and 250mm side horizontals.

Final numbers are TBD, but should come close to this goal: the target is travel motion of 168 in X, and 170 in Y.  The target is 165mm usable Y, with the loss in the rear, for the shared nozzle endstop and ZeroClick keep-out region.

### Can I port this to a V2-style gantry?

Good question!

Part of what makes the design possible is that the Y rails on a V0-style gantry face inwards, vs upwards or downwards.  This makes them suitable for a symmetric design that places one gantry above and one below.  

For a V2/Trident-style gantry, you’d have to modify the XY joints to support 4 stacked belts, which might become an issue as those belts get farther away from the carriages and as that higher distance creates higher torques on the carriages.  Or, you’d need to use 4 total single-carriage rails and align them carefully, which seems a bit risky.

### Why not just do an IDEX?

**Answering as a user**: because single-extruder prints can be faster and better without a second toolhead to drag around, and there are some unique capabilities (simultaneous different prints, full-workspace single prints) that you get.

**Answering as a printer-designer**: it’s a unique and interesting challenge to fit all the belts and toolheads into one gantry, especially in a way that reuses much of what’s out there.  

**Answering as a coder**: there are some interesting - but still reasonable - 2D object interference and path-planning challenges, as well as firmware changes to make this all work.  Plus, there are lots of optimizations to implement and then evaluate.

## Support?

Post to the Reddit thread; if this gains more traction, then it should probably be its own channel in DoomCube.