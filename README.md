# ansible_from_properties

ansible jinja2 custom filter to read java properties file

require pyjq, to install, pip install pyjq

e.g.

```bash
- name: read java properties file
  set_fact: properties={{lookup('file','path/to/properties/file') | from_properties }}
```

use lookup to read in properties file

```
x.a=123
x.b=234
y.c=456
```

properties will be set to

```json
{
  "x": {
    "a": 123,
    "b": 234
  },
  "y": {
    "c": 456
  }
}
```
