"""
The `~certbot_dns_bunny.dns_bunny` plugin automates the process of
completing a ``dns-01`` challenge (`~acme.challenges.DNS01`) by creating, and
subsequently removing, TXT records using the `Bunny.net`_ API.

.. _Bunny.net: https://bunny.net?ref=e174a06f0l

.. note::
   The plugin is not installed by default.

Installation
------------

If you followed the official instructions, you likely installed certbot as a
snap. In that case, you can install the plugin by running:

.. code:: bash

    snap install certbot-dns-bunny
    sudo snap connect certbot:plugin certbot-dns-bunny

Alternatively, you can install certbot using pip and install the plugin by
running:

.. code:: bash

    pip install certbot-dns-bunny

Named Arguments
---------------

========================================  =====================================
``--dns-bunny-credentials``          Bunny credentials_ INI file.
                                          (Required)
``--dns-bunny-propagation-seconds``  The number of seconds to wait for DNS
                                          to propagate before asking the ACME
                                          server to verify the DNS record.
                                          (Default: 10)
========================================  =====================================


Credentials
-----------

Use of this plugin requires a configuration file containing Bunny API
credentials, obtained from your
`Bunny panel <https://panel.bunny.net/account>`_.

Bunny API keys are not scoped and give access to all account features.

.. code-block:: ini
   :name: certbot_bunny_token.ini
   :caption: Example credentials file using restricted API Key:

   # Bunny API token used by Certbot
   dns_bunny_api_key = a65e8ebd-45ab-44d2-a542-40d4d009e3bf

The path to this file can be provided interactively or using the
``--dns-bunny-credentials`` command-line argument. Certbot records the path
to this file for use during renewal, but does not store the file's contents.

.. caution::
   You should protect these API credentials as you would the password to your
   Bunny account. Users who can read this file can use these credentials
   to issue arbitrary API calls on your behalf. Users who can cause Certbot to
   run using these credentials can complete a ``dns-01`` challenge to acquire
   new certificates or revoke existing certificates for associated domains,
   even if those domains aren't being managed by this server.

Certbot will emit a warning if it detects that the credentials file can be
accessed by other users on your system. The warning reads "Unsafe permissions
on credentials configuration file", followed by the path to the credentials
file. This warning will be emitted each time Certbot uses the credentials file,
including for renewal, and cannot be silenced except by addressing the issue
(e.g., by using a command like ``chmod 600`` to restrict access to the file).


Examples
--------

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     -d example.com

.. code-block:: bash
   :caption: To acquire a single certificate for both ``example.com`` and
             ``www.example.com``

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     -d example.com \\
     -d www.example.com

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``, waiting 60 seconds
             for DNS propagation

   certbot certonly \\
     --authenticator dns-bunny \\
     --dns-bunny-credentials ~/.secrets/certbot/bunny.ini \\
     --dns-bunny-propagation-seconds 60 \\
     -d example.com

"""
