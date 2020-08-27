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
import logging
import os
import sys
import click

from TEMPLATE import __version__, __title__
from TEMPLATE.logging import colour
from TEMPLATE.logging import logger_setup


def print_help():
    lines = ['',
             colour(f'▖▙ {__title__} v{__version__} ▟▗'.center(80), fg='blue'),
             '',
             colour('METHODS'.center(80), fg='blue', attr=['underscore']),
             '  ' + colour('tree_convert → Convert/validate GTDB accessions within a tree.', fg='blue'),
             '',
             colour(''.center(80), fg='blue', attr=['underscore']),
             colour(f'  Use: {__title__} <command> -h for command specific help.', fg='blue')]
    print('\n'.join(lines))


@click.group()
def greet():
    """A sample command group."""
    pass

@greet.command()
@click.argument('user', envvar='USER')
def hello(user):
    """Greet a user."""
    click.echo('Hello %s' % user)

@greet.command()
def world():
    """Greet the world."""
    click.echo('Hello world!')

def main(args=None):

    greet()
    return


    parser = argparse.ArgumentParser(prog=__title__, add_help=False, conflict_handler='resolve')
    subparsers = parser.add_subparsers(help="--", dest='subparser_name')

    # tree_convert
    tree_convert_p = subparsers.add_parser('tree_convert', conflict_handler='resolve',
                                           help='Convert/validate GTDB accessions within a tree.')

    mutual_genome_denovo_wf = tree_convert_p.add_argument_group('mutually exclusive required arguments')
    mutex_group = mutual_genome_denovo_wf.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('--ncbi',
                             help='Method to apply to taxa that only have a NCBI accession.')
    mutex_group.add_argument('--mixed',
                             help='Method to apply to taxa that have both an NCBI and USER accession.')
    mutex_group.add_argument('--user',
                             help='Method to apply to taxa that only have a USER accession.')
    mutex_group.add_argument('--release',
                             help="The GTDB release to consider: [R89, R95]")

    # Verify that a subparser was selected
    if len(sys.argv) == 1:
        print_help()
        sys.exit(0)
    elif sys.argv[1] in {'-v', '--v', '-version', '--version'}:
        print(f'binf v{__version__}')
        sys.exit(0)
    else:
        print(f'binf v{__version__}')
        args = parser.parse_args(args)

        # setup logger
        logger_setup(args.out_dir if hasattr(args, 'out_dir') else None,
                     "binf.log", "binf", __version__, False,
                     hasattr(args, 'debug') and args.debug)
        log = logging.getLogger('default')

        # Validate the input arguments.
        if not os.path.isfile(args.newick):
            print(f'The input file cannot be found: {args.newick}')
            sys.exit(1)
        if args.method not in {'pd', 'node'}:
            print('Invalid choice for method, select either: pd or node')
            sys.exit(1)
        out_dir = os.path.dirname(args.output)
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

        # newick_to_pdm(args.newick, args.method, args.output)
        tree_convert()

    # Done - no errors.
    sys.exit(0)


if __name__ == "__main__":
    main()
