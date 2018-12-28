# Copyright © 2018 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

import locale
import argparse

from . import __version__, __description__

def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-V', '--version', action='version', version=str(__version__))
    parser.add_argument('-c', '--config', help='Take a config file instead of command line parameters')
    parser.add_argument('-f', '--clientflags', help='Pass additional flags to the client invocation (in addition to the usual -Js1)')
    parser.add_argument('-F', '--serverflags', help='Pass additional flags to the server invocation (in addition to the usual -J1)')
    parser.add_argument('-u', '--username', help='The ssh username to use')
    parser.add_argument('-p', '--password', help='The ssh password to use')
    parser.add_argument('-k', '--keyfilename', help='The ssh key filename to use')
    parser.add_argument('-P', '--port', type=int, help='The ssh port to use, otherwise let iperf3 decide', default=-1)
    args = parser.parse_args()

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    main()

