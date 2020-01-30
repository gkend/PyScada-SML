PyScada SML Extension
======================

This is an extension for PyScada to support data logging from Serial IR-Interface of Smart Meters.

This package is derived from `PyScada-GPIO <https://github.com/trombastic/PyScada-GPIO>`_. 

The OBIS Code is parsed with Python Package `pysml <https://github.com/mtdcr/pysml>`_ 

What is Working
---------------

- USB-Serial IR-Optocop with Smart Meter Types:
    - ISKA M175
    - ESY Q3MA 

What is not Working/Missing
---------------------------

- Replace bulk buffer reading to avoid dropping packages
- Register package at pypi.org
- Documentation
 
Installation
------------

Follow the `Pyscada Installation Guide <https://pyscada.readthedocs.io/en/master/installation.html>`_ 
and verify the instance is working.

Download this Repo and change into the directory

::

  git clone https://github.com/gkend/PyScada-SML.git
  cd PyScada-SML   

Install globally via pip3

::

  sudo pip3 install -e .

Add the PyScada sub-app to the installed apps list of Django.

::

  nano /var/www/pyscada/PyscadaServer/PyScadaServer/settings.py

::
  
  INSTALLED_APPS = [
        ...
        'pyscada.sml',
        ...
    ]
 
Restart Services

::
 
  sudo systemctl restart gunicorn 
  sudo systemctl restart pyscada  

PyScada-Backend Settings
--------------------------------

- Add SML Device and adjust the defaults to your instance. 
- Add SML Variable
   * Check required Obis Code `OBIS code IEC 62056 standard protocol <https://www.promotic.eu/en/pmdoc/Subsystems/Comm/PmDrivers/IEC62056_OBIS.htm>`_
   * Choose your Sensor Type

Contribute
----------

- Issue Tracker: https://github.com/gkend/PyScada-SML/issues
- Source Code: https://github.com/gkend/PyScada-SML

License
-------
The project is licensed under the _GNU General Public License v3 (GPLv3)_.

