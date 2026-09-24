# larzscript-mandelbrot

The Mandelbrot set in text, and an estimate of its area, in [Larzscript](https://github.com/larz-scripter/larzscript). No dependencies beyond the standard `cli`, `args` and `table` packages.

For each complex number `c`, start from `z = 0` and repeat `z → z² + c`. If `z` ever gets farther than 2 from the origin it escapes for good; `c` is in the set exactly when it never does. The program counts steps until escape (up to `--max`) and draws each point by that count: blank for quick escapes, then `. : - = + * #`, and `@` for points that had not escaped when counting stopped, standing in for "inside".

```
$ larzscript mandelbrot.lz render
             .........:::::::::::::::::::::--------::::::.............
            .......:::::::::::::::::::-------==+==------::::..........
           .....:::::::::::::::::::----------==+*+#=------:::::.......
          ....::::::::::::::::::------------==+*#*+==-------::::::....
         ...::::::::::::::::::-----------===+*@@@@**==-------::::::...
        ..::::::::::::::::::---------=======+#@@@@@+=======----::::::.
       ..::::::::::::::::----------==+*+++**@@@@@@@@@*#+==+*=---::::::
       .::::::::::::::-----------====+@@#@@@@@@@@@@@@@@@*@@#+=---:::::
      .::::::::::::-----------=====#**@@@@@@@@@@@@@@@@@@@@*+==---:::::
      :::::::-------==+====+======+*@@@@@@@@@@@@@@@@@@@@@@@@++=---::::
     .:::----------===+**++*##++++*@@@@@@@@@@@@@@@@@@@@@@@@@*+=---::::
     ::-----------===++*@@@@@@@*++@@@@@@@@@@@@@@@@@@@@@@@@@@@*=----:::
     --------=====*+++*@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@*=-----:::
     --=========++*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+==-----:::
     --=========++*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+==-----:::
     --------=====*+++*@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@*=-----:::
     ::-----------===++*@@@@@@@*++@@@@@@@@@@@@@@@@@@@@@@@@@@@*=----:::
     .:::----------===+**++*##++++*@@@@@@@@@@@@@@@@@@@@@@@@@*+=---::::
      :::::::-------==+====+======+*@@@@@@@@@@@@@@@@@@@@@@@@++=---::::
      .::::::::::::-----------=====#**@@@@@@@@@@@@@@@@@@@@*+==---:::::
       .::::::::::::::-----------====+@@#@@@@@@@@@@@@@@@*@@#+=---:::::
       ..::::::::::::::::----------==+*+++**@@@@@@@@@*#+==+*=---::::::
        ..::::::::::::::::::---------=======+#@@@@@+=======----::::::.
         ...::::::::::::::::::-----------===+*@@@@**==-------::::::...
          ....::::::::::::::::::------------==+*#*+==-------::::::....
           .....:::::::::::::::::::----------==+*+#=------:::::.......
            .......:::::::::::::::::::-------==+==------::::..........
             .........:::::::::::::::::::::--------::::::.............
```

## Commands

| Command | What it does |
| --- | --- |
| `render [--xmin --xmax --ymin --ymax --width --height --max]` | Draws a window (default: the whole set, 70 × 28, 100 steps). Zoom by narrowing the window and raising `--max`. |
| `point --re --im [--max]` | Steps until one point escapes (`point --re=-0.75 --im=0.1` takes 33). |
| `area [--max]` | Grid estimates of the area on 20², 40² and 80² grids next to the true value, about 1.5066. |
| `stats` | Inside count and total steps for a window (used for cross-checking). |

Limits: width 2–200, height 2–100, `--max` up to 1,000 (100,000 for `point`).

## Notes

- The picture uses each pixel's centre, and in the default window rows are spaced twice as far apart as columns because text characters are about twice as tall as wide, so the set looks the right shape in a terminal.
- **The area estimate runs a little high**, and converges slowly. Points that need more than `--max` steps to escape are counted as inside, and the boundary is infinitely detailed: between 1.52 and 1.56 in the test runs, against the true 1.5066.
- Only `+ - * /` and comparisons are involved, all on 64-bit floats, so `tools/reference.py` (the same iteration in Python) reproduces every count exactly. `tests/crosscheck.sh` compares whole pictures (by checksum) and the inside/step totals for nine windows, including deep zooms up to `--max=1000`, and the tests fail on any difference; all nine were identical. Six single points also matched.

## Tests

```
sh tests/run_tests.sh
```

MIT licence.
