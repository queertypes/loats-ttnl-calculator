#!/usr/bin/env python
#
# Author: Alejandro Cabrera, cpp.cabrera@gmail.com
# Legacy of a Thousand Suns Time to Next Level Calculator (lots-tnl-calc)
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
import colorama

def tstring(secs):
    h = int(int(secs) / 3600)
    secs -= h * 3600
    m = int(int(secs) / 60)
    secs -= m * 60
    return '{}h:{}m:{}s'.format(h,m,secs)

def tnl(honor_recharge_time_secs,
        energy_recharge_time_secs,
        stam_recharge_time_secs,
        current_xp):
    hxp_per_hit = [1,1.5,2]
    exp_per_hit = [1,1.5,2]
    sxp_per_hit = [1,3,5]

    hxp_per_sec = [float(x)/honor_recharge_time_secs for x in hxp_per_hit]
    exp_per_sec = [float(x)/energy_recharge_time_secs for x in exp_per_hit]
    sxp_per_sec = [float(x)/stam_recharge_time_secs for x in sxp_per_hit]

    tot_per_sec = [sum(x) for x in (hxp_per_sec,exp_per_sec,sxp_per_sec)]

    cases = [int(current_xp/float(x)) for x in tot_per_sec]
    best_case_str = colorama.Fore.GREEN + 'best case'
    worst_case_str = colorama.Fore.MAGENTA + 'worst case'
    avg_case_str = colorama.Fore.YELLOW + 'likely case'

    print()
    print('{} time to tnl: {}'.format(best_case_str, tstring(cases[2])))
    print('{} time to tnl: {}'.format(worst_case_str, tstring(cases[0])))
    print('{} time to tnl: about {}'.format(avg_case_str, 
                                            tstring(cases[1])))
    print(colorama.Fore.RESET)    

if __name__ == '__main__':
    colorama.init()

    if sys.version_info[0] == 3:
        inp = input
    else:
        inp = raw_input

    s_str = colorama.Fore.YELLOW + 'stamina' + colorama.Fore.RESET
    h_str = colorama.Fore.MAGENTA + 'honor' + colorama.Fore.RESET
    e_str = colorama.Fore.GREEN + 'energy' + colorama.Fore.RESET
    min_str = colorama.Fore.BLUE + 'minutes' + colorama.Fore.RESET
    sec_str = colorama.Fore.CYAN + 'seconds' + colorama.Fore.RESET
    in_emstr = 'Enter {} to recharge 1 {} point: '.format(min_str, e_str)
    in_esstr = 'Enter {} to recharge 1 {} point: '.format(sec_str, e_str)
    in_smstr = 'Enter {} to recharge 1 {} point: '.format(min_str, s_str)
    in_ssstr = 'Enter {} to recharge 1 {} point: '.format(sec_str, s_str)
    in_hmstr = 'Enter {} to recharge 1 {} point: '.format(min_str, h_str)
    in_hsstr = 'Enter {} to recharge 1 {} point: '.format(sec_str, h_str)

    try:
        print(in_emstr, end='')
        em = int(inp(''))
        print(in_esstr, end='')
        es = int(inp(''))
        print(in_smstr, end='')
        sm = int(inp(''))
        print(in_ssstr, end='')
        ss = int(inp(''))
        print(in_hmstr, end='')
        hm = int(inp(''))
        print(in_hsstr, end='')
        hs = int(inp(''))
        tnl_xp = int(inp('Enter remaining experience until next level: '))

    except (ValueError):
        print('error: Please enter only numbers for time values.')
        print('Aborting.')
        quit()

    es += 60 * em
    ss += 60 * sm
    hs += 60 * hm

    tnl(hs, es, ss, tnl_xp)

    try:
        inp('Press enter to continue...')
    except (EOFError):
        pass
    print()
