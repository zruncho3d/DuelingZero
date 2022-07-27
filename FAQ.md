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

### Is it still a Voron Zero?

**Z says yes.**

The only printed parts this printer shares with a regular Voron Zero:
* 9mm spacers
* Pi mount

Yes, that's it.  So why is it still a Voron Zero?  

Because it wouldn't exist without the V0.  

Because many parts are modifications of existing V0 parts.

Because nearly every non-printed part, including the frame, is a stock V0 part.

So there you go... a V0 in spirit, if not in printed parts.

### Seems like a lotta work for a little printer, right?

Well, yes.

But it'd be even more work for a larger printer.
* It'd be impossible to rotate in your lap as you build it.
* It'd be impossible to reuse your V0 frame kit.
* It'd be impossible to store your test build in a file-folder box.

You wouldn't learn anything more.  A bigger printer would take longer to get up to temperature.  It would  have longer, harder-to-tune belts and potentially worse print quality.  It could cost more and require more energy to run.

If you don't routinely print larger objects, and especially if you do
lots of one-off small part-prototyping prints, you'll find that tiny printers rock.  Check out [3D Printers for Ants](https://3dprintersforants.com) for more examples like this one!
