|Build Status|


.. |Build Status| image:: https://travis-ci.org/bazimov/simple_deploy.svg?branch=master
   :target: https://travis-ci.org/bazimov/simple_deploy


Simple Deploy script.
=====================

Takes 2 AMI-IDs one old, and one new. Gathers necessary information from old AMI-ID then launch the new ami with that info.
Attaches newly launched instances to the ELB that is serving old ami-id instances.
If instances launched with new AMI-ID are healthy, then deregisters old instances from ELB and terminates them.

Requirements
------------
- Python3
- boto3 AWS python sdk
- Proper EC2 & ELB IAM Policy permissions

Installing
----------

Install directly from the code:

::

    git clone https://github.com/bazimov/simple_deploy
    cd simple_deploy
    pip install -U .

Running
-------

::

    deploy --help

    export OLD_AMI_ID=ami-12345
    export NEW_AMI_ID=ami-56789

    deploy ${OLD_AMI_ID} ${NEW_AMI_ID}


Tests
------
Install tox and run.

``pip install tox``

::

    git clone https://github.com/bazimov/simple_deploy
    cd simple_deploy;
    tox

