#!/bin/sh

install_package() {
    distro=$(cat /etc/*release* | grep "^ID=" | cut -d '=' -f 2 | tr -d '"')
    package_name="tor python3 python-pip" 
    case "$distro" in
        "ubuntu" | "debian")
            echo "Installing on $distro..."
            sudo apt-get update
            sudo apt-get install -y $package_name
            echo "packages has been installed successfully"
            ;;
        "centos" | "rhel" | "fedora")
            echo "Installing on $distro..."
            sudo yum install -y $package_name
            echo "packages has been installed successfully"
            ;;
        "arch")
            echo "Installing on $distro..."
            sudo pacman -S --noconfirm  $package_name 
            echo ""
            echo ""
            echo "packages has been installed successfully"
            echo ""
            echo ""
            ;;
        *)
            echo "Unsupported distribution: $distro"
            ;;
    esac
}

install_dependecies (){ 
    
    distro=$(cat /etc/*release* | grep "^ID=" | cut -d '=' -f 2 | tr -d '"')
    case "$distro" in
        "arch")
            echo "Installing dependecies ..."
            pip3 install -r requirement.txt --break-system-packages
            echo ""
            echo ""
            echo "finish installing dependecies"
            echo ""
            echo ""
            ;;
        *)
            pip3 install -r requirement.txt 
            ;;
    esac
}

enable_daemon() {
    
    sleep 2 
    echo "enabling tor ..."
    echo ""
    echo ""


    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$NAME
    elif [ -f /etc/redhat-release ]; then
        OS=$(cat /etc/redhat-release | awk '{print $1}')
    else
        echo "Unsupported OS"
    fi

    if [ "$OS" = "Ubuntu" ] || [ "$OS" = "Debian GNU/Linux" ] ; then
        sudo systemctl enable tor
        echo "tor is enabled on boot "
    elif [ "$OS" = "Arch Linux" ] ; then
        sudo systemctl enable tor
        echo "tor is enabled on boot "
    elif [ "$OS" = "CentOS" ] || [ "$OS" = "Red Hat Enterprise Linux Server" ] ; then
        sudo service tor start
        echo "tor is enabled on boot "
    else
        echo "Unsupported OS: $OS"
        exit 1
    fi
    sleep 2 
}

update_torrc() {

    
    echo ""
    echo ""
    echo "configuring /etc/tor/torrc file "
    echo ""
    echo ""

    if [ -f "/etc/tor/torrc" ]; then
        sudo sed -i '/^#ControlPort/s/#//' /etc/tor/torrc
        sudo sed -i '/^ControlPort/s/9051/1/' /etc/tor/torrc
        
        sudo sed -i '/^#CookieAuthentication/s/#//' /etc/tor/torrc
        sudo sed -i '/^CookieAuthentication/s/0/1/' /etc/tor/torrc
        sleep 2 
        echo "done configuring tor file "
        echo ""
        echo ""
    
    else
        echo "Tor configuration file not found."
        exit 1
    fi
}


restart_tor_with_hashed_password() {
    read -s -p "Enter password for Tor ControlPort: " password
    echo

    hashed_password=$(tor --hash-password "$password")

    if [ -f "/etc/tor/torrc" ]; then

        sudo sed -i '/^#ControlPort/s/#//' /etc/tor/torrc
        sudo sed -i '/^ControlPort/s/9051/1/' /etc/tor/torrc

        sudo sed -i "s/^HashedControlPassword.*$/HashedControlPassword $hashed_password/" /etc/tor/torrc

        sudo systemctl restart tor
        sleep 1 
        echo "end configuring torrc file" 
        echo "" 
        echo ""
        echo "for executing the python script "
    else
        echo "Tor configuration file not found."
        exit 1
    fi
}

main() {
    install_package
    install_dependecies 
    enable_daemon
    update_torrc
    restart_tor_with_hashed_password
}

main 