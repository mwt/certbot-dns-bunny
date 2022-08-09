Bunny.net DNS Authenticator Plugin for Certbot
==============================================

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
