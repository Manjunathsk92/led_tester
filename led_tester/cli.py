# -*- coding: utf-8 -*-

"""Console script for ledtester."""
import sys
import click
from led_tester.utils import parseFile, LEDTester
click.disable_unicode_literals_warning = True



@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for ledtester."""
    print("input", input)
    
    N, instructions = parseFile(input)
    
    ledTester = LEDTester(N)
    var=0
    for instruction in instructions:
        var+=1
        if var%100==0:
            print("100 records")
        if var%1000 ==0:
            print("1000 records")
        ledTester.apply(instruction)
    
        
    print("Number of lights on are : ", ledTester.countLights() )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
