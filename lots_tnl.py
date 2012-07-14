#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © Alejandro Cabrera July 2012, <cpp.cabrera@gmail.com>
# Legacy of a Thousand Suns Time to Next Level Calculator (loats-tnl-calc)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
from __future__ import print_function
import sys
from collections import namedtuple
import colorama
import time

def pyinput_func():
    """
    Determines safe input function to use depending on
    Python version.
    """
    if sys.version_info[0] >= 3:
        return input
    else:
        return raw_input

inp_fn = pyinput_func()

def tstring(secs):
    """
    Given seconds, returns a string breaking the seconds down
    into hours, minutes, and seconds.
    """
    return time.strftime('%H:%M:%S', time.gmtime(secs))

def tnl(honor_recharge_time_secs,
        energy_recharge_time_secs,
        stam_recharge_time_secs,
        current_xp):
    """
    Calculate time to next level and output information to users.
    """
    hxp_per_hit = [1,1.5,2]
    exp_per_hit = [1,1.5,2]
    sxp_per_hit = [1,3,5]

    hxp_per_sec = [float(x)/honor_recharge_time_secs for x in hxp_per_hit]
    exp_per_sec = [float(x)/energy_recharge_time_secs for x in exp_per_hit]
    sxp_per_sec = [float(x)/stam_recharge_time_secs for x in sxp_per_hit]

    tot_per_sec = [sum(x) for x in (hxp_per_sec,exp_per_sec,sxp_per_sec)]

    cases = [int(current_xp/float(x)) for x in tot_per_sec]
    best_case_str = colorama.Fore.CYAN + 'Best case'
    worst_case_str = colorama.Fore.MAGENTA + 'Worst case'
    avg_case_str = colorama.Fore.YELLOW + 'Likely case'

    print()
    print('Times given as hours:minutes:seconds')
    print('{} ttnl: {}'.format(best_case_str, tstring(cases[2])))
    print('{} ttnl: {}'.format(worst_case_str, tstring(cases[0])))
    print('{} ttnl: about {}'.format(avg_case_str,
                                     tstring(cases[1])))
    print(colorama.Fore.RESET)

def print_and_read(in_str):
    """
    Output colorful text to terminal and recover
    user input values as integers.
    """
    print(in_str, end='')
    return int(inp_fn(''))

def gather_input():
    """
    Prompts user to input stamina, energy, honor, and xp values.
    @return A NamedTuple containing ('e','h','s','tnl')
    """

    UserData = namedtuple('UserData', ['e', 'h', 's','tnl'])

    # Some constants
    s_str = colorama.Fore.YELLOW + 'stamina' + colorama.Fore.RESET
    e_str = colorama.Fore.GREEN + 'energy' + colorama.Fore.RESET
    min_str = colorama.Fore.BLUE + 'minutes' + colorama.Fore.RESET
    sec_str = colorama.Fore.CYAN + 'seconds' + colorama.Fore.RESET
    in_emstr = 'Enter {} to recharge 1 {} point: '.format(min_str, e_str)
    in_esstr = 'Enter {} to recharge 1 {} point: '.format(sec_str, e_str)
    in_smstr = 'Enter {} to recharge 1 {} point: '.format(min_str, s_str)
    in_ssstr = 'Enter {} to recharge 1 {} point: '.format(sec_str, s_str)

    try:
        em = print_and_read(in_emstr)
        es = print_and_read(in_esstr)
        sm = print_and_read(in_smstr)
        ss = print_and_read(in_ssstr)
        tnl_xp = int(inp_fn('Enter remaining experience until next level: '))

    except (ValueError):
        print('error: Please enter only numbers for time values.')
        print('Aborting.')
        quit()

    except (KeyboardInterrupt):
        print()
        print('Goodbye.')
        quit()

    es += 60 * em
    ss += 60 * sm

    return UserData(e=es, s=ss, h=120, tnl=tnl_xp)

if __name__ == '__main__':
    colorama.init()
    ud = gather_input()
    tnl(ud.h, ud.e, ud.s, ud.tnl)

    # Attempt a graceful exit so users can read their results
    try:
        inp_fn('Press enter to continue...')
    except (EOFError):
        pass
    print()
