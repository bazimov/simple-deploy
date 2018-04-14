|Build Status|


Simple Deploy script.
=====================

Takes 2 AMI IDs one old, and one new. Gather necessary information from old AMI ID then launch the new ami with that info.
If instances launched with new AMI ID are healthy, then deregisters old instances from ELB and terminates them.

# Requirements
- Python3
- boto3 AWS python sdk

Installing
----------

Install directly from the code:

::
    git clone https://github.com/bazimov/simple_deploy
    cd simple_deploy
    pip install -r requirements.txt

Running
-------

::
    ./deploy.py --help

    export OLD_AMI_ID=ami-12345
    export NEW_AMI_ID=ami-56789
    ./deploy.py ${OLD_AMI_ID} ${NEW_AMI_ID}


Tests
------
Install tox and run.

``pip install tox``

::
    git clone https://github.com/bazimov/simple_deploy
    cd simple_deploy;
    tox

