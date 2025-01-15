#!/bin/bash 

## cheking root permession 
if [[ $EUID -ne 0 ]] 
    then echo "Run this script with root permession please"
    exit 
fi 

OS_VERSION=$(cat /etc/os-release | head -n 1 | cut -d "=" -f2 | sed 's/^"\(.*\)"$/\1/' | cut -d " " -f1)

## checking for tor files 
check_tor() {
    TOR_VERSION=$(tor --version | head -n 1 )

    case $OS_VERSION in
        "Arch")
            pacman -S tor torsocks --noconfirm 

        ;;break;;
        "debian | ubuntu ")
            apt install tor torsocks -y 

        ;;break;;
        "fedora")
            dnf install tor torsocks -y 

        ;;break;;
        *)
          "Enable to download Tor in your Distro"  
        ;; esac 

    ## configuring torify 
    sed -i 's/#\([^ ]*ControlPort\)/\1/' /etc/tor/torrc 
    sed -i 's/^#CookieAuthentication\s\d/CookieAuthentication 0' etc/tor/torrc

    systemctl restart tor 

    #checking connectivity 
    status=$(torify curl https://ifconfig.so  > status ; cat status | grep -P "^\d{1,3}(\.\d{1,3}){3}$")
    if [[ $status == "" ]] 
        then echo "Error getting Tor ip Address" 
        exit 
    fi
}

install_requirement() {  
    PIP_VERSION=$(pip --version | cut -d " " -f2 | grep -E "[0-9]+")   
    if  [[  $PIP_VERSION == ""  ]] 
        then echo "pip not installed "
        echo "installing pip" 

        case $OS_VERSION in
            "Arch")
                pacman -S python python-pip --noconfirm 

            ;;break;;
            "debian | ubuntu ")
                apt install python python-pip -y 

            ;;break;;
            "fedora")
                dnf install python python-pip -y 

            ;;break;;
            *)
              "Enable to download pythobn in your Distro"  
            ;; esac 
    fi 
    # install requiremennts 
    pip install -r requirements.txt --break-systemù-packages 

    # wait for the installation till it ends
    wait  
}