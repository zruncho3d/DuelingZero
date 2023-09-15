## Dueling Zero - a Dual Gantry V0 mod

**Two extruders.  No compromises.**

Enable dual-color, dual-material, and dual-part printing... with the same speed and quality as single-extruder printing.

Mod a [Voron Zero](https://vorondesign.com/voron0.2) or build one fresh!

**D0** is the only open-source, fully-documented, reproducible-by-anyone Dual Gantry printer out there.

| ![alt_text](Renders/Printer/top-3.png) | ![alt_text](Renders/Printer/iso-perspective.png) | ![](Images/v3/cat_small.jpg)
| - | - | - |

Curious?  Watch it print below!

# [> > > Watch Video from first prints](https://youtu.be/2YI3_g30EwA)

[![alt_text](Images/first_print_thumbnail.png)](https://youtu.be/2YI3_g30EwA)
(original v1 gantry shown)

## Release History

**2023-09-16 v3 Gantry release and updates**

This release moves to a completely-new, symmetric, nested belt path:

| ![alt_text](Renders/Gantry/belts_detail.png) | ![alt_text](Renders/Gantry/belts_detail_iso.png) | ![alt_text](Renders/Gantry/belts_colorized.png) |
| - | - | - |

This new [Pandora's Box](https://github.com/MasturMynd/Pandoras_Box/tree/main)-derived gantry design, created in close collaboration with `Desune` on Discord, has far fewer unique parts (for better portability to other sizes) and adds travel.

| ![alt_text](Renders/Gantry/latest_over_the_top_blur_40_022.png) | ![alt_text](Renders/Gantry/bottom_with_wires.png) | ![alt_text](Renders/Gantry/top_with_wires.png) |
| - | - | - |

Here's the side-by-side comparison from above, with v1 on left, and new v3 on right:

| ![alt_text](Archived_v1/Renders/top-2.png) | ![alt_text](Renders/Printer/top-3.png) |
| - | - |

Or, in reality:

| ![alt_text](Images/v3/v1_iso.jpg) | ![alt_text](Images/v3/v3_iso.jpg) |
| - | - |

The printer looks a little different now, with internal spool holders!

| ![alt_text](Renders/Printer/iso-perspective.png) | ![alt_text](Renders/Printer/front-ortho.png) | ![alt_text](Renders/Printer/side-ortho.png) |
| - | - | - |

In short - **this is a big update**.  *This is what D0 should have always been.*

Sometimes it's only through iteration and collaboration that you get to what feels right.  **The v3 gantry feels right**.  

No weird strut, no flipped motors, smaller, more maintainable... all-around, better.

The gantry improvements are summarized below:

![](Diagrams/comparison.png)

Other major improvements to call out:

* **Boop support by default**: for perfect first layers every time, nozzle probing with [Boop](https://github.com/PrintersForAnts/Boop) is now the default.  There are no magnets to get loose in a heated chamber and no probe motions to configure anymore.
* **Voron 0.2-compatible toolheads now fit**, including the Voron Mini Stealthburner toolhead, shown in these renders.
* **Gantry board support** for the [GBB15 gantry board](https://github.com/skuep/GBB15) - enables super-clean, easy wiring with magnetic-attach covers
* **Dual internal spool holders** added

**Existing v1 builders**: to upgrade, the main costs will be new rails, a few new extrusions, and Boop parts.  There's nothing wrong with such a build.  If you're partway there and want to make the transition, Zruncho recommends finishing just the low-side V1 gantry and getting everything operational, then using that printer to print all parts for a single-toolhead v3 gantry, testing it outside of the printer, and then transitioning to it once the new gantry is validated (in a day). If you want full bed over-travel, though, a fresh rebuild with the larger frame makes sense.

For previous updates, see the [Updates](updates.md) page.

## Table of Contents

There's a ton of detailed content in this repo, beyond this README.

- #### [Overview](#overview): Why Dual Gantry?
- #### [Updates](UPDATES.md): Major Release Updates
- #### [Software](SOFTWARE.md): Two toolheads in one workspace, explained
- #### [Parts](PARTS.md): Parts list to build your own
- #### [Instructions](INSTRUCTIONS.md): Instructions to print, assemble, and configure
- #### [FAQ](FAQ.md): Common questions, answered
- #### [Archived v1](Archived-v1/REAMDE-v1.md): Prior design

## Sample Builds

Let's be honest here... there's no such thing as a completely "stock" D0 build.  If you can build this, you're going to pick the best parts for you, and the beauty of living within the V0/T0/Boop ecoystem - more than ever with the v3 gantry - is that you *get* this choice.

Two sample builds below should get you thinking.  Make sure to check out `Hex-Zero` mod by Alexander Þór and HBO's [T0 mods repo](https://github.com/harry-boe/tri-zero/tree/main/Mods/hbo) for alternate skirts and the Z joints, in particular, as well as Desune's [Dueling Boops](https://github.com/desune2487/Dueling_Boops) repo for alternate skirts and gantry parts, as well as skim through `#dueling-zero-dev` on DoomCube for the latest.

### Zruncho's Red/Black Build

Originally [V0.562](https://www.reddit.com/r/voroncorexy/comments/odfid1/voron_00_serial_request_zruncho1790/), then the first Dueling Zero, and now with the v3 gantry:

| ![alt_text](Images/v3/box_o_parts.jpg) | ![alt_text](Images/v3/top.jpg) | ![](Images/v3/archetype_parts.jpg) |
| - | - | - |

Highlights of this particular build:
* XY Motion and Toolhead
  * 2x [Boop beta-4](https://github.com/PrintersForAnts/Boop/tree/main/beta_4)-based carriages with nozzle bed probing, plus rear threads for toolhead boards, using the same sensor option as Tap
  * 2x [MiniSB](https://github.com/VoronDesign/Voron-0/tree/Voron0.2r1/STLs/Toolheads/Mini_Stealthburner) toolheads
  * 2x [Revo Voron](https://e3d-online.com/products/revo-voron) hotends - V0.2r1 version
  * 4x StepperOnline Nema 14 (14HS20-1504S) stepper motors
* Frame and Z
  * Rail-less Z motion (!) using printed Tri-Zero MGN7-compatible sliders with match fit to extrusions
  * [Tri-Zero](https://github.com/zruncho3d/tri-zero) triple-belted Z with tool-less belt attachments
  * 3x Kysan 1124090 NEMA17 motors for Z
  * LDO 1515 V0 frame kit (Red) + MakerBeamXL 1515 (Black) w/500mm pieces cut to size
  * 300W AC 180x180 [Prusa Mini size plate bed](https://www.aliexpress.com/item/3256803530287164.html) with textured and smooth PEI sheets
* Electronics
  * Raspberry Pi 3B
  * SKR Pico controller boards for Z motion
  * 2x [GBB15](https://github.com/skuep/GBB15) gantry boards
  * 2x EBB42 toolhead boards
  * BTT U2C USB CAN board
  * Meanwell LRS-150-24 PSU
  * Mini 12864 display with [Klipper adapter](https://www.aliexpress.com/item/3256802553287831.html)
  * 2x Fysetc PIS USB ADXL boards mounted to x carriages
* Other
  * Panels: [ZeroPanels v3](https://github.com/zruncho3d/ZeroPanels) with optional midclips and rear-hinged top panel
  * Travel: 166mm x 180mm in XY, ~130mm in Z (not optimized!)
  * Filament: mix of KVP ABS flavors: Metallic Silver, Black, and Stellar Black.
  * [PrinterExperiments](https://github.com/zruncho3d/printer-experiments) code for easy Z nozzle alignment with a single command

This build is a bit too small to cover the full bed and support over-travel in all directions. For all new builds, a build the size of Desune's is recommended; more in the [Parts](PARTS.md) section.

### Desune's Silver Build

Highlights of this particular build:

* XY Motion and Toolheads
  * 2x Boop beta4 with OptoTap v2.4.1 board (slightly modified for rear microswitch mounting)
  * 2x Dragon Burner v7 (modified for Boop clearance)
  * 2x Rapido v2 HF
  * 2x Orbiter v2 extruders with filament sensors
  * 2x MGN7H 300mm
  * 2x MGN9H 250mm
  * 4x StepperOnline Nema 14 (14HS20-1504S) stepper motors
  * 3x Cloudray Nema 17 (17CS04A) stepper motors
* Frame and Z
  * Misumi 1515 extrusions (silver)
  * Rail-less Z motion sliders (modified to fit Misumi extrusions)
  * Triple-belted Z with custom Pandora'sBox-derived GE5C joints
  * 180x180 bed with 300W AC powered heater
* Electronics
  * BTT Manta M8P v1.1 with CB1 v2.2 compute module
  * 2x BTT EBB36 v1.2 toolhead boards
  * 7x BTT TMC2209 stepper drivers
  * BTT TFT35 SPI v2.1 touchscreen
  * Meanwell UHP-200 PSU
  * CG 40A DA SSR
* Other
  * ZeroPanels clips (modified for screw mount on Misumi extrusions)
  * Filament - eSUN ABS silver and black
  * Removable base panel for easy electronics access.
  * Outer Dimensions (without enclosure panels):  L: 290  W:380  H:526mm   Height includes electronics compartment and feet.  Vertical extrusions are currently 450mm, however 50~100mm of extra height for umbilical clearance is recommended for maximum Z travel.
  * Maximum XY travel (approximate):  X:188mm  Y:194mm  (with Dragon Burner toolhead)
  * Maximum Z travel (as configured with 200mm linear rails): 168mm

The parts for this specific build are available at Desune's [Dueling Boops](https://github.com/desune2487/Dueling_Boops) repo.  They are extremely similar to Zruncho's parallel implementation; the two influenced each other during development.  Definitely take a look, as you can mix and match parts from this one, including the updated skirts and bed pieces.

## Overview

### What’s a Dual Gantry printer?

**Dual Gantry** is a rare 3D printer type with two toolheads moved by **two** *completely independent* XY motion systems:

 ![alt_text](Renders/Printer/top-3.png)

Yes, you’re seeing double, with black and silver toolheads in a dual-CoreXY motion configuration.

### Why a Dual Gantry printer?

In general, a second hotend adds enormous flexibility - to support two colors, two materials (typically support + main), and two nozzle sizes, in one print, with no color-bleed issues, cross-contamination, or wasteful purging.  Sounds good, right!

Well, that second hotend, if mounted on a single toolhead, can get in the way of print quality, as it drools filament when not in use - and the toolhead is now custom. :frowning:

So along comes IDEX, short for Independent Dual Extrusion, which adds a second, independent toolhead on a shared axis (typically the X axis).  Sounds better, right?

No drool, plus something cooler: one printer can now print two identical parts simultaneously, in mirror or duplicate modes. :muscle:  (note: in theory; depends on firmware support)

Open-source IDEX designs include [Voron](https://vorondesign.com/)-derived ones, like [Zruncho](https://github.com/zruncho3d)’s [Double Dragon](https://github.com/zruncho3d/double-dragon), [Eddietheengineer](https://www.youtube.com/eddietheengineer)'s [Tridex](https://github.com/FrankenVoron/Tridex/), and [Ankurv](https://github.com/ankurv2k6)’s [IDEX Switchwire](https://github.com/ankurv2k6/voron_idex_switchwire).  There's also the [Muldex](https://github.com/3dprintingworld/MULDEX), and there's no shortage of commercial examples, too: [Sovol SV04](https://sovol3d.com/products/sv04), [FlashForge Creator Pro](https://www.flashforge.com/product-detail/flashforge-creator-pro-2-3d-printer), [BCN Sigma](https://www.bcn3d.com/bcn3d-sigma-d25/), [Jadelabo J1](https://www.jadelabo.com/), and many more.

But that second toolhead comes at a cost: moving mass, which has effects on print speed (max accel) and quality (typically, ringing artifacts).  :neutral_face:

> Simplify, then add lightness - [famous quote from Colin Chapman at Lotus](http://www.lotuscars.com.tr/about-us/lotus-philosophy/index-31332.html#:~:text=At%20the%20root%20of%20our,was%20another%20of%20Chapman's%20premises.)

Whether building a fast race car or a fast printer, physics can't be ignored.  

You can mitigate the moving mass somewhat, by using a lighter toolhead, typically with a remote Bowden extruder, but Bowden extruders introduce their own tuning challenges.

**With Dual Gantry, you get a no-mass-added gantry for the common case of single-extruder prints.**  Unlike an IDEX, here, each toolhead is *truly independent* and can move in X *and* Y on its own - [potentially to print two completely different objects at once!](https://forum.duet3d.com/topic/27895/beta-testers-for-multiple-motion-system-support)

There’s no hit to max acceleration or potential for ringing caused by dragging around a heavy second toolhead on a longer rail all the time.

Sure, you can't print more than two colors, like a multi-material unit or toolchanger can, but everything in engineering is tradeoffs.  [As Nero says](https://youtube.com/clip/UgkxAxd22dVnUN7P749WHRpp-yFLg3WqvwTv):

> Multimaterial... sucks.  OK?  There’s no way to do it right.  So either you spend money, time, or waste.  No matter what you do, you're gonna be dealing with that.

Dual Gantry is in an interesting point in a larger space.  **Medium money, medium time, minimal waste**.  It fits within a broader space of 3D printer types that support multiple-extrusion, where the number of toolheads, hotends, and extruders varies:

![alt_text](Diagrams/landscape_of_multiple_extruders.png)

Take a look here, or at [this other helpful categorization](https://gist.github.com/kmcallister/6636d88802ba00432c65d14e9431c0e6).  This diagram is not comprehensive, but gives a sense for the depth of the design space, and especially, the rarity of everything not on the far left side (typical single-extruder printer).  For some interesting points in the design space, there's only one commercial example!  

(Please file an issue on GitHub if you know of any significant omissions.)

### What’s the catch?

If it sounds too good to be true... it probably is.  :shrug:

You don't have to design it (anymore), but you still need to build it, which is roughly twice the work of a typical printer.  Plus, compared to a typical single-extrusion, single-toolhead 3D printer, there are added cost, complexity, and alignment challenges.

**The main reason you probably have never seen a Dual Gantry 3D printer: firmware support.**

Support for two gantries with one control board is a good start:
* RepRapFirmware: supports two active gantries, out-of-the-box.
* Klipper: thanks to a collaboration with [tircown](https://github.com/tircown), there's a PR available now.
* Marlin: no.

To get full motion out of a shared-workspace printer, however, you really want active collision detection and avoidance.  

See the [Software](SOFTWARE.md) section for a full explanation, with diagrams, pics, and explanations, as well as code that implements collision detection and avoidance.

### How does this mod work?

Start with a Pandora's Box gantry.  Turn it 90 degrees.  Modify it to add extra bearing stacks and combine idlers with AB blocks.  Duplicate it about the center.

Then when mounting, flip it upside-down.  

Add off-the-shelf Boop and v0.2-compatible toolheads.

![alt_text](Renders/Gantry/iso_with_final_wires.png)

That’s the core idea.

In practice, though, there are quite a few additional bits to design to make it work.  And like with any V0 mod, the devil is in the packaging details: *every mm matters*.

For the rest of the printer, D0 heavily leverages off-the-shelf parts from these repos:
* [BoxZero](https://github.com/zruncho3d/BoxZero) ditches the V0 tophat
* [TriZero](https://github.com/zruncho3d/tri-zero) adds automatic bed leveling and enables XY scalability
* [ZeroPanels](https://github.com/zruncho3d/ZeroPanels) add snap-in panels
* [Boop](https://github.com/PrintersForAnts/Boop) adds highly accurate nozzle probing
* [Voron V0.2](https://vorondesign.com/voron0.2) provides a good toolhead default

If you're not familiar with these mods, here's a pic, showing a Plus50-size Tri-Zero + BoxZero printer (170x170 bed motion), next to a V0-size (120x120 bed motion) Tri-Zero + BoxZero.  Both have ZeroPanels.

![](Archived_v1/Renders/iso-both.png)

### Learn more!

If you've read this far, great, but there's more good stuff.

There's lots more info beyond this README file, in the repo, split into multiple pages.  And the [V1 Archives](Archived_v1/) section provides a view into the original design that you might find interesting.

Take a look around, or up at the Table of Contents above.

## Links

### Dual Gantry

They do exist.  Others have built printers or similar CNC devices with at least two gantries operating in a single shared workspace:

* [Essentium HSE 280i](https://www.essentium.com/3d-printers/high-speed-extrusion-280/): large, high-dollar, linear-servo printer with two gantries
* [Cronus](https://www.youtube.com/watch?v=TkEOMQ6rQ6s): a 5-head, single-workspace 3d printer
* [Dual Gantry CNC Machining Centers](https://www.cronsrud.com/cro-dual-gantry.html): a related CNC
* [Earlier motion platform example](https://www.youtube.com/watch?v=S_7VCEe3hOk): dates to 2012!

There are also a bunch of posts online with people conceptualizing the concept, dating back years.  The benefits/drawbacks are relatively straightforward to understand, though not widely known.  For a few builds, there are mentions online, but no reference to a video of the machine printing, or a link to learn more.

* 2018-06-04 [Duet Forum post by 3D_low](https://forum.duet3d.com/topic/5561/did-anyone-make-a-idex-with-dual-x-gantry-bar): "Did anyone pull that off yet? i havent found one on the net."
* 2018-11-21 [Duet Forum post by Haggan90](https://forum.duet3d.com/topic/7796/haq-xy/122): HaqXY is a dual Hybrid-CoreXY
* 2021-03-01 [r/3Dprinting post by u/m47812](https://www.reddit.com/r/3Dprinting/comments/lv8ksv/developed_a_new_kind_of_dual_extruder_system_on/): "CODEX" project.  Video shows a fairly far-along dual-gantry; describes collaborative mode too.  Abandoned as of 2023 in favor of a toolchanger.
* 2021-05-01 [r/Reprap post by u/lowfat](https://www.reddit.com/r/Reprap/comments/n2tkvb/corexy_with_dual_fully_independent_gantries/): postulates DG, but abandoned in favor of a toolchanger
* 2021-07-21 [Duet Forum post by breed](https://forum.duet3d.com/topic/24258/independant-dual-gantry-corexy/10?_=1657058082320): "Independent Dual Gantry CoreXY"
* 2021-09-17 [Duet Forum post by oliof](https://forum.duet3d.com/topic/25158/core-xy-idex-with-two-gantries/15): "Core XY - Idex with two gantries", has a nice diagram
* 2022-01-27 [Klipper Discourse post](https://klipper.discourse.group/t/dual-gantry-printer-with-single-mcu-btt-gtr-btt-m5/1900): Dual gantry printer with single MCU
* 2022-03-25 [Duet Forum post by dc42](https://forum.duet3d.com/topic/27895/beta-testers-for-multiple-motion-system-support/41): Beta testers for multiple motion system support: simultaneous multi-printing for RRF v3.5.  Note two pictures, for motion designs from breed and slaughter2k
* 2022-06-23 [Duet Forum post by zruncho](https://forum.duet3d.com/topic/29023/independent-dual-gantry-any-examples-out-there/10): is anything out there?

Please raise an issue for this repo to update the list of links if you come across one!  There’s no pretense of true originality here.

### Related

* [Bill Deckingham’s beast](https://www.youtube.com/watch?t=488&v=O_whcaAJpfs&feature=youtu.be): a CoreXYUVAB system, with extra axes for a very different reason.  Maybe some software lessons or relevant RRF config here?
* [Hashprinter](https://forum.duet3d.com/topic/24287/hash-printer-with-super-simple-gantry/2): super simple gantry
* TAMV = Tool Alignment with Machine Vision: a way to automate XY calibration
  * [Jubilee Toolchanger page](https://jubilee3d.com/index.php?title=TAMV)
  * [HaythamB fork](https://github.com/HaythamB/TAMV)
  * [TAMV on Klipper](https://github.com/TypQxQ/TAMV)
* [Klipper PR by Tircown that adds duplication and mirror modes](https://github.com/Klipper3d/klipper/pull/4464)
* [PitStop3](https://mihaidesigns.com/pages/pitstop-3-multi-material-3d-printer): hotend-swapping multi-material printer
* [Swapper3D](https://www.kickstarter.com/projects/bigbrain3d/swapper3d): nozzle-swapping multi-material printer
* [Enraged Rabbit Project](https://github.com/EtteGit/EnragedRabbitProject): add multimaterial capability
* [3D Chamaleon](https://www.3dchameleon.com/): automatic color changer

## Credits

* **Desune**: designed Dueling Boops (the honorary v2 gantry) and co-designed the v3 gantry w/Zruncho.
* **MasturMynd**: designed Pandora, which made this possible.
* **Tircown**: made a single-Klipper-instance version possible, with his code and live debugging
* **Clee**: saved the project with some hardcore hardware rescue with the STM GB01 chips
* **ToxGunn**: diagnosed a stepper overcurrent issue and saved me more plastic and motors
* **Reviewers (for v1): Red5, _xbst, where’sthelambSAUCE, BeastBc**: thanks for providing feedback that helped make this clear and concise.
* **Clee, Red5, Kyrios, Leopard, EddieTheEngineer, and others**: initial conversations proved motivating - that this wasn’t completely insane.  Thanks!
* **Nemgrea**: none of this would have happened without a solid base.

## Support

The best place to ask questions and see the latest is on the DoomCube Discord, where many Printers For Ants builders hang out.  Go to the `#dueling-zero-dev` thread in the #tri-zero channel.  Put your build log in the `#build_logs` showcase forum there too!

