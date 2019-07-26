#ZADANIE 1
def calculate_paint(efficency_ltr_per_m2, *args):
    paint = efficency_ltr_per_m2 * sum(args)
    print("You need {} liters of paint.".format(paint))
    return paint

calculate_paint(2, 15, 12, 20, 8)

to_paint = [15, 12, 20, 8]

calculate_paint(2, *to_paint)

#ZADANIE 2
import os

def log_it(*args):
    path = r'c:\temp\log_it.txt'
    with open(path, "a") as f:
        for i in args:
            f.write(i)
            f.write(' ')
        f.write('\n')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')