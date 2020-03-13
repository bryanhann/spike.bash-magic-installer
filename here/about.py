"""
Inject into ~/.profile the following behaviour:
    1. Clone ~/.config/bash (if necessary)
    2. Source ~/.config/bash/profile

Inject into ~/.bashrc the following behaviour:
    1. Clone ~/.config/bash (if necessary)
    2. Source ~/.config/bash/profile

Injection appends lines to the end and removes any
previous injection.
"""
