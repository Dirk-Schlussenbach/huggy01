# huggy01
conda activate huggy
conda install cudatoolkit
conda install cuda --channel nvidia/label/cuda-12.3/win-64
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
conda install diffusers
