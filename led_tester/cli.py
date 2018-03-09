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
    #invoke the function to parse the input file
    N, instructions = parseFile(input)
        
    if (N!=0):
        #creating an object of the class LEDTester
        ledTester = LEDTester(N)
        for instruction in instructions:
            instruction=str(instruction)
            #invoke function to apply the commands
            ledTester.apply(instruction)
    
        #invoke the function to count the lights that are on and print it.
        print("Number of lights on are : ", ledTester.countLights() )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
