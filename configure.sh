#!/bin/bash

install_package() {
    distro=$(awk -F= '/^ID=/{print $2}' /etc/*release* | tr -d '"')
    package_name="tor python3 python3-pip"
    case "$distro" in
        "ubuntu"|"debian")
            echo "Installing on $distro..."
            sudo apt-get update
            sudo apt-get install -y $package_name
            ;;
        "centos"|"rhel"|"fedora")
            echo "Installing on $distro..."
            sudo yum install -y $package_name
            ;;
        "arch")
            echo "Installing on $distro..."
            sudo pacman -S --noconfirm $package_name
            ;;
        *)
            echo "Unsupported distribution: $distro"
            exit 1
            ;;
    esac
    echo "Packages have been installed successfully"
}

install_dependencies() {
    distro=$(awk -F= '/^ID=/{print $2}' /etc/*release* | tr -d '"')
    echo "Installing dependencies..."
    if [ "$distro" = "arch" ]; then
        pip3 install -r requirements.txt --break-system-packages
    else
        pip3 install -r requirements.txt
    fi
    echo "Finished installing dependencies"
}

enable_daemon() {
    echo "Enabling Tor..."
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$NAME
    elif [ -f /etc/redhat-release ]; then
        OS=$(awk '{print $1}' /etc/redhat-release)
    else
        echo "Unsupported OS"
        exit 1
    fi

    case "$OS" in
        "Ubuntu"|"Debian GNU/Linux"|"Arch Linux")
            sudo systemctl enable tor
            ;;
        "CentOS"|"Red Hat Enterprise Linux Server")
            sudo chkconfig tor on
            ;;
        *)
            echo "Unsupported OS: $OS"
            exit 1
            ;;
    esac
    echo "Tor is enabled on boot"
}

update_torrc() {
    echo "Configuring /etc/tor/torrc file"
    if [ -f "/etc/tor/torrc" ]; then
        sudo sed -i 's/^#ControlPort 9051/ControlPort 9051/' /etc/tor/torrc
        sudo sed -i 's/^#CookieAuthentication 0/CookieAuthentication 1/' /etc/tor/torrc
        echo "Done configuring Tor file"
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
        sudo sed -i 's/^#ControlPort 9051/ControlPort 9051/' /etc/tor/torrc
        sudo sed -i "s/^HashedControlPassword.*$/HashedControlPassword $hashed_password/" /etc/tor/torrc
        sudo systemctl restart tor
        echo "Finished configuring torrc file"
        echo "The Python script can now be executed"
    else
        echo "Tor configuration file not found."
        exit 1
    fi
}

main() {
    install_package
    install_dependencies
    enable_daemon
    update_torrc
    restart_tor_with_hashed_password
}

main
