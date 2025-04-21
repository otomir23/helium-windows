#!/bin/bash -eu

_root_dir=$(dirname $(dirname $(readlink -f $0)))
_helium_repo=$_root_dir/helium-chromium

printf '%s-%s.%s' $(cat $_helium_repo/chromium_version.txt) $(cat $_helium_repo/revision.txt) $(cat $_root_dir/revision.txt)
