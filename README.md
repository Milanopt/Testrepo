# Testrepo

My repository to test new ideas

## Cable cross section calculator

`cable_cross_section.py` computes the required cable cross sectional area for a
specified impedance and length. The impedance range 1–16 Ω is supported. Run it
like this:

```bash
python cable_cross_section.py <impedance_ohm> <length_m>
```

Example:

```bash
python cable_cross_section.py 8 50
```

This uses the resistivity of copper by default (1.68e-8 Ω·m). Use the
`--resistivity` option to specify a different material.
