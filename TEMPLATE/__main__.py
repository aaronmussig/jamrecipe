###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

import argparse

from corejam.argparse import CustomArgParser
from corejam.argparse import jam_parser

from TEMPLATE import __title__, __version__, __url__


def main_parser():
    parser = CustomArgParser(prog=__title__, ver=__version__, url=__url__)
    subparsers = parser.add_subparsers(dest='subparser_name')
    subparsers.metavar = 'methods'

    # define common shared arguments
    base_subparser = argparse.ArgumentParser(add_help=False)
    base_subparser.add_argument('--debug', help='output debugging information', action='store_true', default=False)

    # subparser a
    subparser_a = subparsers.add_parser('foo',
                                        help='foo help.',
                                        parents=[base_subparser])

    sa_mutex = subparser_a.add_argument_group('mutually exclusive required arguments')
    mutex_group = sa_mutex.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('--a',
                             help='add a.')

    subparser_b = subparsers.add_parser('bar',
                                        help='bar help.',
                                        parents=[base_subparser])
    subparser_b.add_argument('--b',
                             help='add b.')

    return parser


def main():
    with jam_parser(main_parser(), __title__, __version__) as args:
        pass


if __name__ == "__main__":
    main()
