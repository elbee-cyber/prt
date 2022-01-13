#!/bin/bash

/usr/bin/pip3 install argparse
/usr/bin/pip3 install Sublist3r
/usr/bin/pip3 install googlesearch-python
/usr/bin/pip3 install BeautifulSoup
/usr/bin/pip3 install tld

/usr/bin/chmod +x ./passive_recon.py

main() {
    read -p "Do you want to copy it to the PATH?[Y/N]: " menu
        if [[ $menu == "Y" || $menu == "y" ]]
        then
            if [ "$EUID" -ne 0 ]
            then
                echo "Permission required"
            fi
            sudo cp ./passive_recon.py /usr/bin/passive_recon.py
        elif [[ $menu == "N" || $menu == "n" ]]
        then
            echo "There is nothing to do"
        else
            echo "Invalid option"
            main
    fi
}
main
