#!/usr/bin/python3
#Originally from https://econometrics.io/yield-to-maturity-calculation-using-a-python-script/
import argparse
import math
import sys 
 
def total_present_value(face_value, coupon, periods, rate):
    total_pv = 0
    for n in range(1, periods+1):
        total_pv += coupon / math.pow((1 + rate), n)
 
    total_pv += face_value / math.pow((1 + rate), periods)
 
    return total_pv
    
 
def main():
    """
    python3 yield.py -p 139.87 -f 99.94 -r 6.250 -y 12 -s
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=float, help='specifies the current price')
    parser.add_argument('-f', type=float, help='specifies the face Value')
    parser.add_argument('-r', type=float, help='specifies the annual coupon rate in percent')
    parser.add_argument('-y', type=int, help='specifies the number of years remaining to maturity')
    parser.add_argument('-s', action='store_true', default=False, help='coupon is a semi-annual coupon. Default is annual')

    args = parser.parse_args()

    if not args.p or not args.f or not args.r or not args.y:
        parser.print_help()
        sys.exit(0)

    coupon_rate = args.r / 100.0
    coupon = args.f * coupon_rate
    factor = 2 if args.s else 1
 
    print("------------------------------------------------")
    print("Price: %s" % args.p)
    print("Face Value: %s" % args.f)
    print("Annual coupon rate: %.2f%%" % args.r)
    print("Coupon: %s" % coupon)
    print("Semi-annual coupon: %s" % args.s)
    print("Years remaining: %s" % args.y)
    print("\n")
 
 
    ytm = coupon_rate
    condition = True
    while condition:
        if (args.p < args.f):
            ytm += 0.00001
        else:
            ytm -= 0.00001
 
        total_pv = total_present_value(args.f, coupon/factor, args.y*factor, ytm/factor)
 
        if (args.p < args.f):
            condition = total_pv > args.p
        else:
            condition = total_pv < args.p
 
    print("Yield to Maturity:  %.2f%%" % (ytm*100.0))
 
 
if __name__ == '__main__':
    main()
