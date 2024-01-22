# huggy01
conda activate huggy
conda install cudatoolkit
conda install cuda --channel nvidia/label/cuda-12.3.0/win-64
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install install diffusers==0.20.2
conda update -n base -c defaults conda
