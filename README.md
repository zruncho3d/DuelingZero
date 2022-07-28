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

"Real thing" pics coming soon - with wiring, enclosure, fully-built toolheads, etc.

## Release History

### 2022-07-X: Alpha-1  
This first release covers everything you need to build and run your own Dueling Zero: CAD, STLs, DXFs, sample firmware configs, smart avoidance code, G-code streaming code, instructions, and a parts list... everything but an illustrated manual.  But if you're reading this, you almost certainly don't need a manual, anyway.

To make it easy for anyone to grok this crazy Dual Gantry layout - and learn about its opportunities and challenges, both in hardware and software - this README walks through the software and the design.

Enjoy!  There's a lot of content here, and I hope you enjoy it as much as I did bringing this concept to life.  -Z.

Join the [Reddit thread (TBD)]() on `r/VoronDesign` for any comments, questions, or kudos.

## Table of Contents

There's a ton of detailed content in this repo, beyond this README.

- #### [Overview](#overview)
- #### [Software](SOFTWARE.md): Two toolheads in one workspace, explained
- #### [Parts](PARTS.md): Parts list to build your own
- #### [Instructions](INSTRUCTIONS.md): Instructions to print, assemble, and configure
- #### [Design](DESIGN.md): Get inside the designer's head.  Mostly renders!  An easy read
- #### [FAQ](FAQ.md): Common questions, answered

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

You can mitigate the moving mass somewhat, by using a lighter toolhead, typically with a remote Bowden extruder, but Bowden extruders introduce their own tuning challenges.

**With Dual Gantry, you get a no-mass-added, no-downsides gantry for the common case of single-extruder prints.**

There’s no hit to max acceleration or any potential ringing issues from dragging around a heavy second toolhead on a longer rail all the time, like on an IDEX.

This motion concept fits within a broader space of 3D printer types that support multiple extrusion, where the number of toolheads, hotends, and extruders vary:

![alt_text](Diagrams/landscape_of_multiple_extruders.png)

Take a look.  This diagram is not comprehensive, but gives a sense for the depth of the design space, and especially, the rarity of everything not on the far left side (typical single-extruder printer).  For some points in the design space, there's only one commercial example!  

Please file an issue if you know of any significant omissions.

### What’s the catch?

If it sounds too good to be true... it probably is.

You don't have to design it (anymore), but you still need to build it, which is roughly twice the work of a typical printer.  Compared to the usual single-extrusion, single-toolhead 3D printer, there are added cost, complexity, and alignment challenges.  Many are identical to IDEX.

**But the main reason you’ve probably never seen a Dual Gantry 3D printer: firmware support.**

RepRapFirmware *does* support two active gantries using one control board.

Klipper doesn’t, *yet*, but there’s a workaround.

**Regardless,** neither firmware implements the smart avoidance necessary for safe motion within the full area of bed travel.

This is not a blocker anymore, though!

The code in this repo enables a functioning printer with full bed-travel usage.  See the [Software](SOFTWARE.md) section for a full explanation, with diagrams, pics, and explanations.

### How does this mod work?

Start with a trusted, tested Voron Zero CoreXY gantry.   

Copy and paste, then rotate and move it with a touchpad gesture, so that the two share the same rails.

Flip the XY joints upside down.  Voila!   

![alt_text](Renders/gantry_iso.png)

That’s the core idea.

In practice, though, there are quite a few additional bits to design to make it work.  And like with any V0 mod, the devil is in the packaging details: *every mm matters*.

Each gantry is heavily customized vs a regular V0, to make an underslung low-side gantry (left, in black) as well as an underslung high-side gantry (right, in silver). Beyond these new gantry XY joints, there’s some extra work to relocate the endstops and add a high-side strut; *something* needs to directly resist the forces of the tensioned belt.  Oh, and the belts can't pass through a motor on the high side, so you have to figure that one out, too.

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
* Filament: mix of KVP ABS flavors: Metallic Silver, Black, and Stellar Black.

Two control options have been tested:
* Control Option 1: RepRepFirmware with Duet
    * Duet2 Wifi + Duex5
    * 2x Pancake V0 toolhead boards
    * 5” PanelDue
* Control Option 2: Klipper "Two Ships in the Night" setup
    * Raspberry Pi Zero 2 W
    * 3x SKR Pico controller boards
    * 2x EBB42 toolhead boards
    * Waveshare CAN hat
    * BTT U2C USB CAN board
    * Mini 12864 display with [Klipper adapter](https://www.aliexpress.com/item/3256802553287831.html)

Flexibility, or fear of commitment… you decide!

### Learn more!

If you've read this far, great, but you haven't gotten to the good stuff.

There's 10x the info beyond this README file, in the repo, split into multiple pages.

Take a look around, or up at the Table of Contents above.

## Links

### Dual Gantry

Others have built printers or similar CNC devices with at least two gantries operating in a single shared workspace.  Here are some real ones:

* [Cronus](https://www.youtube.com/watch?v=TkEOMQ6rQ6s](https://www.youtube.com/watch?v=TkEOMQ6rQ6s) - a 5-head, single-workspace 3d printer
* [Dual Gantry CNC Machining Centers](https://www.cronsrud.com/cro-dual-gantry.html)

TBD: many, many more links.

## Support?

Post to the Reddit thread; if this gains more traction, then it should probably be its own channel in DoomCube.