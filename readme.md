## Make Ansible use different Python interpreters

The Ansible developers will not introduce an environment variable to control
which python interpreter is used but they give some pointers on how to make
it work, see [issue6345][].

But how can we make Ansible run a custom Ansible module (i.e. a single "task")
with a certain interpreter, e.g. in a certain virtualenv?
- This (global) setting is crucial, it introduces the dynamic lookup of the
  first python executable found in the path:
  `ansible_python_interpreter="/usr/bin/env python"`
  Caveat: it is a global setting, i.e. it will also affect Ansible itself.
  However, due to its flexible nature this does not feel wrong to me. In fact,
  that's how most Python scripts choose their interpreter anyway.
- The task that should run with another interpreter must be annotated with
  `environment:` setting `PATH` to a value that will make the intended
  interpreter the "best" (first) hit.

Run it like this:
```
ansible-playbook site.yml -vv
```



[issue6345]: https://github.com/ansible/ansible/issues/6345#issuecomment-181981760
