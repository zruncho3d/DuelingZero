## FAQ

### Is it still a Voron Zero?

With the v1 gantry, the answer was "Hell no":

The only printed parts shared with a regular Voron Zero were:
* 9mm spacers
* Pi mount

With the v3 gantry, the answer is "Somewhat".

The only printed parts this printer shares with a regular Voron Zero are:
* MiniSB toolhed
* Pi mount

But really...

**Hell yes!**

Because it wouldn't exist without the V0.  

Because many non-printed parts, including the frame, rails, and motors are identical, or at least similar.

So there you go... a V0 in DNA, if not in printed parts.

### Is it fun to build?

Hell no...  “Get one V0 for the pain/time/cost of two!”

**Hell yes.**  Learn a ton and get a unique and extremely rare printer type.

### Should I make one?

Hell no... "I only build printers from complete manuals."

**Hell yes!**

Everything you need is documented here in this repo.

And if you’re gonna make a printer, you might as well make it interesting.

You can even build just the left half first, then build, wire, and connect up the second gantry at your leisure.

### What’s the cost?

Probably $300+ minimum beyond a stock V0, depending on the parts you already have, with costs similar to a Double Dragon.  The second toolhead dominates the cost (hotend, extruder motor, toolhead board, fans, …), with the extra gantry adding the cost of 2 motors, bearings, rails, and new belts.  And you’ll need some new panels for the necessary widening.  Plus, you’ll need to have the extra drivers and a potentially larger power supply.

The Tri-Zero mod (if included in the build) adds cost too, as you’ll need the 3 Z motors, belts, extra extrusions, and longer rails.  

Add some money for a new, larger bed, too.

And the extra extrusions, too.

But having your very own Dual Gantry CoreXY printer - possibly the second in the world to print with two extruders in the same part: **priceless**.

### How much XY travel do I get?

With the new v3 frame size, assuming Boops are used, beyond 180x180 is possible: 184 x 194 travel.

A shorter-depth moving carriage option, like the Micron or Pandora X carriage options, would add ~8mm to each side, but would require a mount to be added for something like a Klicky.

### Can I port this to a V2-style CoreXY gantry?

Good question!

Yes, though you would lose some of the XY density, if running belts just inside of the extrusions, rather than atop the extrusions, Pandora-style.

However... maybe you won't need to.

The v3 Fusion360 CAD is heavily parametric.  Pages of parameters!  In early design, a range of parameters were actively tested, including everything needed for a V2 gantry: extrusion size, bearing size, and belt spacing.

But as of 2023-09-15, some issue with the base sketch is causing computation errors.  These are hard to debug and fix.  Stay tuned here.

### Why not just do an IDEX?

**Answering as a user**: because single-extruder prints can be faster and better without a second toolhead to drag around, and there are some unique capabilities (simultaneous different prints, full-workspace single prints) that become possible with a Dual Gantry.

**Answering as a printer-designer**: it’s a unique and interesting challenge to fit all the belts and toolheads into one gantry, especially in a way that reuses much of what’s out there.  Lots of people have described the main concept, including many years ago, but few have made it to CAD, let alone a functioning printer, let alone one that others can reproduce from a link.

**Answering as a coder**: there are some interesting - but still reasonable - 2D object interference and path-planning challenges, as well as firmware changes, to make this all work initially.  Plus, there are lots of optimizations to implement and then evaluate.

### Seems like a lotta work for a little printer, right?

Well, yes.

But it'd be even more work for a larger printer.
* It'd be impossible to rotate in your lap as you build it.
* It'd be impossible to reuse your V0 frame kit.
* It'd be impossible to store your test build in a file-folder box.

You wouldn't learn anything more.  A bigger printer would take longer to get up to temperature.  It would  have longer, harder-to-tune belts and potentially worse print quality.  It would cost more and require more energy to run.

If you don't routinely print larger objects, and especially if you do
lots of one-off small part-prototyping prints, you'll find that tiny printers rock.  Check out [3D Printers for Ants](https://3dprintersforants.com) for more examples like this one!
