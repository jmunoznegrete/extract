import matplotlib.pyplot as plt

def evaluate_y(DaySerie, movement, spread):
    upper_limit = DaySerie.Open[0] + movement + spread
    upper_limit_serie=[upper_limit for i in range(DaySerie.len())]
    down_limit = DaySerie.Open[0] - movement
    down_limit_serie=[down_limit for i in range(DaySerie.len())]

    upper_comparison = upper_limit < DaySerie.Low
    down_comparison = down_limit > DaySerie.High

    x = [i for i in range(DaySerie.len())]

    print "*****************", len(DaySerie.High), len(x)

    print x[0:10]
    print DaySerie.High[0:10]

    plt.plot(x, DaySerie.High)
    plt.plot(x, DaySerie.Low)
    plt.plot(x, upper_limit_serie)
    plt.plot(x, down_limit_serie)
    plt.show()

    if upper_comparison > down_comparison:
        return 1
    if upper_comparison < down_comparison:
        return 2
    
    return(0)
