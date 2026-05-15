

This document provides step-by-step instructions on how to install and configure the Interactive Voice Response (IVR) system from the provided project ZIP file. 

## 1. Prerequisites
Before proceeding, ensure the following are already installed on your Linux system:
* **Asterisk PBX**: Installed and running as a service.
* **Softphones**: Registered SIP accounts (e.g., Linphone, Zoiper).
* **Python 3**: Installed and available in the system path.

## 2. Required Python Libraries
The IVR system uses Python AGI scripts that depend on external libraries for web scraping (Euromilhões) and HTTP requests. You must install these before running the scripts:

```bash
# Install required libraries via pip
sudo pip3 install requests beautifulsoup4

```

* **requests**: Handles communication with external web servers.
* **BeautifulSoup (from bs4)**: Parses HTML content to extract lottery results.

## 3. Configuration Files (`/etc/asterisk`)

The ZIP file contains pre-configured settings for SIP users and the dialplan logic. These must replace the default files in the Asterisk configuration directory.

1. Locate `sip.conf` and `extensions.conf` in the project folder.
2. Move them to `/etc/asterisk/` and set the correct ownership:

```bash
# Copy and replace configuration files
sudo cp sip.conf extensions.conf /etc/asterisk/

# Set permissions for the asterisk user
sudo chown asterisk:asterisk /etc/asterisk/sip.conf /etc/asterisk/extensions.conf

```

## 4. Audio Files (`/usr/share/asterisk/sounds`)

The custom audio prompts for the Lunar Landing game and menus must be placed in the standard Asterisk sounds directory so they can be played back during calls.

1. Locate all `.gsm` files in the project folder.
2. Move them to the system sounds directory:

```bash
# Move audio files
sudo cp *.gsm /usr/share/asterisk/sounds/

# Set ownership
sudo chown asterisk:asterisk /usr/share/asterisk/sounds/*.gsm

```

## 5. AGI Scripts (`/usr/share/asterisk/agi-bin`)

The core logic of the project is handled by Python scripts. These must be placed in the AGI directory, made executable, and assigned to the asterisk user.

1. Locate `euromilhoes_agi.py`, `lunar_game.py`, and `lunar_stats.py`.
2. Move them to the AGI directory:

```bash
# Move Python scripts
sudo cp euromilhoes_agi.py lunar_game.py lunar_stats.py /usr/share/asterisk/agi-bin/

# Set ownership and make them executable
sudo chown asterisk:asterisk /usr/share/asterisk/agi-bin/*.py
sudo chmod +x /usr/share/asterisk/agi-bin/*.py

```

## 6. Finalizing the Installation

Once all files are in place, reload the Asterisk service to apply the new configurations and test the extensions:

1. Enter the Asterisk CLI:
```bash
sudo asterisk -vvvvr

```


2. Reload configurations:
```asterisk
sip reload
dialplan reload

```


3. (Optional) Monitor AGI execution:
```asterisk
agi set debug on

```



---

**Note:** If you encounter permission errors while editing or moving files, always ensure you are using `sudo` as many of these directories are system-protected.
"""
