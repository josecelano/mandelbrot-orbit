[![Build Status](https://travis-ci.com/josecelano/mandelbrot-orbit.svg?branch=master)](https://travis-ci.com/josecelano/mandelbrot-orbit)

## Mandelbrot Orbit

This program generates the orbit for a given Mandelbrot point. Something like:

![Orbit of a mandelbrot point](mandelbrot-orbit-sample.png)

That's the orbit of point (-1.3,0) which has period 4.

### Math

This is the Mnadelbrot Set basic formula:

```
f(z) = z² + c
```

where `z` and `c` are complex number. 

The Mandelbrot set is the set of complex numbers `c` for which the function does not diverge when iterated from z=0.
Than means, given a `c` complex number, if you apply the formula to that number `n` times using the previous result as the new `z` number, that `c` belongs to Mandelbrot Set if the sequence does not diverge.

This python script plots the series for a given complex point.

### Prerequisites

```
Python 3.6.9
pytest-5.3.5
```

### Usage

Install:
```
./bin/install
```

Run:
```
mandelbrot-orbit '{ZX}' '{ZY}' {NUM_ITERATIONS}
mandelbrot-orbit -0.1 0.7 100
```

The script generates an image: `mandelbrot-orbit.png`

### Development

Setup:
```bash
./bin/dev-setup
```

Running the tests:
```bash
./bin/test
```

Run:
```bash
./bin/run '-0.1' '0.7' 100
```

### Troubleshooting

You could see this error:
```
/home/josecelano/.local/lib/python3.6/site-packages/matplotlib/backends/backend_gtk3.py:195: Warning: Source ID 8 was not found when attempting to remove it
  GLib.source_remove(self._idle_draw_id)
```
It seems to be a known issue pending to release:

https://stackoverflow.com/questions/29540845/how-can-i-deactivate-warning-source-id-510-was-not-found-when-attempting-to-re

### TODO

* Although calculations are done with an arbitrary precision library, we use `matplotlib` to generate the graph and that package uses a float type for data source so we cannot plot a point with greater precision than the language float precision.
