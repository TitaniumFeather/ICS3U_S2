import math

def wc(TdegC: float, windKPH: float) -> float:
    """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
    """
    vTemp = 0
    vTemp = 13.12 + 0.6125 * TdegC
    vTemp = vTemp - 11.37 * math.pow(windKPH, 0.16)
    vTemp  = vTemp + 0.3965 * TdegC * math.pow(windKPH, 0.16)
    return vTemp


def interpret(WC: float):
    if WC >= -9:
        return "Low risk"
    elif WC >= -27:
        return "Moderate risk of hypothermia"
    elif WC >= -39:
        return "High risk of frostbite"
    elif WC >= -47:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif WC >= -54:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    else:
        return "Extreme risk: exposed skin freezes in under 2 minutes"

    

# the Main program
T = -5.0
W = 10.0
print("WC=%8.3f(%s) T=%8.3f W=%6.3f km/h" % (wc(T, W), interpret(wc(T, W)), T, W))
T = -20.0; W = 20.0
print("WC=%8.3f(%s) T=%8.3f W=%6.3f km/h" % (wc(T, W), interpret(wc(T, W)), T, W))
T = -45.0; W = 40.0
print("WC=%8.3f(%s) T=%8.3f W=%6.3f km/h" % (wc(T, W), interpret(wc(T, W)), T, W))
