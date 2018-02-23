## Purpose

This little project is used to play around with Ansible.

The _master_ branch will not contain any interesting features,
only the scaffolding to try things out quickly and easily.

Experiments that turn out to be interesting enough to keep or
show to others will end up in branches.

## How to run

Run it like this:
```
ansible-playbook site.yml -vv
```

Another command I often use is this one that spits out all the facts:
```
ansible localhost -m setup
```
