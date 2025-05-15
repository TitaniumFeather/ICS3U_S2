import math
def hx(TdegC: float, dewPtC: float) -> float:
    """
     * Calculates the humidex, given
     * TdegC, the temp in degrees C
     * dewPtC, the dewpoint in degrees C
     *
     * Returns:
     * hTemp: humidex in degrees C
    """
    hTemp = 0.0

    p = 5417.753 * ((1/273.15)-(1/(273.15+dewPtC)))
    hTemp = TdegC + (5/9) * (6.11 * math.pow(math.e, p) - 10)

    return hTemp

# Main Program
# Your function must work with this code!
# Do not modify!

T = 28.0
D = 26.0
print("H=%6.3f T=%6.3f D=%6.3f" % (hx(T, D), T, D))
T = 30.0
D = 20.0
print("H=%6.3f T=%6.3f D=%6.3f" % (hx(T, D), T, D))
T = 26.0
D = 28.0
print("H=%6.3f T=%6.3f D=%6.3f\n" % (hx(T, D), T, D))
