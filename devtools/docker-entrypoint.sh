#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate base
conda activate mosdef_gomc

if [ "$@" == "jupyter" ]; then
	jupyter notebook --no-browser --notebook-dir /home/anaconda/data --ip="0.0.0.0"
else
	$@
fi
