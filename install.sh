#!/bin/sh

#Fetch and build rtl-sdr
echo "***** building rtl-sdr *****"
cd /usr/src/app
git clone git://git.osmocom.org/rtl-sdr.git
cd rtl-sdr/
mkdir build
cd build
cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
make
sudo make install
sudo ldconfig
cd ../..
echo "***** finished building rtl-sdr *****"

#Disable the DVB-T driver, which would prevent the rtl_sdr tool from accessing the stick
#(if you want to use it for DVB-T reception later, you should undo this change):
echo "***** disabling DVB-T driver *****"
sudo bash -c 'echo -e "\n# for RTL-SDR:\nblacklist dvb_usb_rtl28xxu\n" >> /etc/modprobe.d/blacklist.conf'

#Disable the problematic kernel module for the current session:
sudo rmmod dvb_usb_rtl28xxu 



echo "***** Begin Setup *****"

#Download OpenWebRX
cd /usr/src/app
git clone https://github.com/fallenangel3k/openwebrx.git


#mynewstuff
go get -u github.com/tweekmonster/nmux/cmd/nmux
cd /usr/src/app

#very important! connector
git clone https://github.com/fallenangel3k/owrx_connector.git
cd owrx_connector
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..

#rpitx installs most of the important stuff!!
git clone https://github.com/fallenangel3k/rpitx
cd rpitx
./install.sh

git clone https://github.com/jketterl/js8py.git
cd js8py
sudo python3 setup.py install
cd ..

git clone https://github.com/szechyjs/mbelib.git
cd mbelib
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..

git clone https://github.com/jketterl/digiham.git
cd digiham
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..

git clone https://github.com/f4exb/dsd.git
cd dsd
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..

sudo git clone https://github.com/hessu/aprs-symbols /opt/aprs-symbols

wget http://physics.princeton.edu/pulsar/k1jt/wsjtx-2.1.2.tgz
tar xvfz wsjtx-2.1.2.tgz
cd wsjtx-2.1.2
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..




echo "***** Setup complete!!! *****"





