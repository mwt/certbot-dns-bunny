Bunny.net DNS Authenticator Plugin for Certbot
==============================================

.. image:: https://img.shields.io/github/license/mwt/certbot-dns-bunny?style=for-the-badge
    :alt: License Badge
    :target: LICENSE

.. image:: https://img.shields.io/pypi/v/certbot-dns-bunny?style=for-the-badge
    :alt: PyPI Version Badge
    :target: https://pypi.org/project/certbot-dns-bunny/

.. image:: https://img.shields.io/pypi/pyversions/certbot-dns-bunny?style=for-the-badge
    :alt: Supported Python Versions Badge
    :target: https://pypi.org/project/certbot-dns-bunny/

.. image:: https://readthedocs.org/projects/certbot-dns-bunny/badge/?version=latest&style=for-the-badge
    :alt: Documentation Badge
    :target: https://certbot-dns-bunny.readthedocs.io/en/latest/

.. image:: https://flat.badgen.net/snapcraft/v/certbot-dns-bunny/?scale=1.4
    :alt: Snap Store Badge
    :target: https://snapcraft.io/certbot-dns-bunny

Full documentation is on `Read the Docs
<https://certbot-dns-bunny.readthedocs.io/en/latest/>`_.


Installation
------------

This package can be installed with pip

.. code:: bash

    pip install certbot-dns-bunny

and can be upgraded using the ``--upgrade`` flag

.. code:: bash

    pip install --upgrade certbot-dns-bunny

If you installed certbot as a snap, then you have to install this plugin as a snap as well.

.. code:: bash

    snap install certbot-dns-bunny
    sudo snap connect certbot:plugin certbot-dns-bunny

Credentials
-----------

.. code:: ini
   :name: certbot_bunny_token.ini

   # Bunny API token used by Certbot
   dns_bunny_api_key = a65e8ebd-45ab-44d2-a542-40d4d009e3bf

Examples
--------

.. code:: bash

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     -d example.com

.. code:: bash

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     -d example.com \\
     -d www.example.com

.. code:: bash

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     --dns-bunny-propagation-seconds 60 \\
     -d example.com
