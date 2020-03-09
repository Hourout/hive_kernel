import os
import sys
import json
import base64
import argparse

from IPython.utils.tempdir import TemporaryDirectory
from jupyter_client.kernelspec import KernelSpecManager

kernel_logo = b'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'
kernel_json = {"argv":[sys.executable, "-m", "hive_kernel", "-f", "{connection_file}"],
               "display_name":"Hive",
               "language":"sql"}

def install_my_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        with open(os.path.join(td, 'logo-64x64.png'), 'wb') as f:
            f.write(base64.b64decode(kernel_logo))
        print('Installing Jupyter Hive kernel spec.')
        KernelSpecManager().install_kernel_spec(td, 'Hive', user=user, replace=True, prefix=prefix)

def _is_root():
    try:
        return os.geteuid()==0
    except AttributeError:
        return False

def main(argv=None):
    parser = argparse.ArgumentParser(description='Install Jupyter KernelSpec for Hive Kernel.')
    prefix_locations = parser.add_mutually_exclusive_group()
    prefix_locations.add_argument('--user',
                                  help='Install Jupyter Hive KernelSpec in user homedirectory.',
                                  action='store_true')
    prefix_locations.add_argument('--sys-prefix',
                                  help='Install Jupyter Hive KernelSpec in sys.prefix. Useful in conda / virtualenv',
                                  action='store_true',
                                  dest='sys_prefix')
    prefix_locations.add_argument('--prefix',
                                  help='Install Jupyter Hive KernelSpec in this prefix',
                                  default=None)
    args = parser.parse_args(argv)

    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    install_my_kernel_spec(user=user, prefix=prefix)

if __name__ == '__main__':
    main()
