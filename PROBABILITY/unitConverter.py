def power_raise(value):
    scientific_notation = "{:.2e}".format(value)
    print(scientific_notation,"-----scn noti----")
    # print(type(scientific_notation),"-----type---")
    # [print(x, end=",") for x in scientific_notation]
    output = ""
    power = ''
    output += scientific_notation[:4] + " x 10 "
    if scientific_notation[5:6] == "+":
        power = scientific_notation[6:]
        if power[0]=='0':
            power = power[1:]
    else:
        power_digit = scientific_notation[6:]
        power = power + '-'

        if power_digit[0]=='0':
            power += power_digit[1:]
        else:
            power +=power_digit
        # power = scientific_notation[5:]
    # print(output,"----------",power)
    return output, power