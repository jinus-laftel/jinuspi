from relay_switch import Power

power = Power(channel=4)


def power_on():
    power.on()


def power_off():
    power.off()
