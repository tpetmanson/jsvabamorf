# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import
import os
import json

def get_sources(src_dir='src', ending='.cpp'):
    """Function to get a list of files ending with `ending` in `src_dir`."""
    return [os.path.join(src_dir, fnm) for fnm in os.listdir(src_dir) if fnm.endswith(ending)]

# define directories for vabamorf source directories
dirs = ['etana', 'etyhh', 'fsc', 'json', 'proof']
src_dirs = [os.path.join('src', d) for d in dirs]

# define a list of C++ source files
lib_sources = []
vabamorf_src = os.path.join('src', 'etana', 'vabamorf.cpp')
for d in src_dirs:
    lib_sources.extend(get_sources(d))
lib_sources.append('vabamorf_wrap.cxx')

# define directories for vabamorf include directories
dirs.append(os.path.join('fsc', 'fsjni'))
include_dirs = [os.path.join('include', d) for d in dirs]

binding = {
    'targets': [{
        'target_name': 'jsvabamorf',
        'sources': lib_sources,
        'include_dirs': include_dirs,
        'cflags!': [ '-fno-exceptions' ],
        'cflags_cc!': [ '-fno-exceptions' ],
        }],
}

print (json.dumps(binding, indent=4))
