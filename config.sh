#!/bin/bash

## checking root permission
if [[ $EUID -ne 0 ]]; then
    echo "Run this script with root permission please"
    exit 1
fi

## Get OS ID in lowercase
OS_ID=$(grep '^ID=' /etc/os-release | cut -d '=' -f2 | tr -d '"' | tr '[:upper:]' '[:lower:]')

## Check for Tor installation and configure
check_tor() {
    # Check if Tor is already installed
    if ! command -v tor &> /dev/null; then
        echo "Installing Tor and Torsocks..."
        case $OS_ID in
            "arch")
                pacman -S tor torsocks --noconfirm 
                ;;
            "debian" | "ubuntu")
                apt update
                apt install tor torsocks -y 
                ;;
            "fedora")
                dnf install tor torsocks -y 
                ;;
            *)
                echo "Unable to install Tor on your distribution: $OS_ID"
                exit 1
                ;;
        esac
    else
        TOR_VERSION=$(tor --version | head -n 1)
        echo "Tor already installed: $TOR_VERSION"
    fi

    ## Configuring Tor
    echo "Configuring Tor..."
    
    # Backup original config
    cp /etc/tor/torrc /etc/tor/torrc.bak
    
    # Uncomment ControlPort and set authentication
    sed -i 's/^#ControlPort .*/ControlPort 9051/' /etc/tor/torrc 
    sed -i 's/^#CookieAuthentication .*/CookieAuthentication 1/' /etc/tor/torrc
    sed -i 's/^#SOCKSPort .*/SOCKSPort 9050/' /etc/tor/torrc
    
    # Add HashedControlPassword for authentication
    if ! grep -q "HashedControlPassword" /etc/tor/torrc; then
        echo "HashedControlPassword $(tor --hash-password "your_password" | tail -n 1)" >> /etc/tor/torrc
    fi

    # Fix permissions for Tor user
    chown -R debian-tor:debian-tor /var/lib/tor 2>/dev/null || true
    chown -R tor:tor /var/lib/tor 2>/dev/null || true
    
    # Stop any running Tor processes
    systemctl stop tor.service 2>/dev/null || true
    pkill -9 tor 2>/dev/null || true
    
    # Wait for port to be free
    echo "Releasing port 9050..."
    counter=0
    while ss -tulpn | grep -q ':9050\b'; do
        sleep 0.5
        counter=$((counter+1))
        if [ $counter -gt 10 ]; then
            echo "Force-releasing port 9050"
            fuser -k 9050/tcp
            break
        fi
    done

    # Start Tor with error handling
    if ! systemctl start tor.service; then
        echo "Tor failed to start. Checking logs..."
        journalctl -u tor.service -xe --no-pager | tail -n 20
        echo "Trying to start Tor directly..."
        tor &
        sleep 5
    fi

    ## Checking connectivity
    echo "Verifying Tor connection..."
    status=$(torify curl -s https://ifconfig.me 2>/dev/null)
    
    if [[ $status =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        echo "Tor connection successful! Exit IP: $status"
    else
        echo "Error: Failed to get Tor IP address"
        echo "Trying alternative method..."
        status=$(curl --socks5 localhost:9050 -s https://ifconfig.me)
        if [[ $status =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
            echo "Tor connection successful via SOCKS! Exit IP: $status"
        else
            echo "Tor connection test failed. Check logs with: journalctl -u tor.service"
            exit 1
        fi
    fi
}

install_requirements() {  
    ## Check for Python
    if ! command -v python3 &> /dev/null; then
        echo "Installing Python..."
        case $OS_ID in
            "arch")
                pacman -S python --noconfirm 
                ;;
            "debian" | "ubuntu")
                apt install python3 -y 
                ;;
            "fedora")
                dnf install python3 -y 
                ;;
            *)
                echo "Unable to install Python on your distribution"
                exit 1
                ;;
        esac
    fi

    ## Check for pip
    if ! command -v pip3 &> /dev/null; then
        echo "Installing pip..."
        case $OS_ID in
            "arch")
                pacman -S python-pip --noconfirm 
                ;;
            "debian" | "ubuntu")
                apt install python3-pip -y 
                ;;
            "fedora")
                dnf install python3-pip -y 
                ;;
        esac
    fi

    ## Install requirements
    echo "Installing Python dependencies..."
    pip3 install -r requirements.txt
}

## Main execution
check_tor
install_requirements

echo "Setup completed successfully!"
echo "You can now run: python3 darkscrappy.py"
