import unittest
import mpmath

from mandelbrot_orbit.orbit_calculator import OrbitCalculator


class OrbitCalculatorTest(unittest.TestCase):

    def test_orbit_of_point_0(self):
        c = mpmath.mpc(real='0.0', imag='0.0')
        orbit_re, orbit_im = OrbitCalculator.generate(c, 10)

        self.assertEqual(['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'], orbit_re)
        self.assertEqual(['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'], orbit_im)

    def test_orbit_of_point_that_tends_to_a_fixed_point(self):
        c = mpmath.mpc(real='-0.1', imag='0.1')

        orbit_re, orbit_im = OrbitCalculator.generate(c, 10)

        self.assertEqual([
            '-0.1',
            '-0.1',
            '-0.0964',
            '-0.097763',
            '-0.0974656',
            '-0.0974917',
            '-0.0975012',
            '-0.0974958',
            '-0.0974973',
            '-0.0974971'
        ], orbit_re)
        self.assertEqual([
            '0.1',
            '0.08',
            '0.084',
            '0.0838048',
            '0.083614',
            '0.083701',
            '0.0836797',
            '0.0836823',
            '0.0836827',
            '0.0836823'
        ], orbit_im)

    def test_orbit_of_point_with_period_4(self):
        c = mpmath.mpc(real='-1.3', imag='0')

        orbit_re, orbit_im = OrbitCalculator.generate(c, 10)

        self.assertEqual([
            '-1.3',
            '0.39',
            '-1.1479',
            '0.0176744',
            '-1.29969',
            '0.389188',
            '-1.14853',
            '0.0191275',
            '-1.29963',
            '0.389049'
        ], orbit_re)
        self.assertEqual(['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'], orbit_im)
