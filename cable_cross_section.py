# Cable cross section calculator

def cross_section(impedance_ohm, length_m, resistivity_ohm_m=1.68e-8):
    """Calculate cable cross section area in mm^2.

    Args:
        impedance_ohm (float): Target cable impedance in ohms.
        length_m (float): Cable length in meters.
        resistivity_ohm_m (float): Material resistivity in ohm*meter (default: copper).

    Returns:
        float: Cross section area in square millimeters.
    """
    area_m2 = resistivity_ohm_m * length_m / impedance_ohm
    return area_m2 * 1e6


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Cable cross section calculator")
    parser.add_argument("impedance", type=float, help="Desired impedance in ohms (1-16)")
    parser.add_argument("length", type=float, help="Cable length in meters")
    parser.add_argument("--resistivity", type=float, default=1.68e-8,
                        help="Conductor resistivity in ohm*m (default copper)")
    args = parser.parse_args()

    if not (1 <= args.impedance <= 16):
        parser.error("Impedance must be between 1 and 16 ohms")

    area_mm2 = cross_section(args.impedance, args.length, args.resistivity)
    print(f"Required cross section: {area_mm2:.3f} mm^2")


if __name__ == "__main__":
    main()
