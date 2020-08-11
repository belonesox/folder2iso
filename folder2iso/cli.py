"""Console script for folder2iso."""
import argparse
import sys
import os
import pycdlib
import datetime

def main():
    """Console script for folder2iso."""
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=str, help='Folder to ISOse')

    args = parser.parse_args()

    from io import BytesIO

    if not os.path.exists(args.folder):
        return 
    lastname = os.path.split(args.folder)[-1]

    time_prefix = datetime.datetime.now().replace(microsecond=0).isoformat().replace(':', '-')
    isoname = "%(time_prefix)s-%(lastname)s.iso" % vars()

    iso = pycdlib.PyCdlib()

    iso.new(#joliet=True, 
            #rock_ridge='1.09', 
            udf='2.60',
            interchange_level=4)
    #directory

    exclude_dirs = ['.git', '.vagrant', 'tmp']

    for root, dirnames, filenames in os.walk(args.folder):
        ok = True
        for ex_ in exclude_dirs:
            if os.path.sep + ex_ + os.path.sep in root:
                ok = False
                break

        if not ok:
            continue        

        for directory in dirnames:
            if directory in exclude_dirs:
                continue
        if '.git' in root:
            continue
        if '.vagrant' in root:
            continue
            direct = "/" + directory
            print(direct)
            iso.add_directory(
                direct,
                #joliet_path=f'/{direct}', 
                #rr_name=directory
                )
        for file_ in filenames:
            file = '' + file_
            print(os.path.join(root, file))
            iso.add_file(
                os.path.join(root, file),
                f'/{file};3',
                #joliet_path=f'/{file}',
                #rr_name=file
                )
        # current_total_size += path.getsize(path.join(root, file))

    iso.write(isoname)
    iso.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
