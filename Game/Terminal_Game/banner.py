#!/usr/bin/python3
"""Define the banner picture for Game
"""
from colors import bcol
from user import User


def banner():
    """ This is representation the banner Mastermind"""

    bann = bcol.BLUE
    bann += ' @@@@@@@@@@    @@@@@@    @@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@@@   @@@  @@@  @@@  @@@@@@@   \n'
    bann += '@@@@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  \n'
    bann += '@@! @@! @@!  @@!  @@@  !@@         @@!    @@!       @@!  @@@  @@! @@! @@!  @@!  @@!@!@@@  @@!  @@@  \n'
    bann += '!@! !@! !@!  !@!  @!@  !@!         !@!    !@!       !@!  @!@  !@! !@! !@!  !@!  !@!!@!@!  !@!  @!@  \n'
    bann += '@!! !!@ @!@  @!@!@!@!  !!@@!!      @!!    @!!!:!    @!@!!@!   @!! !!@ @!@  !!@  @!@ !!@!  @!@  !@!  \n'
    bann += '!@!   ! !@!  !!!@!!!!   !!@!!!     !!!    !!!!!:    !!@!@!    !@!   ! !@!  !!!  !@!  !!!  !@!  !!!  \n'
    bann += bcol.NOCOLOR
    bann += '!!:     !!:  !!:  !!!       !:!    !!:    !!:       !!: :!!   !!:     !!:  !!:  !!:  !!!  !!:  !!!  \n'
    bann += ':!:     :!:  :!:  !:!      !:!     :!:    :!:       :!:  !:!  :!:     :!:  :!:  :!:  !:!  :!:  !:!  \n'
    bann += ':::     ::   ::   :::  :::: ::      ::     :: ::::  ::   :::  :::     ::    ::   ::   ::   :::: ::  \n'
    bann += ' :      :     :   : :  :: : :       :     : :: ::    :   : :   :      :    :    ::    :   :: :  :  \n'
    bann += '\n'
    bann += bcol.GREEN+ '\t\t [!] Authors \n' + bcol.NOCOLOR
    bann += '\t\t\tEstefania Ruiz\t'
    bann += '\t Laura Caicedo\t'
    bann += '\t Juan Duque'
    bann += '\t Carolina Lopera\n'
    bann += '\n'
    bann += '\n'
    bann += '\n'

    print(bann)